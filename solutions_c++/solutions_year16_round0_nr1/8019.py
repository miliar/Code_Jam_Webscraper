#include "problem_name.h"
#include <cstdio>

bool isvisited[10];

void workout(int obj,int& visitednum)
{
        char ch[10];
        sprintf(ch,"%d\n",obj);
        int i = 0;
        while(ch[i]!='\n')
        {
                if (isvisited[ch[i]-'0'] == 0)
                {
                        isvisited[ch[i]-'0'] = 1;
                        ++visitednum;
                }
                ++i;
        }
        return;
}

int main()
{
        FILE* in = fopen("A-small-attempt0.in","r");
        FILE* out = fopen("A-small-attempt0.out","w");
        int t;
        fscanf(in,"%d",&t);
        for (int z=1;z<=t;++z)
        {
                for (int j=0;j<10;++j)
                        isvisited[j] = 0;
                int visitednum = 0;
                int obj;
                fscanf(in,"%d",&obj);
                if (obj == 0)
                {
                        fprintf(out,"Case #%d: INSOMNIA\n",z);
                        continue;
                }
                int time = 0;
                while(visitednum<10)
                {
                        ++time;
                        workout(time*obj,visitednum);
                }
                fprintf(out,"Case #%d: %d\n",z,time*obj);
        }
        fclose(in);
        fclose(out);
        return 0;
}
