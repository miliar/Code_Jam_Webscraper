#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
    int n,i,j,p;
    double c,f,x,t1,t2,k;

    cin>>n;
    for(i=0; i<n; i++)
    {
        cin>>c>>f>>x;

        k=2+f;
        t1=x/2;
        t2=c/2+x/k;

        while(t1>t2)
        {
            t1=t2;
            k=k+f;
            t2=t2-x/(k-f)+c/(k-f)+x/k;
        }
        cout<<"Case #"<<i+1<<": ";
        printf("%.7f",t1);

        if(i<n-1) cout<<endl;
    }
    return 0;
}
