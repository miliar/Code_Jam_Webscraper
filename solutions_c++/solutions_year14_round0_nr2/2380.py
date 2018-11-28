#include<iostream>
#include<iomanip>
#include<stdio.h>
#include<cstring>
using namespace std;
int main(void)
{
    int n, cn=1;
    freopen("output.txt","w",stdout);
    freopen("B-large.in","r",stdin);
    cin>>n;
    while(cn<=n)
    {
        double c, f, x, k=2, w, y, s=0;
        cin>>c>>f>>x;
        cout<<"Case #"<<cn<<": ";
        do
        {
              w=x/k;
              y=c/k + x/(k+f);
              if(w<y)
              {
                  s+=w;
                  cout<<fixed;
                  cout<<setprecision(7)<<s<<endl;
                  break;
              }
              else
              {
                  s+=c/k;
                  //cout<<(c/k)<<" "<<s;
                  k+=f;
              }
        }while(true);
        cn++;
    }
    fclose(stdout);
    fclose(stdin);
}
