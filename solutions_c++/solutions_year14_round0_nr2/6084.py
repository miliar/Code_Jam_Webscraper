#include <iostream>
#include <cstdio>
using namespace std;
int main ()
{
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    double c,f,x,t1,t2,p1;
    cin>>t;
    for (int i=0; i<t; i++)
    {
          cin>>c>>f>>x;
          p1=2.0;
          t2=0;
          do
          {
          t1=t2+x/p1;
          t2+=c/p1;
          p1+=f;
          }
          while (t1>t2+x/p1);
          cout<<"Case #"<<i+1<<": ";
          printf("%.7f\n", t1);
          }
    fclose(stdin);
    fclose(stdout);
    }
