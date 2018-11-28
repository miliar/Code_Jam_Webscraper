#include<stdio.h>
#include<iostream>

#define MAXL 1000

using namespace std;

int main()
{
    int tcase,test;
    int smax;
    char shy[MAXL+2];
    int arr[MAXL+1];
    int answer=0;
    int sum;
    int i;

    freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

    scanf("%d",&test);

    for(tcase=1;tcase<=test;tcase++)
    {
        scanf("%d",&smax);
        cin>>shy;

        for(i=0;i<=smax;i++)
            arr[i]=shy[i]-'0';

        answer=0;
        sum=0;

        for(i=0;i<=smax;i++)
        {
            if(sum<i)
            {
                answer+=(i-sum);
                sum+=(i-sum);
            }

            sum+=arr[i];
        }

        printf("Case #%d: %d\n",tcase,answer);
    }

    return 0;
}
