#include <stdio.h>

using namespace std;

int main()
{
    FILE* in=fopen("input.txt","r");
    FILE* out=fopen("output.txt","w");

    int n, i, cnt=0,j,sum,k, cnt1=0,temp;
    int arr[101], ck[11];

    fscanf(in,"%d",&n);

    for(i=0;i<10;i++)
    {
        ck[i]=11;
    }
    for(i=0;i<n;i++)
    {
        fscanf(in,"%d",&arr[i]);
    }
    for(i=0;i<n;i++)
    {
        if(arr[i]!=0)
        {
            for(j=1;;j++)
            {

                sum=arr[i]*j;
                temp=sum;
                for(;;)
                {
                    if(cnt>=10) break;
                    if(sum<=0) break;
                    for(k=0;k<10;k++)
                    {
                        if(ck[k]==sum%10) cnt1++;
                    }
                    if(cnt1==0)
                    {
                        ck[cnt]=sum%10;
                        cnt++;
                    }
                    cnt1=0;
                    sum=sum/10;
                }

                if(cnt>=10)
                    {
                        fprintf(out,"Case #%d: %d\n",i+1,temp);
                        break;
                    }

            }
            cnt=0;
            for(j=0;j<11;j++)
            {
                ck[j]=11;
            }
        }
        else fprintf(out,"Case #%d: INSOMNIA\n",i+1);

    }

    return 0;
}
