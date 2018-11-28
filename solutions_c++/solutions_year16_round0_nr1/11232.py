#include<iostream>
#include<stdio.h>

using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    unsigned long long i,t,cas=0,n,temp;

    cin>>t;
    while(t--)
    {
        int flag=0;
        int a[12]= {0,0,0,0,0,0,0,0,0,0,0,0};
        cin>>n;
        if(n==0)
        {
            cout<<"Case #"<<++cas<<": "<<"INSOMNIA"<<endl;
            //cout<<"INSOMNIA"<<endl;
            continue;
        }
        //flag=1;

        i=1;

        while(true)
        {
            temp=n*i;
            flag=0;
            while(temp>0)
            {
                a[temp%10]++;
                temp/=10;
            }

            for(int j=0; j<10; j++)
            {
                if(a[j]==0)
                {
                    flag=1;
                }
            }
            if(flag)
            {
                i++;
                continue;
            }
            else{
            cout<<"Case #"<<++cas<<": "<<n*i<<endl;
            break;
            }

        }


        //cout<< ++cas<<endl;
    }
fclose(stdin);
fclose(stdout);
}
