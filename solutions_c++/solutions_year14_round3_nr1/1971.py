#include<iostream>
#include<fstream>

using namespace std;

int main()
{
    fstream f;
    f.open("A-small-attempt3.in",ios::in|ios::out);
    int P,Q;
    char c;
	int T;
	f>>T;
	for(int i=0;i<T;i++)
    {
        f>>P>>c>>Q;
       // cout<<P<<c<<Q;
       int t=2;
       while(Q>t)
       {
           t=t*2;
       }
        if(Q%2==0 && Q==t)
        {

            float r;
            r=P;
            r=r/Q;
            int ct=0;
            float temp=1;
            while(r < temp)
            {
                ct++;
                temp=temp/2;
               // cout<<"temp="<<temp<<"r="<<r<<endl;

            }
            cout<<"Case #"<<i+1<<": "<<ct<<endl;
        }
        else
            cout<<"Case #"<<i+1<<": impossible\n";
    }
}
