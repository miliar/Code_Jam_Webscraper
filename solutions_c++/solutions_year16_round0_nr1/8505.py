#include<cstdio>
#include<cstring>
#include<cmath>
#include<cctype>
#include<vector>
#include<stack>
#include<queue>
#include<set>
#include<map>
#include<algorithm>
#include<iostream>
#include<sstream>
#include<numeric>
#include<fstream>
using namespace std;
#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))
#define SET(a) memset(a,-1,sizeof(a))
#define CLR(a) memset(a,0,sizeof(a))
#define pb push_back
#define all(a) a.begin(),a.end()
#define eps (1e-9)
#define inf (1<<29)
#define i64 long long
#define u64 unsigned i64

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.ans","w",stdout);
    bool vis[10];
    int t, cs = 1, n;
    cin>>t;
    while(t--){
        cin>>n;
        printf("Case #%d: ",cs++);
        if(n == 0){
            cout<<"INSOMNIA"<<endl;
            continue;
        }
        CLR(vis);
        int m = n;
        while(1){
            int x = n;
            while(x){
                vis[x%10] = 1;
                x/=10;
            }
            int i;
            for(i = 0;i<=9;i++)
                if(!vis[i]) break;
            if(i>9) break;
            n+=m;
        }
        cout<<n<<endl;
    }
	return 0;
}
