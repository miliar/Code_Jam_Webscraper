#include<stdio.h>
#include<math.h>
#include<string.h>
#include<iostream>
#include<algorithm>
#include<stack>
#include<map>
#include<set>
#include<queue>
#include<vector>
#define pi (2*acos(0))
#define SF scanf
#define SFd1(a) scanf("%d",&a)
#define SFd2(a,b) scanf("%d%d",&a,&b)
#define SFd3(a,b,c) scanf("%d%d%d",&a,&b,&c)
#define PF printf
#define inf 99999999
#define eps 0.00000001
#define ll long long
#define ull long long unsigned
#define fr(i,n) for(i=0;i<n;i++)
#define dist(x1,y1,x2,y2) sqrt( ((x2-x1)*(x2-x1)) + ((y2-y1)*(y2-y1)) )
using namespace std;
//int rr[]={1,2,-1,-2,1,2,-1,-2};
//int cc[]={2,1,2,1,-2,-1,-2,-1};

int flag[110][110][110],n,p,cum[110][110];
char arr[110][110][110],ck[110][110][110];

int is_possible(void)
{
    for(int i=1;i<=n;i++)
    {
        int l=strlen(arr[p][i]);
        ck[p][i][0]=arr[p][i][0];
        int k=1;
        for(int j=1;j<l;j++)
        {
            if(arr[p][i][j]!=arr[p][i][j-1])
                ck[p][i][k++]=arr[p][i][j];
        }
    }
    for(int i=2;i<=n;i++)
    {
        if(strcmp(ck[p][i],ck[p][i-1])!=0)
            return false;
    }
    return true;
}

main()
{
    int i,j,res,t,l,k;
    FILE *read,*write;
    read=fopen("the_repeater_in.txt","r");
    write=fopen("the_repeater_out.txt","w");
    fscanf(read," %d",&t);
    for(p=1; p<=t; p++)
    {
        //memset(flag,0,sizeof(flag));
        //memset(cum,0,sizeof(cum));
        fscanf(read," %d",&n);
        for(i=1; i<=n; i++)
        {
            fscanf(read," %s",&arr[p][i]);
            l=strlen(arr[p][i]);
            arr[p][i][l]='#';
            k=0;
            for(j=0; j<l; j++)
            {
                if(arr[p][i][j]==arr[p][i][j+1])
                    flag[p][i][k]++,cum[p][k]++;
                else
                    k++;
                //flag[i][arr[i][j]-'a']++;
                //cum[arr[i][j]-'a']++;
            }
        }
        if(is_possible())
        {
            res=0;
            for(i=0; i<k; i++)
            {
                int r1=0,r2=0;
                int a1=cum[p][i]/n;
                int a2=a1+1;
                for(j=1;j<=n;j++)
                    r1+=abs(flag[p][j][i]-a1);
                for(j=1;j<=n;j++)
                    r2+=abs(flag[p][j][i]-a2);
                res+=min(r1,r2);
            }
            fprintf(write,"Case #%d: %d\n",p,res);
        }
        else
            fprintf(write,"Case #%d: Fegla Won\n",p);

    }
    fclose(read);
    fclose(write);
    return 0;
}

