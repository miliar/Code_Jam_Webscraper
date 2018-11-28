#include<iostream>
#include<fstream>
using namespace std;
int a[10]={0};
int isfreq()
{
    int flag=1;
    for(int i=0;i<=9;i++)
    {
        if(a[i]==0)
            flag=0;
    }
    if(flag==1)
        return 1;
    else
        return 0;
}
int isDig(int x)
{
    while(x>0)
    {
        int d=x%10;
        a[d]++;
        x=x/10;
    }
    int result=isfreq();
    if(result==1)
        return 1;
    else
        return 0;
}

int main()
{
    freopen("d:/work/large.in","r",stdin);
    freopen("d:/work/output3.out","w",stdout);
    int t;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        int flag=0;
        long n;
        cin>>n;
        long long int sum=n;
       /* if(n==0)
            cout << "Case #" << i << ": INSOMNIA" << endl;*/
       for(int j=2;j<10000;j++)
       {
            int res=isDig(sum);
            if(res==1)
            {
                cout << "Case #" << i << ": " << sum << endl;
                flag=1;
                for(int k=0;k<=9;k++)
                    a[k]=0;
                break;
            }
            sum=n*j;
       }
        if(flag==0)
             cout << "Case #" << i << ": INSOMNIA" << endl;
    }
    return 0;

}
