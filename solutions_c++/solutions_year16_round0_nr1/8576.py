#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("jam.out","w",stdout);
    long long int t,n,n1,var=1;
    cin>>t;
    set< int > sheep;
    for(int j=1;j<=t;j++)
    {
        cin>>n;
        n1=n;//temp value
        if(n1==0)
           {
               cout<<"Case #"<<j<<": "<<"INSOMNIA"<<"\n";
           }
        else
        {
        while(sheep.size()!= 10)
        {
           n=n1*var;
           while(n>0)
           {
               sheep.insert(n%10);
               n=n/10;
           }
           var++;
        }
        cout<<"Case #"<<j<<": "<<(n1*(var-1))<<"\n";
        var=1;
        sheep.clear();
        }
    }

    return 0;
}
