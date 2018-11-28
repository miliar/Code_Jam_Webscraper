#include<stdio.h>
#include<iostream>
using namespace std;
int main()
{
    int t,r=0;
    scanf("%d",&t);
    int n[t];
    while(t)
    {
        int p,q,a[4][4],b[4][4],c[4],d[4],j=0,f=0,s=0,z;
        scanf("%d",&p);
        for(int i=0;i<4;i++)
            {
                for(int k=0;k<4;k++)
                {
                    scanf("%d",&a[i][k]);
                    if(i==(p-1))
                    {
                        c[j]=a[i][k];
                        j++;
                    }
                }
            }


        scanf("%d",&q);
        for(int i=0;i<4;i++)
            {
                for(int k=0;k<4;k++)
                {
                    scanf("%d",&b[i][k]);
                    if(i==(q-1))
                    {
                        d[f]=b[i][k];
                        f++;
                    }
                }
            }

     //   cout<<c[0]<<" "<<c[1]<<" "<<c[2]<<" "<<c[3]<<endl;
     //   cout<<d[0]<<" "<<d[1]<<" "<<d[2]<<" "<<d[3]<<endl;
        for(int i=0;i<4;i++)
        {
            for(int k=0;k<4;k++)
            {
                if(c[i]==d[k])
                {
                        s++;
                        z=i;
                }

            }
        }
     //   cout<<s<<endl;
        if(s==1)
        {
            if(c[z]==1)
            {
                n[r]=17;
                r++;
            }
            else
            {
                n[r]=c[z];
                r++;
            }
        }
        if(s>1)
        {
            n[r]=1;
            r++;
        }
        if(s==0)
        {
                n[r]=0;
                r++;
        }
        t--;
    }
    for(int i=0;i<r;i++)
    {
        if(n[i]==1)
            cout<<"Case #"<<(i+1)<<": "<<"Bad magician!"<<endl;
        if(n[i]==0)
            cout<<"Case #"<<(i+1)<<": "<<"Volunteer cheated!"<<endl;
        if(n[i]==17)
            cout<<"Case #"<<(i+1)<<": "<<(n[i]-16)<<endl;
        if((n[i]>1)&&(n[i]<=16))
            cout<<"Case #"<<(i+1)<<": "<<n[i]<<endl;
    }
    return 0;
}
