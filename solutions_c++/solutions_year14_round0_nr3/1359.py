#include<cstdio>
#include<cstring>

char lst[55][55];

void print(int r,int c)
{
    for(int i = 0; i < r; i ++)
    {
        printf("%s\n",lst[i]);
    }
}

int main()
{
    int ti;scanf("%d",&ti);
    for(int ca=1; ca<=ti; ca++)
    {
        memset(lst,0,sizeof(lst));
        int rr,cc,mm;scanf("%d%d%d",&rr,&cc,&mm);
        for(int i = 0; i < rr; i ++)
        for(int j = 0; j < cc; j ++)
            lst[i][j] = '.';
        lst[0][0] = 'c';
        int r = rr, c = cc, m = mm;
        while(m>=r||m>=c)
        {
            if(r > c)
            {
                for(int i = 0; i < c; i ++)
                {
                    lst[r-1][i] = '*';
                }
                m-=c;
                r--;
            }
            else
            {
                for(int i = 0; i < r; i ++)
                {
                    lst[i][c-1] = '*';
                }
                m-=r;
                c--;
            }
        }
        int rp = r-1, cp = c-1;
        if(m > 0)
        {
            lst[rp--][cp--] = '*';
            m --;
            while(m > 0)
            {
                if(rp > cp)
                {
                    lst[rp--][c-1] = '*';
                }
                else
                {
                    lst[r-1][cp--] = '*';
                }
                m--;
            }
        }
        printf("Case #%d:\n",ca);
        if((rp == 0 || cp == 0)&& rr!=1 && cc!=1 && rr*cc-1!= mm)
        {
            //print(rr,cc);
            printf("Impossible\n");
        }
        else print(rr,cc);
    }
}
