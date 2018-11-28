#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    int caseNo=1,t,r,c,w;
    //long int n,N,temp,temphalf;
    ifstream input;
    ofstream output;
    output.open("output.txt");
    input.open("input.txt");
    input>>t;
    //cout<<t;
    while(caseNo<=t)
    {
        input>>r>>c>>w;
        output<<"Case #"<<caseNo<<": "<<(c+w-1)/w+(w-1)<<endl;
        caseNo++;
    }
    input.close();
    output.close();
}
