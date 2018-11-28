#include <iostream>
#include <cstdio>
#include <set>
using namespace std;

int a[5][5],b[5][5];
int n,m;

int ans;
int type;
set<int>st;
set<int>::iterator it;

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T,cas=0;
    scanf("%d",&T);
    while (T--) {
        type=0;
        st.clear();
        scanf("%d",&n);
        for (int i=1;i<=4;i++){
            for (int j=1;j<=4;j++){
                scanf("%d",&a[i][j]);
                if (n==i) st.insert(a[i][j]);
            }
        }
        scanf("%d",&m);
        for (int i=1;i<=4;i++){
            for (int j=1;j<=4;j++){
                scanf("%d",&b[i][j]);
                if (i==m){
                    it=st.find(b[i][j]);
                    if (it!=st.end()){
                        ans=b[i][j];
                        type++;
                    }
                }
            }
        }
        printf("Case #%d: ",++cas);
        if (type==0) printf("Volunteer cheated!\n");
        else if (type==1) printf("%d\n",ans);
        else printf("Bad magician!\n");
    }
    return 0;
}
