#include <iostream>
#include <cstdio>

using namespace std;

#define DEBUG

int main()
{
    #ifdef DEBUG
    freopen("a.in", "r", stdin);
    freopen("outfile.txt", "w", stdout);
    #endif

    long int temp,loc,j,k,t,i,a1[4][4],r1,r2,a2[4][4];
    cin>>t;
    for(i=1;i<=t;i++) {
        cin>>r1;
        r1--;
        for(j=0;j<4;j++)
            for(k=0;k<4;k++)
                cin>>a1[j][k];
        cin>>r2;
        r2--;
        for(j=0;j<4;j++)
            for(k=0;k<4;k++)
                cin>>a2[j][k];
        temp=0;
        for(k=0;k<4;k++) {
        for(j=0;j<4;j++) {
            if(a1[r1][k]==a2[r2][j]&&temp==0) {
                loc=a1[r1][k];
                temp=1;
            } else if(a1[r1][k]==a2[r2][j]&&temp==1) {
                temp=2;
            }
        }
        }
        if(temp==0)
            cout<<"Case #"<<i<<": Volunteer cheated!\n";
        else if(temp==1)
            cout<<"Case #"<<i<<": "<<loc<<endl;
        else if(temp==2)
            cout<<"Case #"<<i<<": Bad magician!\n";
    }

    return 0;
}
