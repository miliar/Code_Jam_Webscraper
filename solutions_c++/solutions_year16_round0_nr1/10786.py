#include<bits/stdc++.h>
using namespace std;
int num[10];
char nums[500];
int main()
{
    int T,N;
    freopen("output.txt","w",stdout);
    while(scanf("%d",&T)!=EOF)
    {
        for(int i=1;i<=T;i++)
        {
            for(int q=0;q<10;q++)num[q]=0;
            scanf("%d",&N);
            printf("Case #%d: ",i);
            int tmp;
            int complete=0;int nownum=0;
            for(int i=1;i<=100;i++)
            {
                tmp=N*i;
                sprintf(nums,"%d",tmp);
                int l=strlen(nums);


                for(int j=0;j<l;j++)
                {
                    int temp=(nums[j]-48);
                    //printf("%d",temp);
                    if(num[temp]==0){num[temp]++;nownum++;}
                    if(nownum==10)complete=1;
                    //printf("nownum=%d\n",nownum);
                }
                if(complete==1)break;
            }
            if(complete)printf("%d\n",tmp);
            else printf("INSOMNIA\n");
        }
    }

}
