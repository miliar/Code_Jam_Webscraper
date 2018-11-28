#include <fstream>
#include <iostream>
#include <string>
#include <complex>
#include <math.h>
#include <set>
#include <vector>
#include <map>
#include <queue>
#include <stdio.h>
#include <stack>
#include <algorithm>
#include <iomanip>
#include <list>
#include <ctime>
#include <memory.h>
#include <bitset>
#include <climits>

#define F first
#define S second
#define endl "\n"
#define mp make_pair
#define pb push_back
#define MOD 1000000007
#define pi 3.141592653589793
#define y1 zjdfshnvoavaofobiopj
using namespace std;

map<string, int>mymap, dist;
int t, k;
string st;

void bfs(string ts)
{
    queue<string>q;
    q.push(ts);
    while(q.size())
    {
        string node = q.front();
        q.pop();
        string save;
        //cout<<"current node = "<<node<<endl;
        for(int i = 0; i < ts.size(); i++)
        {
            save = node;
            for(int j = i; j+1; j--)
            {
                if(save[j] == '+')
                    save[j] = '-';
                else
                    save[j] = '+';
            }
            //cout<<"                    "<<save<<endl;
            if(!mymap[save] && dist[save] == 0)
                q.push(save), dist[save] = dist[node]+1, mymap[save] = 1;
        }
    }
}

int main(){
//freopen("input.txt", "r", stdin);
//freopen("/home/str/Downloads/B-small-attempt0.in", "r", stdin);
//freopen("output.txt", "w", stdout);
ios_base::sync_with_stdio(0);
cin.tie(0);

cin>>t;
while(t--)
{
    ++k;
    cin>>st;
    string dest = "";
    mymap.clear(), dist.clear();
    for(int i = 0; i < st.size(); i++)
    dest+='+';
    if(st != dest)
        bfs(st);
    cout<<"Case #"<<k<<": "<<dist[dest]<<endl;
}

return 0;}
