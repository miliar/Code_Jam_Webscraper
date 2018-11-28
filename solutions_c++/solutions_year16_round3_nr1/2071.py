#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    freopen("inputA.txt", "r", stdin);
    freopen("outputA.txt", "w", stdout);
    int n,i,t,P[37],j,sum=0,cur,x,y,max,index,flag;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        printf("Case #%d: ",i);
        cin>>n;sum=0;
        for(j=1;j<=n;j++){cin>>P[j];sum+=P[j];}
        cur=sum;
        while(cur>0)
        {
            max=0;x=0;y=0;index=0;flag=0;
            for(j=1;j<=n;j++)
            {
                if(P[j]>max)
                    {
                        max=P[j];
                        index=j;
                    }
            }
            printf("%c",index+'A'-1);P[index]--;
            max=0;cur--;
            if(cur>0)
            {
                for(j=1;j<=n;j++)
                {
                 if(P[j]>max)
                    {
                        max=P[j];
                        index=j;
                    }
                }
                for(j=1;j<=n;j++)
                {
                    if(j!=index)
                    {
                        if(P[j]>(cur-1)/2)
                        {
                            printf(" ");
                            flag=1;break;
                        }
                    }
                }
                if(flag!=1)
                {printf("%c ",index+'A'-1);P[index]--;cur--;}
            }
        }
        printf("\n");
    }
}
