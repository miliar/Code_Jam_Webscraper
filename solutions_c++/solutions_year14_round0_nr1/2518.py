#include <iostream>
#include <cstdio>
#include <cstring>
#include <set>
#include <vector>
#include <map>
#include <algorithm>
#include <string>
#include <ctime>
#include <cstring>
#include <sstream>
#include <fstream>
using namespace std;

int main( )
{   
    /*clock_t start;
    start=clock();
    /***********************************************/
    freopen("A-small-attempt0.in", "rt", stdin);
    freopen("A-small.out", "wt", stdout);
    int t;
    cin>>t;
    for(int i=1; i<t+1; ++i) {
        cout<<"Case #"<<i<<": ";
        int flag=0, ans=0, mat1[5][5], mat2[5][5], row1, row2; 
        
        cin>>row1;
        for(int j=1; j<5; ++j)
            for(int k=1; k<5; ++k)
                cin>>mat1[j][k];
        cin>>row2;
        for(int j=1; j<5; ++j)
            for(int k=1; k<5; ++k)
                cin>>mat2[j][k];
        

        for(int j=1; j<5; ++j){
            for(int k=1; k<5; ++k){
                if(mat1[row1][j]==mat2[row2][k]){
                    if(flag==1){
                        flag=2;
                        goto end;
                    }
                    flag=1;
                    ans=mat1[row1][j];
                }
            }
        }
        end: ;
        if(flag==0)
            cout<<"Volunteer cheated!\n";
        else if (flag==1)
            cout<<ans<<endl;
        else if(flag==2)
            cout<<"Bad magician!\n";
    }
    /************************************************
    start=clock()-start;
    printf("Time = %f\n", (float)start/CLOCKS_PER_SEC);*/
    return 0 ;
}