#include<iostream>
#include<stdio.h>
#include<string.h>

int main()
{
    FILE *fp;
    fp=fopen("abc.txt","w");
    int l=0;
    int t;
    scanf("%d",&t);
    while(t--)
    {
        l++;
        int arr[16];
        for(int i=0;i<16;i++)
            arr[i]=0;
        int a;
        scanf("%d",&a);
        for(int i=0;i<4;i++)
        {
            if(i==a-1)
            {
                for(int j=0;j<4;j++)
                {
                    int x;
                    scanf("%d",&x);
                    arr[x-1]=1;
                }
            }
            else
            {
                for(int j=0;j<4;j++)
                {
                    int x;
                    scanf("%d",&x);

                }
            }

        }
        int b;
        int a1=0,a2=0;
        scanf("%d",&b);
        for(int i=0;i<4;i++)
        {
            if(i==b-1)
            {
                for(int j=0;j<4;j++)
                {
                    int x;
                    scanf("%d",&x);
                    if(arr[x-1])
                    {
                        if(a1)
                            a2=1;
                        else
                            a1=x;
                    }
                }
            }
            else
            {
                for(int j=0;j<4;j++)
                {
                    int x;
                    scanf("%d",&x);

                }
            }

    }
                if(a2)
                fprintf(fp,"Case #%d: Bad magician!\n",l);
            else if(a1)
                fprintf(fp,"Case #%d: %d\n",l,a1);
            else
                fprintf(fp,"Case #%d: Volunteer cheated!\n",l);
    }

    return 0;
}
