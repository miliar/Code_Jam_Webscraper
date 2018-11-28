#include<iostream>
#include<cstdlib>
#include<cmath>

using namespace std;

bool prime(unsigned long long n){
    unsigned long long i;

    if (n==2)
        return true;

    if (n%2==0)
        return false;

    for (i=3;i<=sqrt(n);i+=2)
        if (n%i==0)
            return false;

    return true;
}

unsigned long long baseConvert(unsigned long long n,unsigned long long a[],unsigned long long i)
{
    unsigned long long j,k,res=0;
    for(j=1,k=0;k<n;k++,j*=i)
        res+=(a[n-k-1]*j);
    return res;
}

bool baseCheck(unsigned long long n,unsigned long long a[])
{
    unsigned long long i;
    for(i=2;i<=10;i++)
    {

        if(prime(baseConvert(n,a,i)))
            return false;
    }
    return true;
}

int main()
{
    unsigned long long t,n,j,s,k,l,i,m,st,cnt;
    cin>>t;
     unsigned long long a[32]={0};

    cout<<"Case #1:"<<endl;
    while(t--)
    {

        cin>>n>>j;
        cnt=0;
        a[0]=a[n-1]=1;
        s=n-2;

        for(k=0;k<(1<<s) && cnt<j;k++)
        {
                for(l=0;l<s;l++){
                    if(k & (1<<l))
                        a[l+1]=1;
                }

                if(baseCheck(n,a))
                {
                    cnt++;
                    for(i=0;i<n;i++)
                        cout<<a[i];
                    cout<<" ";
                    for(i=2;i<=10;i++)
                    {
                        st=baseConvert(n,a,i);

                        for(m=2;m<=st/2;m++)
                        {
                            if(st%m==0){
                                cout<<m<<" ";
                                break;
                            }
                        }

                    }
                    cout<<endl;
                }
                for(l=0;l<s;l++){
                    if(k & (1<<l))
                        a[l+1]=0;
                }
        }

        a[0]=a[n-1]=0;
    }
    return 0;
}
