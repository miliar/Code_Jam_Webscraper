#include<iostream>
#include<string>
#include<fstream>
#include<cmath>
using namespace std;

int main()
{
    fstream f1,f2;
    f1.open("input.in",ios::in);
    f2.open("output.txt",ios::out);
    int t,w=1;
    f1>>t;
    while(t--)
    {

        int i,j,temp;
        double c,f,x,k,l,m;
        f2.precision(7);
        f2.setf(ios::fixed,ios::floatfield);
        f1>>c>>f>>x;
        k=x*f-c*f-2*c;
        k/=(c*f);
        temp=ceil(k);
        if(temp<=0)
        {

            f2<<"Case #"<<w<<": "<<(x/2)<<"\n";
        }
        else
        {
            double ans=0;
            m=2;
            for(i=1;i<=temp;i++)
            {
                ans+=(c/m);
                m+=f;
            }
            ans+=(x/m);
            f2<<"Case #"<<w<<": "<<(ans)<<"\n";
        }

        w++;
    }
    return 0;
}
