#include <iostream>
#include <set>
#include <cstdio>
using namespace std;

set <int> s;
int _;
int i,j;
int a,b,te;
int cas=0;

int main(){
    //freopen("A-small-attempt0.in","r",stdin);
    //freopen("a.out","w",stdout);
    scanf("%d",&_);
    while(_--){
        scanf("%d",&a);
        for (int i=1;i<=4;i++)
        for (int j=1;j<=4;j++){
            scanf("%d",&te);
            if (i==a) s.insert(te);
        }
        scanf("%d",&a);
        int sav=0;
        for (int i=1;i<=4;i++)
        for (int j=1;j<=4;j++){
            scanf("%d",&te);
            if (i==a && s.count(te)){
                sav = te;
                s.erase(te);
            }
        }
        printf("Case #%d: ",++cas);
        if (s.size()==3) printf("%d\n",sav);
        if (s.size()==4) printf("Volunteer cheated!\n");
        if (s.size()<3) printf("Bad magician!\n");
        s.clear();


    }

}
