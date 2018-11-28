#include<bits/stdc++.h>
using namespace std;
int arr[11]={0};
bool chk()
{
    int ck=2,i,j;
    for(i=0;i<10;i++)
    {
        if(arr[i]==0)
            return false;
    }
    return true;
}
void putty(long long int n)
{
    int i,j,k;
    while(n)
    {
        i=n%10;
        n/=10;
        arr[i]=1;
    }

}
int main()
{
    long long int n,i,j,k,l,a,b;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    cin>>n;
    for(i=1;i<=n;i++)
    {
        cin>>a;
        memset(arr,0,sizeof(arr));
        printf("Case #%d: ",i);
        int ck=2;
        for(j=1;j<1000;j++)
        {
            putty(j*a);
            if(chk()==true)
            {
                cout<<j*a<<endl;
                ck=3;
                break;
            }
        }
        if(ck==2)
            cout<<"INSOMNIA"<<endl;
    }
}
