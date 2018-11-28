#include <cstdio>

using namespace std;

int main()
{
    FILE* fin=fopen("a.in","r");
    FILE* fout=fopen("a.out","w");
    int n=0,t=0,tt=1;
    int ok = 0;

    long long now =0,tmp = 0;
    fscanf(fin,"%d",&t);

    while (t--)
    {
        fscanf(fin,"%d",&n);

        now = 0;

        ok = 0;

        if (n == 0)
        {
            fprintf(fout,"Case #%d: INSOMNIA\n",tt++);
            continue;
        }

        do
        {
            now += n;

            tmp = now;

            while (tmp!=0)
            {
                ok|=(1<<(tmp%10));
                tmp/=10;
            }

        }
        while (ok != 0x3ff);

        fprintf(fout,"Case #%d: %I64d\n",tt++,now);
    }

    return 0;
}
