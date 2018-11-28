#include<iostream>
#include<cstdio>
using namespace std;

int main()
{
    FILE *f;
    long int i,j,a[20],b[20],n,m,t,c,d,k,s,num;
    f=fopen("output","w");
    cin>>t;
    for(k=1;k<=t;k++)
    {
        cin>>n;
        for(i=1;i<=16;i++)
        {
            cin>>a[i];
        }
        cin>>m;
        for(i=1;i<=16;i++)
        {
            cin>>b[i];
        }
        s=0;
        c=(4*(n-1))+1;
        d=(4*(m-1))+1;
        for(i=c;i<=c+3;i++)
        {
            for(j=d;j<=d+3;j++)
            {
                if(a[i]==b[j])
                {
                    s++;
                    num=a[i];
                }
            }
        }
        if(s>1)  fprintf(f,"Case #%ld: Bad magician!\n",k);
        else if(s==0) fprintf(f,"Case #%ld: Volunteer cheated!\n",k);
        else fprintf(f,"Case #%ld: %ld\n",k,num);
    }
    fclose(f);
    return 0;
}
