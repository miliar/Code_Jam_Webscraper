#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string.h>
#include <stdio.h>
#define all(v) (v).begin(),(v).end()
#define rall(v) (v).rbegin(),(v).rend()
using namespace std;  // H A M L E T
long long toi(string s){istringstream is(s);long long x;is>>x;return x;}
string tos(long long t){stringstream st; st<<t;return st.str();}
long long gcd(long long a, long long b){return __gcd(a,b);}long long lcm(long long a,long long b){return a*(b/gcd(a,b));}

int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    
    int tc;
    cin>>tc;
    int c[10001];
    bool visited[10001];

    for(int caso=1;caso<=tc;caso++){
        cout<<"Case #"<<caso<<": ";
        int n,x;
        cin>>n>>x;
        for(int i=0;i<n;i++)scanf("%d",&c[i]);
        sort(c,c+n);
        memset(visited,0,sizeof(visited));
        int cont=0;
        
        for(int i=0;i<n;i++){
            if(visited[i])continue;
            int val=c[i];
            int dif=x-c[i];
            int id=-1;
            
            for(int j=i+1;j<n;j++){
                if(visited[j])continue;
                if(c[j]<=dif)
                    id=j;
                else
                    break;
            }
            
            cont++;
            if(id!=-1)visited[id]=1;    
        }
        
        cout<<cont<<endl;
    }
    
    
    return 0;
}
