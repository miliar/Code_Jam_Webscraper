#include "iostream"
#include "cstdio"
#include "set"
#include "cmath"
using namespace std;

int t;
double C,F,X;

double getans(int n)
{
    double ret=0;
    for(int i=0;i<n;i++)
        ret+=C/(2+i*F);
    return ret+X/(2+n*F);
}
int main()
{
    //freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    cin>>t;
    for(int  cas=1; cas<=t; cas++)
    {
        cout<<"Case #"<<cas<<": ";
        cin>>C>>F>>X;
        int n=max(0,(int)(X/C-2/F));
        printf("%.7lf\n",getans(n));
    }
    return 0;
}
