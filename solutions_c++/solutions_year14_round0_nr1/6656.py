#include <bits/stdc++.h>

#define FI(ii,aa,bb) for(ll ii=aa;ii<=bb;ii++)
#define F(ii,aa,bb) for(ll ii=aa;ii<bb;ii++)
#define TF(ii,aa,bb) for(ll ii=aa;ii>=bb;ii--)
#define mp make_pair
#define pii pair<ll,ll>
#define st first
#define nd second
#define pb push_back
#define pdd pair<double,double>
#define ll long long
#define inf (ll_MAX)

using namespace std;

int A[5][5],B[5][5],n,m;

int main()
{
      freopen("in.in","r",stdin);
      freopen("out.out","w",stdout);

      int T;
      scanf("%d",&T);
      FI(t,1,T){
            scanf("%d",&n);
            FI(i,1,4) FI(j,1,4) scanf("%d",A[i]+j);
            scanf("%d",&m);
            FI(i,1,4) FI(j,1,4) scanf("%d",B[i]+j);
            vector<int> ans;
            FI(i,1,4) FI(j,1,4){
                  if(A[n][i]==B[m][j]) ans.pb(A[n][i]);
            }
            printf("Case #%d: ",t);
            if(ans.size()==0) printf("Volunteer cheated!\n");
            else if(ans.size()==1) printf("%d\n",ans[0]);
            else printf("Bad magician!\n");

      }
      return 0;
}
