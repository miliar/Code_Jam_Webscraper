#include<iostream>
#include<fstream>
#include<string>
using namespace std;

int main()
{
    ifstream infile;
    ofstream outfile;
    int testCase=1,i,counter=0;
    char current='+';
    string panCake;

    infile.open("B-large.in");
    outfile.open("B-large-output.out");
    infile>>testCase;
    for(i=0;i<testCase;i++){
        counter=0;
        current='+';
        infile>>panCake;
        for(int j=panCake.size()-1;j>=0;j--){
            if(panCake[j]!=current){
                counter++;
                current=panCake[j];
            }
        }
        outfile<<"case #"<<i+1<<": "<<counter<<endl;
    }
    //cout<<testCase<<endl;
    infile.close();
    outfile.close();
    return 0;
}
