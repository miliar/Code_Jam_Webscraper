#include <iostream>
#include <stdio.h>
#include <string.h>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <algorithm>
#include <iomanip>
#include <fstream>

using namespace std;

int main()
{
    int test;
    cin>>test;
    int c=1;
    ofstream myfile;
    myfile.open ("asdk.txt");
    while (test--){
        int r1;
        int a[4][4], b[4][4];
        cin>>r1;
        for (int i=0;i<4;i++){
            for (int j=0;j<4;j++){
                cin>>a[i][j];
            }
        }

        int r2;
        cin>>r2;
        for (int i=0;i<4;i++){
            for (int j=0;j<4;j++){
                cin>>b[i][j];
            }
        }
        int cnt=0;
        int ans=-1;
        for (int i=0;i<4;i++){
            for (int j=0;j<4;j++){
                if (a[r1-1][i]==b[r2-1][j]){
                    cnt++;
                    ans=a[r1-1][i];
                }
            }
        }

    //myfile << "Writing this to a file.\n";

     /*   cout<<"Case #"<<c<<": ";
        if (cnt==1){
            cout<<ans<<"\n";
        } else if (cnt>1){
            cout<<"Bad magician!\n";
        } else {
            cout<<"Volunteer cheated!\n";
        }
        */
        myfile <<"Case #"<<c<<": ";
        if (cnt==1){
            myfile<<ans<<"\n";
        } else if (cnt>1){
            myfile<<"Bad magician!\n";
        } else {
            myfile<<"Volunteer cheated!\n";
        }

        c++;

    }
    myfile.close();
    return 0;
}
