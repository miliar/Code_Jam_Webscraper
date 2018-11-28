#include <iostream>
#include <cstdio>
#include <vector>

#define pb push_back
#define FI(ii,aa,bb) for(int ii=aa;ii<=bb;ii++)

using namespace std;

int A[5][5],B[5][5],n,m,N;

int main(void){
      freopen("gir.in","r",stdin);freopen("cik.out","w",stdout);


      scanf("%d",&N);

      FI(t,1,N)
      {
            scanf("%d",&n);

            FI(i,1,4)
             FI(j,1,4) scanf("%d",A[i]+j);

                        scanf("%d",&m);
            FI(i,1,4)

             FI(j,1,4) scanf("%d",B[i]+j);

            vector<int> ans;

            FI(i,1,4)


             FI(j,1,4){
                  if(A[n][i]==B[m][j]) ans.pb(A[n][i]);
            }

                        printf("Case #%d: ",t);

            if(ans.size()==0)             printf("Volunteer cheated!\n");

            else if(ans.size()==1) printf("%d\n",ans[0]);else printf("Bad magician!\n");}



      return 0;
}
