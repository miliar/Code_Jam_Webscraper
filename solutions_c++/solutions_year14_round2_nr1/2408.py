#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("input.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t,ii;
    scanf("%d",&t);
    for(ii=1;ii<=t;ii++)
    {
        int n,i,j,k;
        scanf("%d",&n);
        char a[n][101];
        for(i=0;i<n;i++)
            scanf("%s",a[i]);
        int sum=0,aa[100],coun[100],lala[100];
        for(i=0;i<100;i++)
            {aa[i]=0;coun[i]=0;}
        for(i=0;i<n;i++)
        {
            for(j=0;a[i][j]!='\0';j++);
            lala[i]=j;
        }
        char x;
        int ll,flag2=0,ans=0;
        for(j=0;flag2==0&&a[0][j]!='\0';)
        {
            x=a[0][j];
            sum=0;
            int flag=0;
            while(a[0][j]==x)
            {
                sum++;
                j++;
                aa[0]++;
                coun[0]++;
            }
            //cout<<aa[0]<<x<<"asdf\t\n";
            for(i=1;i<n;i++)
            {
                //cout<<aa[i]<<i<<"\t";
                while(a[i][aa[i]]!='\0'&&a[i][aa[i]]==x)
                {
                    aa[i]++;
                    coun[i]++;
                    sum++;
                    flag=1;
                }
                if(flag==0)
                {
                    printf("Case #%d: Fegla Won\n",ii);
                    flag2=1;
                    break;
                }
                flag=0;

            }
            sum/=n;
            for(i=0;i<n;i++)
            {
                ans+=abs(coun[i]-sum);
                coun[i]=0;
            }
        }
        int flag=0;
        for(i=0;i<n;i++)
        {
            if(aa[i]!=lala[i])
            {flag=1;break;}
        }
        if(flag2==0&&flag==0)
            printf("Case #%d: %d\n",ii,ans);
        else if(flag2==0&&flag==1)
            printf("Case #%d: Fegla Won\n",ii);
    }
    return 0;
}
