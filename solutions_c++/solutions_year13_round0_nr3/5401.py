#include<iostream>
#include<math.h>
using namespace std;
bool isPalin(int a)
{
    int A[10000];
    int i=0;
    while(a>0)
    {
        A[i]=a%10;
        a/=10;
        i++;
    }
    for(int j=0;j<i/2;j++)
    {
        if(A[j]!=A[i-j-1])
        {
            return false;
        }
    }
    return true;
}
int main()
{
    int t;
    cin>>t;
    int cas=1;
    while(t--)
    {
        int a,b;
        cin>>a>>b;
        int n1=(int)(ceil(sqrt(a)));
        int n2=(int)(floor(sqrt(b)));
        int cnt=0;
        for(int i=n1;i<=n2;i++)
        {
            int s=i*i;
            if(isPalin(i) && isPalin(s))
            {
                cnt++;
            }
        }
        cout<<"Case #"<<cas<<": "<<cnt<<endl;
        cas++;
    }
}
