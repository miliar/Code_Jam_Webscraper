#include<iostream>
using namespace std;

int main()
{
    int t,t1=1;
    long int n,n1;
    int flag[10],flag1,j,i;

    cin>>t;
    while(t--)
    {
        cin>>n;

        if(n==0)    cout<<"Case #"<<t1<<": INSOMNIA\n";
        else
        {
            for(i=0;i<10;i++) flag[i]=0;

            flag1=0;
            n1=n;
            j=2;

            while(flag1!=1)
            {
                flag1=1;
                while(n1!=0)
                {
                    flag[(int)(n1%10)]=1;
                    n1=n1/10;
                }
                for(i=0;i<10;i++)
                {
                    if(flag[i]==0) flag1=0;
                }

                if(flag1==1) n1=n*(j-1);
                else n1=n*j;
                j++;
            }
            cout<<"Case #"<<t1<<": "<< n1<<endl;
        }
        t1++;
    }

}
