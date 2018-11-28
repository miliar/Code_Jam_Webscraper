#include<bits/stdc++.h>
using namespace std;
int main()
{
    #ifndef ONLINE_JUDGE
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    #endif
    long long t,n,d,n1,n2,a[10],flag,count=0,x;

    cin>>t;
    do
    {
        for(int j=0;j<10;j++)
        {
            a[j]=0;
        }
        flag=1;
        count++;
        cin>>n;
        n1=n2=n;
        x=1;
        if(n==0)
            {
                cout<<"Case #"<<count<<": INSOMNIA\n";
            }
        else
            {
                while(1)
                {

                    n1=n2;
                    flag=1;
                    x++;
                   while(n1>0)
                   {
                       d = n1%10;
                       switch(d)
                       {
                            case 0: a[0]=1;
                                    break;
                            case 1: a[1]=1;
                                    break;
                            case 2:  a[2]=1;
                                    break;
                            case 3:  a[3]=1;
                                    break;
                            case 4:  a[4]=1;
                                    break;
                            case 5:  a[5]=1;
                                    break;
                            case 6:  a[6]=1;
                                    break;
                            case 7:  a[7]=1;
                                    break;
                            case 8:  a[8]=1;
                                    break;
                            case 9:  a[9]=1;
                                    break;
                       }

                       n1= n1/10;
                   }
                   for(int i=0;i<10;i++)
                   {
                       if(a[i]==0)
                        flag = 0;
                   }
                   if(flag==1)
                    {
                        cout<<"Case #"<<count<<": "<<n2<<"\n";
                        break;
                    }
                    n2=x*n;
                }
            }
        t--;
    }while (t>0);
}
