#include<bits/stdc++.h>

using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output3.txt","w",stdout);

    int t;
    scanf("%d",&t);

    int z=1;

    while(t--)
    {
        char A[102];
        scanf(" %s",A);
        int B[102];
        int ans=0;
        int len=strlen(A);

        /*for(int i=0;i<len;i++)
        {
            if(i==0)
            {
                if(A[i]=='-')
                ans++;
            }
            else
            {
                if(A[i]!=A[i-1])
                    ans++;
            }

        }

        if(A[len-1]=='-')
            ans++;

        printf("Case #%d: %d\n",z++,ans);*/

        for(int i=0;i<len;i++)
        {
            if(A[i]=='-')
                B[i]=0;
            else
                B[i]=1;
        }

        int i=len-1;

        while(B[i]==1&&i>=0)
        {
            i--;
        }
        //printf("%d\n",i);
        int work[102];

        int end1=i;

        for(int j=0;j<=i;j++)
            work[j]=B[j];

        while(end1>=0)
        {
            if(work[0]==0)
            {
                int k=0;

                while(work[k]==0&&k<=end1)
                    k++;

                //printf("K=%d\n",k);
                for(int m=k;m<=end1;m++)
                {
                    work[m-k]=work[m];
                }

                end1=end1-k;
                ans++;
            }
            else
            {
                int k=0;
                while(work[k]==1&&k<=end1)
                {
                    work[k]=0;
                    k++;
                }
                ans++;
                //printf("Ans=%d\n",ans);
            }
        }

        printf("Case #%d: %d\n",z++,ans);

    }

}
