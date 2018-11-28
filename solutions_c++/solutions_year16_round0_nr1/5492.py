#include<bits/stdc++.h>
using namespace std;
int main(void)
{
    long long int t,n,a[10];
    //ifstream cin("A-large.in");
    //ofstream cout("output.txt");
    cin>>t;
    for(int i=0;i<t;i++)
    {
        cin>>n;
        for(int j=0;j<10;j++)
        {
            a[j]=0;
        }
        if(n==0)
        {
            cout<<"Case #"<<(i+1)<<": INSOMNIA"<<endl;
        }
        else
        {
            int k=1;
            long long int num=n;
            while(true)
            {
                int temp=0;
                while(num/10!=0)
                {
                    a[num%10]=1;
                    num=num/10;
                }
                a[num]=1;
                for(int j=0;j<10;j++)
                {
                    if(a[j]==0)
                    {
                        temp=1;
                        break;
                    }
                }
                if(temp==0)
                {
                    break;
                }
                else
                {
                    k++;
                    num=(k*n);
                }
                //printf("Num %d\n",num);
            }
            cout<<"Case #"<<i+1<<": "<<k*n<<endl;
        }
    }
    return 0;
}
