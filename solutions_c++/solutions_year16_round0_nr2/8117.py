#include "problem_name.h"
#include <cstdio>
#include <cstring>

int main()
{
        FILE* in = fopen("B-large.in","r");
        FILE* out = fopen("B-large.out","w");
        int t;
        fscanf(in,"%d",&t);
        for (int z=1;z<=t;++z)
        {
                char ch[105];
                fscanf(in,"%s",ch);
                int l = strlen(ch);
                char sign = ch[0];
                int result = 0;
                for (int i=1;i<l;++i)
                {
                        if (ch[i]!=sign)
                        {
                                ++result;
                                sign = ch[i];
                        }
                }
                if (ch[l-1] == '-') ++result;
                fprintf(out,"Case #%d: %d\n",z,result);
        }
        fclose(in);
        fclose(out);
        return 0;
}
