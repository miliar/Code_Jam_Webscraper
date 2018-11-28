#include <iostream>
using namespace std;
int main() {
    
    int i,a[10],t,o;
    int sum,temp,init;
    int n,l,k;

    cin>>t;
    for(o=0;o<t;o++)
        {
        cin>>n;
        for(i=0;i<10;i++)
        a[i]=0;
        sum=0;
        k=1;
        init=n;
if(n!=0)
{
        while (true)
            {
            temp=n;

        while(n>0)
            {
            l=n%10;
            if(a[l]==0)
            {
                a[l]=1;
                sum++;
            }
            n=n/10;
            
        }
            n=init*(++k);
if(sum==10)break;
        }
        cout<<"Case #"<<(o+1)<<": "<<temp<<endl;
}
else cout<<"Case #"<<(o+1)<<": INSOMNIA"<<endl;
}
    return 0;
}
