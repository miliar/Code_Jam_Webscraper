#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cmath>
#include <bitset>
#include <map>
#include <stdlib.h>
#include <ctype.h>
#include <string>
#include <string.h>
#include <set>
#include <stack>
#include <deque>
#include <queue>
    using namespace std;

int BFS(vector <int> st, vector <int> target)
{
    int ret = 0;
    set < vector <int> > vis;
    queue < pair < vector <int> , int> > q;
    q.push(make_pair(st,0));
    vis.insert(st);
    while(!q.empty())
    {
        vector <int> v = q.front().first , v2;
        int r = q.front().second;
        q.pop();
        if(v == target)
            return r;
        for(int i=0;i<v.size();i++){
            v2 = v;
            for(int j=0;j<=i;j++){
                v2[j] ^= 1;
            }
            reverse(v2.begin(),v2.begin()+i+1);
            if(vis.find(v2) == vis.end()){
                q.push( make_pair(v2,r+1));
                vis.insert(v2);
            }
        }
    }
    return ret;

}
int main ()
{
    //freopen("input.txt","r",stdin);
    freopen("B-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    int TC;
    string s;
    cin>>TC;
    for(int test=1;test<=TC;test++)
    {
        cin>>s;
        vector <int> in,tar;
        for(int i=0;i<s.size();i++){
            in.push_back(s[i] == '+');
            tar.push_back(1);
        }
        printf("Case #%d: %d\n",test,BFS(in,tar));
    }
    return 0;
}
