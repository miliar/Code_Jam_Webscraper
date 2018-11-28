#include<cstdio>

using namespace std;

int main()
{
    int test;
    scanf("%d",&test);

    for(int i=0;i<test;i++)
    {
        int row1,row2,a;
        int arr[10];
        int b[5][5];
        scanf("%d",&row1);

        for(int j=0;j<4;j++)
        {
            for(int k=0;k<4;k++)
            {
                scanf("%d",&a);
                if(j+1==row1)
                {
                    arr[k]=a;
                }
            }
        }
        scanf("%d",&row2);

        int count=0;

        for(int j=0;j<4;j++)
        {
            for(int k=0;k<4;k++)
            {
                scanf("%d",&b[j][k]);
            }
        }
        int choice;
        for(int j=0;j<4;j++)
        {
            for(int k=0;k<4;k++)
            {
                if(arr[j]==b[row2-1][k])
                {
                    count+=1;
                    choice=arr[j];
                    break;
                }
            }
        }

        if(count==0)
        printf("Case #%d: Volunteer cheated!",i+1);
        else if(count==1)
        printf("Case #%d: %d",i+1,choice);
        else
        printf("Case #%d: Bad magician!",i+1);

        printf("\n");
    }
}
