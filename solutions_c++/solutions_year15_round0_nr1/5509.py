#include<bits/stdc++.h>
using namespace std;

#define sin(x) scanf("%d",&x)
#define sin2(x,y) scanf("%d%d",&x,&y)
#define sin3(x,y,z) scanf("%d%d%d",&x,&y,&z)

#define pb push_back
#define mp make_pair
#define y1 asdnqw
#define next mdamdamda
#define right praviy
#define x first
#define y second
#define endl "\n"
const int N=1200007;
int n,m,cur,ans,x;
char ch;
main(){
    cin.tie(0);ios_base::sync_with_stdio(0);
    //freopen("segmentupdate.in","r",stdin);freopen("segmentupdate.out","w",stdout);
    freopen("1.txt","r",stdin);
    freopen("2.txt","w",stdout);
    cin>>n;
    for(int i=1;i<=n;++i){
        cin>>m;
        cur=0;ans=0;
        for(int i=0;i<=m;++i){
            cin>>ch;x=ch-'0';
            if(cur<i){
                ans+=i-cur;
                cur=i;
            }
            cur+=x;
        }
        cout<<"Case #"<<i<<": "<<ans<<endl;
    }

}
