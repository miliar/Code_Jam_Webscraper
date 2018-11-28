#include <stdio.h>
#include <math.h>
#include <iostream>
int main()
{
     freopen("1.in","r",stdin); //输入重定向，输入数据将从in.txt文件中读取
    freopen("1.out","w",stdout); //输出重定向，输出数据将保存在out.txt文件中

    int T;
    scanf("%d",&T);
    for(int testcase=1;testcase<=T;testcase++){
        int first,second,temp;
        int ans[4];
        int flag[4];
        scanf("%d",&first);
        for(int i = 0;i<4;i++ ){
            for(int j=0;j<4;j++){
                if(i==first-1){
                    scanf("%d",&ans[j]);
                    flag[j]=0;
                }
                else
                    scanf("%d",&temp);
            }
        }
        scanf("%d",&second);
        for(int i = 0;i<4;i++ ){
            for(int j=0;j<4;j++){
                scanf("%d",&temp);
                if(i==second-1){
                    for(int k=0;k<4;k++){
                        if(ans[k]==temp)
                            flag[k]=1;
                    }
                }
            }
        }

        int count =0;
        int res =-1;
        for(int i=0;i<4;i++){
            if(flag[i]==1){
                count++;
                res =  ans[i];
            }
        }
        if(count==0)
            printf("Case #%d: Volunteer cheated!\n",testcase);
        else if(count>1)
            printf("Case #%d: Bad magician!\n",testcase);
        else
            printf("Case #%d: %d\n",testcase,res);

    }
     fclose(stdin);//关闭文件
    fclose(stdout);//关闭文件
    return 0;
}
