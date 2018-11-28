#include <iostream>
#include <sstream>
#include <fstream>
#include <limits>
#include <limits.h>
#include <list>
#include <cstdio>
#include <cmath>
#include <string>
#include <string.h>
#include <algorithm>
#include <queue>
#include <map>
#include <vector>
#define min(a,b) a<b?a:b
#define max(a,b) a>b?a:b
#define INF 2000000000
#define sci(i) scanf("%d",&i)
#define scc(i) scanf("%c",&i)
#define scii(i,j) scanf("%d%d",&i,&j)
#define scl(i) scanf("%I64d",&i)
#define scs(i) scanf("%s",i)
#define lp(i,n) for(int i=0;i<n;i++)
#define vlp(v,i) for(int i=0;i<v.size();i++)
using namespace std;

typedef long long ll;
typedef char ch;
typedef string st;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef pair<int,int>pii;
typedef pair<char,char>pcc;
typedef pair<ll,ll>pll;
typedef map<int,int> mii;
typedef map<ll,ll> mll;
typedef map<char,int> mci;
typedef map<int,bool> mib;
typedef map<char,bool> mcb;

int di[]={0,1,0,-1,1,-1,1,-1};
int dj[]={1,0,-1,0,1,-1,-1,1};
vi arr;
int n,ans = INF;
void calc(int s){
    int sum =0 ;
    lp(i,n)sum = max(arr[i],sum);
    sum+=s;
    ans = min(ans,sum);
}
void tryit(int s, map<vi,bool> &vis){
    sort(arr.begin(),arr.begin()+n);
    if(vis[arr])return;
    else vis[arr]=true;
    calc(s);
    for(int i=0;i<n;i++){
        if(arr[i]==1)continue;
        for(int j=1;j<=arr[i]/2;j++){
            vi temp = arr;
            arr[i]-=j;
            arr[n]=j;
            n++;
            tryit(s+1,vis);
            calc(s+1);
            n--;
            arr = temp;
        }
    }
}
int main()
{
    freopen ("new.txt","w",stdout);
    int N;sci(N);
    lp(i,10000)arr.push_back(0);
    lp(I,N){
        ans = INF;
        sci(n);
        lp(i,n)sci(arr[i]);
        if(n  == 4 &&  (arr[0] == arr[1] && arr[1] == arr[2] && arr[2]== arr[3]) ){
            ans = arr[0];

        } else if (  n  == 5 &&  arr[0] == arr[1]&& arr[1] == arr[2] && arr[2] == arr[3] && arr[3] == arr[4]) ans = arr[0];
        else if (  n  == 6 &&  (arr[0] == arr[1]&& arr[1] == arr[2] && arr[2] == arr[3]&& arr[3] == arr[4] && arr[4] == arr[5]) ) ans = arr[0];
        else {

        map<vi,bool>vis;
        tryit(0,vis);
        }
        cout << "Case #"<<I+1<<": "<<ans<<endl;
    }
    return 0;
}
