#include<iostream>
using namespace std;
int main()
{
    long double c,a,b,l,f,n;
    long int t,k;
    cin>>t;
    for(k=0;k<t;k++)
{
    cin>>c>>f>>l;
b=l/2.0+1;
    a=l/2.0;
    n=0.0;
    while(b>a)
    {
        if(a>(a-(l/(2+(n*f)))+(c/(2+n*f))+l/(2+(n+1)*f)))
        {
b=a;
a=a-(l/(2+(n*f)))+(c/(2+n*f))+l/(2+(n+1)*f);
        }
        else
            break;
n++;
    }
    cout.precision(7);
    cout<<"Case #"<<k+1<<": "<<fixed<<a<<"\n";

}
}
