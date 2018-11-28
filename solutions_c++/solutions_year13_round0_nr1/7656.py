#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
int cas,judgex,judgeo,totw;
char ch;
int x[16],o[16];

void jude(int line,int num)
{
    if (num == 1)
    {
        if ((x[line] && x[line-1]) && (x[line-2] && x[line-3])) judgex=1;
        return;
    }
    else
    {
        if ((o[line] && o[line-1]) && (o[line-2] && o[line-3])) judgeo=1;
    }
}

int main()
{
    freopen("google1.in","r",stdin);
    freopen("google1.out","w",stdout);
    scanf("%d\n", &cas);
    for (int i = 1; i <= cas; i++)
    {

       // memset(x,0, sizeof(x));
        //memset(o,0, sizeof(o));
        int cnt = 0, flag = 0;judgex=0,judgeo=0,totw=0;
        do
        {
            cnt++;

            scanf("%c", &ch);
           // printf("%c",ch);
            x[cnt] = 0;
            o[cnt] = 0;
            if ((ch == 'X')||(ch == 'T'))
            {
                x[cnt]=1;
            }
            if ((ch == 'O')||(ch == 'T')) o[cnt]=1;
            if (ch == '.')
            {
                totw++;
            }
            if (cnt %4 == 0)
            {

                if (!judgex) jude(cnt,1);
                if (!judgeo) jude(cnt,2);
                if (judgex && judgeo)
                {
                    printf("Case #%d: Draw\n",i);
                    flag = 1;
                }
                scanf("\n");
            }
        }

       while (cnt != 16);
//for (int i = 1; i<=16; i++) printf("%d",x[i]);
//        printf("\n");
//        for (int i = 1; i<=16; i++) printf("%d",o[i]);
//        printf("\n");


        if (!flag)
        {
            if (!judgex)
                if
                ((((x[1]&&x[6])&&(x[11]&&x[16])) || ((x[4]&&x[7])&&(x[10]&&x[13]))) ||
                ((( ((x[1]&&x[5]) && (x[9]&&x[13])) ) || ( ((x[2]&&x[6]) && (x[10]&&x[14])) ))  || (( ((x[3]&&x[7]) && (x[11]&&x[15])) ) || ( ((x[4]&&x[8]) && (x[12]&&x[16])) ))))
                judgex = 1;
            if (!judgeo)
                if ((((o[1]&&o[6])&&(o[11]&&o[16])) || ((o[4]&&o[7])&&(o[10]&&o[13]))) ||
                ((( ((o[1]&&o[5]) && (o[9]&&o[13])) ) || ( ((o[2]&&o[6]) && (o[10]&&o[14])) ))  || (( ((o[3]&&o[7]) && (o[11]&&o[15])) ) || ( ((o[4]&&o[8]) && (o[12]&&o[16])) ))))
                judgeo = 1;
            if (judgex && judgeo)
            {
                printf("Case #%d: Draw\n",i);
            }
            else
            {
                if (judgex)  printf("Case #%d: X won\n",i);
                else
                {
                    if (judgeo) printf("Case #%d: O won\n",i);
                    else
                    {
                        if (totw !=0) printf("Case #%d: Game has not completed\n",i);
                        else printf("Case #%d: Draw\n",i);
                    }
                }
            }



        }
        scanf("\n");
        scanf("\n");
    }
    return 0;
}
