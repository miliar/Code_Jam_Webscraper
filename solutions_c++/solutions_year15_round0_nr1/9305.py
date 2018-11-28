#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;

int main()
{
    //cout << "Hello world!" << endl;

    long long int t,k=1;
    freopen("input.txt","r+",stdin);
    freopen("output.txt","w+",stdout);
    cin>>t;
    while(t--)
    {
       long long int n,count=0,sum=0;
       string nit;
       cin>>n>>nit;
       sum=nit[0]-48;
       for(long long int i=1;i<nit.length();i++)
       {
           if(i>sum)
           {
              count+=i-sum;
              sum+=i-sum;
           }
           sum+=nit[i]-48;
       }
       cout<<"Case #"<<k<<": "<<count<<endl;
       k++;
    }
    return 0;
}
