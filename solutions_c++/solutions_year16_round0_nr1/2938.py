#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    int t,p,count=1;
    long long int n,i,j,k;
    //ofstream out;
    //out.open("cntsheep2.out");
    cin>>t;
    while(t--)
    {
        cin>>n;
        bool b[10]={0};
        p=0;i=1;
        cout<<"Case #"<<count<<": ";
        count++;
        if(n==0)
        {
            cout<<"INSOMNIA\n";
            continue;
        }
        while(p!=10)
        {
            j=n*i;
            i++;
            while(j>0)
            {
                if(b[j%10]==0)
                {
                    b[j%10]=1;
                    p++;
                }
                j/=10;
            }
        }
        cout<<n*(i-1)<<endl;
    }
    return 0;
}
