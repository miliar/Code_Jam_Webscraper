#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <set>
#include <queue>
#include <stack>
#include <map>
#include <list>
#include <utility>
#include <algorithm>
#include <cassert>
#include <fstream>
#include <iomanip>
using namespace std;
typedef long long ll; 
typedef unsigned long long ull;
typedef pair<int,int> pii;
typedef pair<int, bool> pib;
typedef pair<ll,ll> pll;
#define MOD %1000000007
#define F first
#define S second
#define MP make_pair
#define PB push_back




ll reverse(ll n){
    ll t=0;
    while(n>0){
			
        t+=n%10;
        t*=10;
        n/=10;
    }
    return t/10;
}
ll visited[1000001]={0};
int BFS(int n)
{
    ll top;
    queue<ll> q;
    q.push(1);
    
    memset (visited,0,sizeof(visited));
    visited[1]=1;
    while(q.size())
    {
        top=q.front();
        //cout<<top<<endl;
        q.pop();
        if(visited[top+1]==0){
            visited[top+1]=visited[top]+1;
            if(top+1==n){
                return visited[top+1];
            }
            q.push(top+1);
        }
        if(visited[reverse(top)]==0){
            visited[reverse(top)]=visited[top]+1;
            if(reverse(top)==n){
                return visited[top+1];
            }
            if(reverse(top)>n){
                continue;
            }
            q.push(reverse(top));
        }
    }

    return 1;
}
int main(){
    ios_base::sync_with_stdio(false);cin.tie(0);
    ifstream fin("Aip.in");
    ofstream fout("Aop.out");
    ll n ,t;
    fin>>t;
    
    for(int caseno=1;caseno<=t;caseno++){
        fin>>n;
        //MS0(visited);
        fout<<"Case #"<<caseno<<": "<<BFS(n)<<endl;
    }

    //system("pause");
    return 0;
}  
