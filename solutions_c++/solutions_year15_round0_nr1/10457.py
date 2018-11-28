#include <iostream>
#include <fstream>
using namespace std;
int main()
{
    ifstream infile("A-small-attempt1.in");
    ofstream offile("output-small.txt");
    int testcases,nople,ple_std,ple_req;
    infile>>testcases;
    string audience;
    for(int m=1;m<=testcases;m++)
    {
        ple_std=0;
        ple_req=0;
        infile>>nople;
        infile>>audience;
        for(int i=0;i<=nople;i++)
        {
            if(ple_std >= i && (audience[i]-'0')!=0)
            {
                cout<<"a "<<audience[i]<<endl;
                ple_std+=(audience[i]-'0');
                cout<<"std "<<ple_std<<endl;
            }
            else if((audience[i]-'0')!=0)
            {
                ple_req+=(i-ple_std);
                ple_std+=(ple_req+(audience[i]-'0'));
                cout<<"p "<<ple_req<<endl;
            }
        }
        offile<<"Case #"<<m<<": "<<ple_req<<endl;
        cout<<endl;
    }
    return 0;
}
