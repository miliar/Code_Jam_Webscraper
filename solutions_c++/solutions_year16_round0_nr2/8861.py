#include <algorithm>
#include <iostream>
#include <iterator>
#include <numeric>
#include <sstream>
#include <fstream>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
#include <bitset>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <map>
#include <set>
using namespace std;

#define len(x) ((int)(x.size()))
#define inf 1061109567





int main(){
    ios_base::sync_with_stdio(0);
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    
    int tst;
    cin>>tst;
    for(int test=1;test<=tst;test++){
        string s;
        cin>>s;
        int cnt=0;
        int flag=1;

        vector<int> v;
        for(int i=0;i<s.size();i++){
            v.push_back(s[i]=='+');
        }
        int target=1;

        int n=s.size();
        while(n--){

            if(v[n]!=target){
                cnt++;
                target=1-target;
            }

        }
        cout<<"Case #"<<test<<": "<<cnt<<endl;
    } 

}


