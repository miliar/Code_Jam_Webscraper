#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;
int main()
{
    freopen("c:\\temp\\in.txt","r",stdin);
    freopen("c:\\temp\\out.txt","w",stdout);
    int test_case;
    scanf("%d",&test_case);
    for(int ca=1;ca<=test_case;ca++)
    {
      int data[5][5];
      int first_ans,second_ans;
      scanf("%d",&first_ans);
      for(int i=1;i<=4;i++)
      {
          for(int j=1;j<=4;j++)
            scanf("%d",&data[i][j]);
      }
      int value_1[5],value_2[5];
        for(int i=1;i<=4;i++)
        value_1[i]=data[first_ans][i];
           scanf("%d",&second_ans);
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
           scanf("%d",&data[i][j]);
        }
           int cou=0,out=-1;
        for(int i=1;i<=4;i++)
        {
            value_2[i]=data[second_ans][i];
        }
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            if(value_1[i]==value_2[j])
            {
                cou++;out=value_1[i];
            }
        }
        if(cou==0)
            printf("Case #%d: Volunteer cheated!\n",ca);
        else if(cou==1)
              printf("Case #%d: %d\n",ca,out);
        else   printf("Case #%d: Bad magician!\n",ca);
    }
    return 0;
}
