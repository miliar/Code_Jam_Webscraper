/***    google_code_jam_pro1    ***/

#include <stdio.h>

using namespace std;

char data[1001];

int T,S_max;

int temp_num,used_num;

void work()
{
    for(int i=1;i<=T;++i)
    {
        scanf("%d %s",&S_max,data);
        /**init**/
        temp_num=data[0]-'0';
        used_num=0;
        /** work**/
        for(int j=1;j<=S_max;++j)
        {
            if(data[j]=='0'){continue;}
            else
            {
                if(temp_num<j)
                {
                    used_num+=j-temp_num;
                    temp_num=j;
                }
                temp_num+=data[j]-'0';
            }
        }
        printf("Case #%d: %d\n",i,used_num);
    }
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&T);getchar();
    work();
    fclose(stdin);
    fclose(stdout);
    return 0;
}
