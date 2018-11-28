#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream infile("A-small-attempt3.in");
    ofstream outfile("A-small-attempt3.txt");

    int t;
    int row1,row2;
    int magic1[4][4];
    int magic2[4][4];
    int ans;
    int counter;

    infile>>t;
    for(int i=0;i<t;i++){
        counter = 0;
        infile>>row1;
        for(int j=0;j<4;j++)
            for(int k=0;k<4;k++)
                infile>>magic1[j][k];

        infile>>row2;
        for(int j=0;j<4;j++)
            for(int k=0;k<4;k++)
                infile>>magic2[j][k];

        for(int j=0;j<4;j++)
            for(int k=0;k<4;k++){
                if(magic1[row1-1][j]==magic2[row2-1][k]){
                    counter++;
                    ans = magic1[row1-1][j];
                }
            }
        outfile<<"case #"<<i+1<<": ";
        if(counter==0) outfile<<"Volunteer cheated!"<<endl;
        if(counter==1) outfile<<ans<<endl;
        if(counter>1) outfile<<"Bad magician!"<<endl;
    }

    return 0;
}
