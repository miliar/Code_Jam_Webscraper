#include<iostream>      
#include<cstdio>      
#include<map>      
#include<cstring>      
#include<cmath>      
#include<vector>      
#include<algorithm>      
#include<set>      
#include<stack>    
#include<string>      
#include<ctime>    
#include<queue>      
#define inf 0x3f3f3f3f   
#define maxn 210005      
#define eps 1e-8    
#define zero(a) fabs(a)<eps      
#define Min(a,b) ((a)<(b)?(a):(b))      
#define Max(a,b) ((a)>(b)?(a):(b))      
#define pb(a) push_back(a)      
#define mp(a,b) make_pair(a,b)      
#define mem(a,b) memset(a,b,sizeof(a))      
#define LL long long      
#define MOD 1000000007    
#define sqr(a) ((a)*(a))      
#define Key_value ch[ch[root][1]][0]      
#define test puts("OK");      
#define pi acos(-1.0)    
#define lowbit(x) ((-(x))&(x))    
#define HASH1 1331    
#define HASH2 10001 
#define lson step<<1
#define rson step<<1|1   
#define C   240      
#define vi vector<int>    
#define TIME 10      
//#pragma comment(linker, "/STACK:1024000000,1024000000")      
using namespace std;
int a[105][105];
int b[105][105];
int main(){
    int t,cas=0;
    //freopen("B-large.in","r",stdin);
    //freopen("out.txt","w",stdout);
    scanf("%d",&t);
    while(t--){
        int n,m;
        scanf("%d%d",&n,&m);
        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++){
                b[i][j]=100;
                scanf("%d",&a[i][j]);
            }
        for(int i=0;i<n;i++){
            int mx=0;
            for(int j=0;j<m;j++)
                mx=max(mx,a[i][j]);
            //cout<<mx<<endl;
            for(int j=0;j<m;j++)
                b[i][j]=min(b[i][j],mx);
        }
        
        for(int j=0;j<m;j++){
            int mx=0;
            for(int i=0;i<n;i++)
                mx=max(mx,a[i][j]);
           // cout<<mx<<endl;
            for(int i=0;i<n;i++)
                b[i][j]=min(b[i][j],mx);
        }
        bool flag=true;
        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++)
                if(a[i][j]!=b[i][j])
                    flag=false;
        printf("Case #%d: %s\n",++cas,flag?"YES":"NO");
    }
    return 0;
}