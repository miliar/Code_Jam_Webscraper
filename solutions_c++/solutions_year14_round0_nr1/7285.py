#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int main()
{
    freopen("in.txt","r",stdin); //输入重定向，输入数据将从in.txt文件中读取
    freopen("out.txt","w",stdout); //输出重定向，输出数据将保存在out.txt文件中
    int a[5][5],b[5],t,count,num;
    int answer1,answer2;
    scanf("%d",&t);
    for (int k=1;k<=t;k++)
    {
        scanf("%d",&answer1);
        for (int i=1;i<=4;i++)
        for (int j=1;j<=4;j++)
        {
            scanf("%d",&a[i][j]);
        }
        b[1]=a[answer1][1];b[2]=a[answer1][2];b[3]=a[answer1][3];b[4]=a[answer1][4];
        scanf("%d",&answer2);
        for (int i=1;i<=4;i++)
        for (int j=1;j<=4;j++)
        {
            scanf("%d",&a[i][j]);
        }
        count=0;
        for (int i=1;i<=4;i++)
        for (int j=1;j<=4;j++)
        if (b[i]==a[answer2][j])
        {
            count++;
            num=a[answer2][j];
        }
        if(count==0) printf("Case #%d: Volunteer cheated!\n",k);
        else if(count==1) printf("Case #%d: %d\n",k,num);
        else if(count>1) printf("Case #%d: Bad magician!\n",k);
    }
    fclose(stdin);//关闭文件
    fclose(stdout);//关闭文件
    return 0;
}
