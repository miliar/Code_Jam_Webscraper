#include<iostream>
#include<vector>
#include<string>
#include<set>
#include<map>
#include<queue>
#include<fstream>
using namespace std;
int main()
{
ifstream fin("A-small-attempt4.in");
ofstream fout("output.txt");
long long t,r,p,i,req,count,c=0,start,last;
fin>>t;
while(t--)
{
    count=0;

    fin>>r>>p;


    start=r;

    while(1)
    {
    //    cout<<"hello"<<endl;



        req=1+2*start;
        if(req<=p)
        {
         p=p-req;
         count++;
         start=start+2;
        }
        else
        break;


    }


    c++;
    fout<<"Case #"<<c<<": "<<count<<endl;
}
return 0;
}
