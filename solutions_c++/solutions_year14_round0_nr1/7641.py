#include<bits/stdc++.h>
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
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int t,a,x,c[20],i,j,cs=1;
    cin>>t;
    while(t--){
        cin>>a;
        CLR(c);
        for(i = 0;i<4;i++){
            for(j = 0;j<4;j++){
                cin>>x;
                if(i == a-1){
                    c[x]++;
                }

            }
        }
        int b;
        cin>>b;
        int ans = -1;
        for(i = 0;i<4;i++){
            for(j = 0;j<4;j++){
                cin>>x;
                if(i == b-1){
                    c[x]++;
                    if(c[x]==2){
                        if(ans==-1) ans = x;
                        else ans = -2;
                    }
                }
            }
        }
        printf("Case #%d: ",cs++);
        if(ans == -2) printf("Bad magician!\n");
        else if(ans==-1) printf("Volunteer cheated!\n");
        else printf("%d\n",ans);
    }
	return 0;
}
