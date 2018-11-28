#include<iostream>
using namespace std;
void finddigits(int x[10], int n)
{
    while(n)
    {
        x[n%10]=1;
        n=n/10;
    }
}
int main()
{
    int t,s,i,j,k;
    long long n;
    int x[10];
    cin>>t;
    for(i=1;i<=t;i++)
    {
        cin>>n;
        if(n==0)
        {
            cout<<"Case #"<<i<<": INSOMNIA"<<"\n";
        }
        else
        {
            j=1;
            while(1)
            {
        
                finddigits(x,n*j);
                s=0;
                for(k=0;k<=9;k++)
                {
                    if(x[k]==1)
                        s++;
                }
                
                if(s==10)
                {
                    cout<<"Case #"<<i<<": "<<n*j<<"\n";
                    for(k=0;k<=10;k++)
                        x[k]=0;
                    break;
                }
                j++;
            }

        }
        }
}
