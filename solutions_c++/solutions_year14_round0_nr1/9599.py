#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;
using namespace std;
int main() {
    int t,ans1,ans2,dato;
    //freopen("magic.c","r",stdin);
   // freopen("magic.out","w",stdout);
    scanf("%d",&t);
    for(int ca=1; ca<=t; ca++) {
        scanf("%d",&ans1);
        vector <int> G1[6],G2[6];
        for(int j=1; j<=4; j++)
            for(int i=1; i<=4; i++) {
                scanf("%d",&dato);
                G1[j].push_back(dato);
            }
        scanf("%d",&ans2);
        for(int j=1; j<=4; j++)
            for(int i=1; i<=4; i++) {
                scanf("%d",&dato);
                G2[j].push_back(dato);
            }

        int sw=0,real;
        for(int i=0; i<4; i++) {
            for(int j=0; j<4; j++) {
                if(G1[ans1][i]==G2[ans2][j]) {
                    sw++;
                    real=G1[ans1][i];
                }
            }

        }
        printf("Case #%d: ",ca);
        if(sw==1)
            cout<<real<<endl;
        else if(sw>1)
            cout<<"Bad magician!"<<endl;
        else
            cout<<"Volunteer cheated!"<<endl;
    }
    return 0;
}
