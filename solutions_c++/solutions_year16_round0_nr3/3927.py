#include<iostream>
#include<cmath>
using namespace std;
int checkprime(unsigned long long x)
{
     if (x ==2 ) return 1;
        for(unsigned long long i =2; i * i <= x; i++ )
            if (x %i == 0) {
                return 0;
            }
            return 1;
}

void printmul(unsigned long long x)
{
        for(unsigned long long i =2; i * i <= x; i++ )
            if (x %i == 0) {
                cout<<i<<" ";
                return;
            }
       cout<<x/2<<" ";
       return;
}

void printbin(unsigned long long n,int x)
{
    cout<<"1";
    int cnt[32]={0},i=0;
    while(n>0)
    {
        cnt[i++]=n%2;
        n=n/2;
    }
    for(int j=x-3;j>=i;j--) cout<<"0";
    for(int j=i-1;j>=0;j--)cout<<cnt[j];
    cout<<"1 ";
}
void printmul(unsigned long long val[]);
main()
{
    int t;
    cin>>t;
    unsigned long long n,jr;
    cin>>n>>jr;
    cout<<"Case #"<<1<<": "<<endl;
    for(unsigned long long i=0;i<(1<<(n-2));i++)
    {
       // cout<<"y"<<endl;
        unsigned long long x=i,val[11]={0},ctr=1,flag=0;
        for(int j=2;j<=10;j++)
        {
            val[j]+=1;
            val[j]+=(unsigned long long) pow(j,n-1);
           // cout<<j<<" "<<val[j]<<endl;
        }
        while(x>0)
        {
         if(x%2==1)
         for(int j=2;j<=10;j++)
         {
              val[j]+= (unsigned long long) pow(j,ctr);
         }
         x=x/2;
         ctr++;
        }
        for(int j=2;j<=10;j++)
        {
           // if(!checkprime(val[j]))
           // cout<<i<<" "<<j<<" "<<val[j]<<checkprime(val[j])<<endl;
            if(checkprime(val[j]))  {flag=1; break;}
        }
        if(flag==0&&jr>=1)
        {
         //  cout<<i<<endl;
           printbin(i,n);
           for(int j=2;j<=10;j++) printmul(val[j]);
           cout<<"\n";
           jr--;
        }
        if(jr==0) break;
    }
    return 0;
}
