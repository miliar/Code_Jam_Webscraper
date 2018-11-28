#include<stdio.h>
#include<iostream>
#include<vector>
#include<cmath>
using namespace std;
double ni[100005],k[100005],knum;
int vn[10000],vk[10000];
main()
{
    int i,j,n,m,t,fans=0,flag=0,ans=0,count1=0;

    FILE *fin  = fopen ("input.in", "r");
    FILE *fout = fopen ("output.txt", "w");
    fscanf(fin,"%d",&t);
    //cin>>t;
    for(m=1;m<=t;m++)
    {
        fans=0;
        ans=0;
        flag=0;
        count1=0;

        fscanf(fin,"%d",&n);
        for(i=0;i<n;i++)
        vn[i]=vk[i]=0;
        //cin>>n;
        for(i=0;i<n;i++)
        fscanf(fin,"%lf",&ni[i]);

        for(i=0;i<n;i++)
        fscanf(fin,"%lf",&k[i]);

        sort(ni,ni+n);
        sort(k,k+n);
        while(count1!=n)
        {




        for(i=n-1;i>=0;)
        {
           // cout<<i<<endl;
            if(vn[i]==1)
            {
                i--;
                continue;
            }

            else
            count1++;

            flag=0;
            for(j=n-1;j>=0;j--)
            {
                if(vk[j]==1)
                continue;

                if(ni[i]<k[j])
                {
                    flag=1;
                    //printf("%d\n",j);
                    break;
                }
            }
            if(flag==0)
            {

                for(j=0;j<n;j++)
                {
                    if(vk[j]==0)
                    {
                        knum=k[j];
                        vk[j]=1;
                        break;
                    }
                }
                for(j=0;j<n;j++)
                {

                    if((ni[j]>knum)&&(vn[j]==0))
                    {

                        vn[j]=1;
                        fans++;
                        break;
                    }
                }

            }
            if(flag==1)
            {
                //printf("%lf\n",ni[i]);
                for(j=0;j<n;j++)
                {
                    if(vn[j]==0)
                    {
                        vn[j]=1;
                        break;
                    }
                }
                for(j=n-1;j>=0;j--)
                {
                    if(vk[j]==0)
                    {
                        vk[j]=1;

                        break;
                    }
                }

                //printf("%lf",ni[i]);

            }
            if(count1==n)
            break;

        }
        }


        for(i=0;i<n;i++)
        vn[i]=vk[i]=0;
        for(i=0;i<n;i++)
        {
            flag=0;
            for(j=0;j<n;j++)
            {
                if(vk[j]==1||vn[i]==1)
                continue;
                if(k[j]>ni[i])
                {
                    vn[i]=1;
                    vk[j]=1;
                    flag=1;
                    break;
                }
            }
            if(flag==0)
            ans++;
        }
        fprintf(fout,"Case #%d: %d %d\n",m,fans,ans);
    }
    return 0;
}

