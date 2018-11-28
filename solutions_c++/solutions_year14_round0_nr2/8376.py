#include<iostream>
#include<fstream>
#include<cstdio>
#include<iomanip>
using namespace std;
int main()
{
    long long int t;
    long double tb, c, f, x, i, ch=0;
    long double a1=0, a2=0, tp=0;
    cin>>t;
    freopen("output21.txt","w",stdout);
    for (i=1; i<=t; i++)
    {
        cin>>c>>f>>x;
        tb=2;
        if (x>=c)
        {
            while (ch!=1)
            {
                  tp=tp+(c/tb);
                  a1=x/(tb+f);
                  a2=(x-c)/tb;
                  if (a1<a2)
                  {
                      tb=tb+f;
                  }
                  else
                  {
                      tp=tp+(x-c)/tb;
                      ch=1;
                  }
            }
        }
        else 
        tp=x/tb;
        
        cout<<"Case #"<<i<<": "<<setprecision(7)<<tp<<'\n';
        a1=0; a2=0; tp=0; ch=0;
    }
    system("pause");
              
    return 0;
}
