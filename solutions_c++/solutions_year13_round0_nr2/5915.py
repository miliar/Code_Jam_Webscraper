#include<iostream>
#include<conio.h>
#include<stdio.h>
#include<fstream>

using namespace std;

int main() {

    ofstream myfile;
      myfile.open ("ans2.txt");

    int lawn[3][3]={2,1,2,
                    1,1,1,
                    2,1,2};

    int r=3,c=3;
    int nos=1;
    //cout<<"now : "<<endl;

    fflush(stdout);

    cin>>nos;

    for(int k=0;k<nos;k++) {


    //cout<<"rc : "<<endl;
    fflush(stdout);
    cin>>r>>c;
    const int n=r;
    const int m=c;


    fflush(stdout);
    char lawn[n][m];
    for(int pr=0;pr<n;pr++)
    for(int pc=0;pc<m;pc++)
    cin>>lawn[pr][pc];

    int flag=0;
    for(int i=0;i<n;i++)
    for(int j=0;j<m;j++) {
        int flag1=0;
        for(int k=0;k<m;k++) {
            if(lawn[i][k]>lawn[i][j]) {
                flag1=1;
            }
        }
        int flag2=0;
        for(int k=0;k<n;k++) {
            if(lawn[k][j]>lawn[i][j]) {
                flag2=1;
                break;
            }
        }
        if(flag1==1 && flag2==1) {
            flag=1;
            break;
        }
    }
    if(flag==1) cout<<"Case #"<<k+1<<": NO\n";
    else  cout<<"Case #"<<k+1<<": YES\n";
    }


    myfile.close();
    return 0;
}
