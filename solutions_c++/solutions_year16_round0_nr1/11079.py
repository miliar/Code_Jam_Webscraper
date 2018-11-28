#include<iostream>
using namespace std;
int main()
{
    int t,i,j,n,num[10],p,q,r,s;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        cin>>n;
        if(n==0)
        {
            cout<<"Case #"<<i<<": INSOMNIA"<<endl;
        }
        else
        {
            for(j=0;j<=9;j++)
            {
                num[j]=0;
            }
            p=n;
            while(1)
            {
                q=p;
                while(q!=0)
                {
                    r=q%10;
                    switch (r)
                    {
                        case 0: num[0]=1;
                                break;
                        case 1: num[1]=1;
                                break;
                        case 2: num[2]=1;
                                break;
                        case 3: num[3]=1;
                                break;
                        case 4: num[4]=1;
                                break;
                        case 5: num[5]=1;
                                break;
                        case 6: num[6]=1;
                                break;
                        case 7: num[7]=1;
                                break;
                        case 8: num[8]=1;
                                break;
                        case 9: num[9]=1;
                                break;
                    }
                    q=q/10;
                }
                s=0;
                for(j=0;j<=9;j++)
                {
                    s=s+num[j];
                }
                if(s==10)
                    break;
                else
                    p=p+n;
            }
            cout<<"Case #"<<i<<": "<<p<<endl;
        }
    }
    return 0;
}
