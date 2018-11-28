#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <algorithm>
#include <map>
#include <string>
#include <iostream>
#include <ctime>
#include <cstdlib>
using namespace std;

char str[100][200];
int add[100][200],all[200];
int main()
{
    int t,T,N;
    freopen("A-small-attempt1.in.txt","r",stdin);
	freopen("A-small-attempt1.out.txt","w",stdout);
    scanf("%d",&T);
    for(t=1;t<=T;t++)
    {
        memset(add,0,sizeof(add));
        memset(all,0,sizeof(all));
        scanf("%d",&N);
        for(int i=0;i<N;i++)
        {
            scanf("%s",str[i]);
        }
        char temp[200];
        int count=0;
        temp[count++]=str[0][0];
        add[0][count-1]++;
        all[count-1]++;
        for(int j=1;str[0][j]!=0;j++)
        {
            if(str[0][j]==str[0][j-1])
            {
                all[count-1]++;
                add[0][count-1]++;
                continue;
            }
            else
            {
                temp[count++]=str[0][j];
                all[count-1]++;
                add[0][count-1]++;
            }
        }
        temp[count]=0;
        int flag=1;
        for(int i=1;i<N;i++)
        {
            count=0;
            for(int j=0;str[i][j]!=0;j++)
            {
                if(j>0&&str[i][j]==str[i][j-1])
                {
                    add[i][count-1]++;
                    all[count-1]++;
                    continue;
                }
                if(temp[count]==str[i][j])
                {
                    count++;
                    add[i][count-1]++;
                    all[count-1]++;
                }
                else
                {
                    flag=0;
                    break;
                }
            }
            if(temp[count]!=0)
            {
                flag=0;
                break;
            }
        }
        if(!flag)
        {
            printf("Case #%d: Fegla Won\n",t);
            continue;
        }
        count=0;
        for(int i=0;temp[i]!=0;i++)
        {
            int x=round((double)all[i]/N);
            for(int j=0;j<N;j++)
            {
                count+=abs(x-add[j][i]);
            }
        }
        printf("Case #%d: %d\n",t,count);
    }
    return 0;
}