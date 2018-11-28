#include<iostream>
#include<string.h>
using namespace std;
#define ull long long int
int arr[11];
void func(ull n)
{
    ull k;
    while(n>0)
    {
        k=n%10;
        n/=10;
        arr[k]=1;
    }
    return;
}
int main()
{
    ios::sync_with_stdio(false);
    ull t,n,i,j,k,flag;
    cin>>t;
    for(j=1;j<=t;j++)
    {
        cin>>n;
        i=0;
        memset(arr,0,sizeof(arr));
        if(n!=0)
        while(1){
            func((i+1)*n);
            flag=0;
            for(k=0;k<10;k++){
                if(!arr[k]){
                    flag=1;
                    continue;
                }
            }
            if(!flag)
                break;
            i++;
        }
        if(n==0)
            cout<<"Case #"<<j<<": INSOMNIA"<<"\n";
        else
            cout<<"Case #"<<j<<": "<<(i+1)*n<<"\n";
    }
    return 0;
}
