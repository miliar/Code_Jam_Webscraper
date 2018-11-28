#include<iostream>
using namespace std;
int main()
{
    int t,a,b,l,i,j,k,c;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        cin>>a>>b>>k;
        c=0;
        for(j=0;j<a;j++)
        {
            for(l=0;l<b;l++)
            {
                if((j&l)<k)
                    c++;
            }
        }
        cout<<"Case #"<<i<<": "<<c<<endl;
    }
}
