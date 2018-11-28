#include<iostream>
#include<fstream>
#include<string>
#include<math.h>
using namespace std;

int main()
{
    ifstream infile;
    ofstream outfile;

    int S,K,testCase,C,i;
    infile.open("testInput.in");
    outfile.open("testOutput.out");
    infile>>testCase;
    for(i=0;i<testCase;i++){
        infile>>K;
        infile>>C;
        infile>>S;
        //cout<<K<<" "<<C<<" "<<S<<endl;
        outfile<<"Case #"<<i+1<<":";
        for(int j=1;j<=S;j++){
            outfile<<" "<<j;
        }
        outfile<<endl;



    }

    infile.close();
    outfile.close();

    return 0;
}
