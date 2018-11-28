#include <iostream>
using namespace std;

int check(int a[10])
{
    int i;
    for(i=0;i<10;i++)if(a[i]==0)return 1;
    return 0;
}

int add(long long s,int a[10])
{
    while(s!=0)a[s%10]=1,s/=10;
    return 0;
}

int main()
{
    int tc,tci=0;
    cin>>tc;
    while(tc--)
    {
        tci++;
        long long n;
        cin>>n;
        long long s=n;
        if(n==0){cout<<"Case #"<<tci<<": INSOMNIA"<<endl;continue;}
        int a[10]={0};
        do
        {
            add(s,a);
            s+=n;
        }while(check(a));
        cout<<"Case #"<<tci<<": "<<s-n<<endl;
    }
    return 0;
}
