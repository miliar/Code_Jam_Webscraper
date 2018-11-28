#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <algorithm>
#define N (1<<12)

char ico[3]={'P','R','S'};

char _list[N],_buf[N];

void generate(char *list,int step)
{
    if(!step)return ;
    list[step]=(*list+1)%3;
    generate(list,step>>1);
    generate(list+step,step>>1);
}
void sort(char *list,int step)
{
    if(!step)return ;
    sort(list,step>>1);
    sort(list+step,step>>1);
    if(memcmp(list,list+step,step)>0)
    {
        memcpy(_buf,list,step);
        memcpy(list,list+step,step);
        memcpy(list+step,_buf,step);
    }
}

int main()
{
    int T;
    scanf("%d",&T);
    for(int tc=1;tc<=T;++tc)
    {
        printf("Case #%d: ",tc);
        int n,p[3];
        scanf("%d%d%d%d",&n,p+1,p,p+2);
        int s[3]={1,0,0};
        for(int i=1<<(n-1);i;i>>=1)
        {
            int tmp=s[0]+s[2];
            s[2]+=s[1];
            s[1]+=s[0];
            s[0]=tmp;
        }
        int cnt=0;
        while(cnt!=3)
        {
            if(s[0]==p[(0+cnt)%3]&&s[1]==p[(1+cnt)%3]&&s[2]==p[(2+cnt)%3])break;
            ++cnt;
        }
        if(cnt==3)printf("IMPOSSIBLE\n");
        else
        {
            _list[0]=cnt;
            generate(_list,1<<(n-1));
            sort(_list,1<<(n-1));
            for(int i=0,e=1<<n;i!=e;++i)
            {
                printf("%c",ico[_list[i]]);
            }
            printf("\n");
        }
    }
    return 0;
}
