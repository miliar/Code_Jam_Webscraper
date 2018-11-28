#include<iostream>
#include<fstream>
#include<string>
using namespace std;
int main()
{
    int t;
    ofstream myfile;
    myfile.open ("rajvir1.txt");
    ifstream myfile2;
    myfile2.open("B-large.in");
    myfile2>>t;
    int z=t;
    while(t--)
    {
        string a;
        int a2[4]={0,1,2,1};
        myfile2>>a;
        int sumu=0;
        if(a.length()==1)
        {
            if(a[0]=='-')
                myfile<<"Case #"<<z-t<<": 1\n";
            else
                myfile<<"Case #"<<z-t<<": 0\n";
        }
        else
        {
        for(int i=1;i<a.length();i++)
        {
            if(a[i-1]!=a[i])
            {
                sumu++;
            }
         }
             if(a[a.length()-1]=='+')
                myfile<<"Case #"<<z-t<<": "<<sumu<<"\n";
            else
                myfile<<"Case #"<<z-t<<": "<<sumu+1<<"\n";


        }
    }
    return 0;
}
