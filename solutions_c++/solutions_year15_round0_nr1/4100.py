#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    ifstream in("A-large.in");
    ofstream out("coutput.txt");
int testcase;
in>>testcase;

for(int t=0;t<testcase;t++)
{
        out<<"Case #"<<(t+1)<<": ";
        int s;
        in>>s;
        string x;
        in>>x;
        int count=0;
        int stood=0;
        int y=0;
        for(int i=0;i<x.size();i++)
        {
                
                if(x[i]=='0')
                continue;
                y=int(x[i]-48);
                if(stood>=i)
                stood+=y;
                else
                {
                    int cc=0;
                     while(stood<(i))
                     {
                                stood++;
                                cc++;
                     }
                    count+=cc;
                      stood+=y;
                    
                }
                
               
        }

        out<<count<<endl;
}
    
}
