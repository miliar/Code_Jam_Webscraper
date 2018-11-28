#include<bits/stdc++.h>
using namespace std;
int main()
{
ifstream cin("in.txt");
ofstream cout("b.txt");
    long long int i,n,x,t,an=0;
    cin>>t;
    while(t--)
    {
        long long int a[10]={0},c=0;
        long long int x;
        cin>>x;
        if(x==0) cout<<"Case #"<<++an<<": "<<"INSOMNIA"<<endl;
        else for(i=1;;i++)
        {
            n=x*i;
            while(n)
            {
                if(a[n%10]==0)
                {
                    a[n%10]=1;
                    c+=1;
                }
                n/=10;
            }
            if(c==10)
            {
                cout<<"Case #"<<++an<<":"<<" "<<x*i<<endl;
                break;
            }

        }
    }
    return 0;
}
