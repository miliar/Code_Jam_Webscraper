#include<iostream>
#include<cstdlib>

using namespace std;

int main()
{
    long long int t,n,i,j,k,name,st;
    long long int a[10];
    long long int p;

    cin>>t;

    for(i=1;i<=t;i++)
    {
        cin>>n;
        cout<<"Case #"<<i<<": ";
        if(n==0)
            cout<<"INSOMNIA\n";
        else{
            j=1;
            for(k=0;k<10;k++)
                a[k]=0;
            do{
                st=name=n*j;
                while(name>0)
                {
                    a[name%10]++;
                    name/=10;
                }

                j++;
                p=1;
                for(k=0;k<10;k++)
                    p*=a[k];
            }while(p==0);
            cout<<st<<endl;
        }
    }
    return 0;
}
