#include<iostream>
#include<fstream>
using namespace std;
int main(){
    ifstream inF("input.txt");
    ofstream outF("output.txt");
    int x;
    inF>>x;
    for(int COUNT=1;COUNT<=x;COUNT++){
    int arr1[4][4],arr2[4][4];
    int i,j;
    int r1,r2;
    inF>>r1;
    for(i=0;i<4;i++)
        for(j=0;j<4;j++)
            inF>>arr1[i][j];
    inF>>r2;
    for(i=0;i<4;i++)
        for(j=0;j<4;j++)
            inF>>arr2[i][j];
    r1--,r2--;
    int howmany=0;
    int index=-1;
    for(i=0;i<4;i++)
        for(j=0;j<4;j++)
            if(arr1[r1][i]==arr2[r2][j])
                    howmany++,index=arr1[r1][i];

        if(howmany==0){
            outF<<"Case #"<<COUNT<<": Volunteer cheated!"<<endl;continue;
        }
        if(howmany>1){
            outF<<"Case #"<<COUNT<<": Bad magician!"<<endl;continue;
        }
        if(howmany==1){
            outF<<"Case #"<<COUNT<<": "<<index<<endl;continue;
        }
    }
        return 0;
}
