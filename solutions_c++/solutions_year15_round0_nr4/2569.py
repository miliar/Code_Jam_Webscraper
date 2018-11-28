#include<iostream>
#include<fstream>
#include<vector>
using namespace std;
int main()
{
    ifstream cinn("aa.in",ios::in);
    ofstream coutt("aa1.out",ios::out);
    int t,p=1,d=1;
    cinn>>t;
    while(t--)
    {

        int x,r,c,i,j,k=0;
        cinn>>x>>r>>c;
        if((r%x==0&&c>=x-1) || (c%x==0&&r>=x-1))
            coutt<<"Case #"<<d<<": GABRIEL"<<"\n";
        else
            coutt<<"Case #"<<d<<": RICHARD"<<"\n";
        d++;
    }
}
