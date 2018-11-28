#include<cstdio>
#include<cstdlib>
#include<iostream>
using namespace std;

int main()
{
    freopen("B-large(1).in", "rt", stdin);
    freopen("B-large3.out", "wt", stdout);
    double c,farm,x,mini,temp,dir,f,sum,arr[100000];
    int t,cnt,i,k;
    cin>>t;
    for(k=1;k<=t;k++)
    {
        cin>>farm>>f>>x;
        c=2;
        cnt=0;
        while(1)
        {
            temp=x/c;
            dir=(farm/c)+(x/(c+f));
            if(temp>dir)
            {
                arr[cnt++]=farm/c;
                c+=f;
                continue;
            }
            else
            {
                sum=0;
                arr[cnt++]=x/c;
                for(i=0;i<cnt;i++)
                {
                    sum+=arr[i];
                }
                break;
            }
        }
        printf("Case #%d: %.7lf\n",k,sum);
    }
    return 0;
}

