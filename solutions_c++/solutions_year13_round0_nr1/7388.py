#include <iostream>
#define N 4
#define XW 1
#define OW 2
#define DRAW 3
#define NC 4

//prototypes
int is_xort(char c);
int is_oort(char c);

using namespace std;

int main()
{
    int T=0;
    char map[N][N]={0};
    freopen("output","w",stdout);
    freopen("input","r",stdin); 

    int index=0; 
    scanf("%d\n",&T);
    int status=DRAW;//初始态定为"平局"
    int num=1;
    int i=0,j=0; 
    for(index=0;index<T;index++)
    {
        status=DRAW;
        for(i=0;i<N;i++)
        {
            for(j=0;j<N;j++)
                scanf("%c",&map[i][j]);
            scanf("\n");
        }
        for(i=0;i<N;i++)
        {
            //判断行X
            if(is_xort(map[i][0]) && is_xort(map[i][1]) && is_xort(map[i][2]) && is_xort(map[i][3]))
            {
                status=XW;    
                goto end_now;
            }

            //判断行O
            if(is_oort(map[i][0]) && is_oort(map[i][1]) && is_oort(map[i][2]) && is_oort(map[i][3]))
            {
                status=OW; 
                goto end_now;
            }
            
            //判断列X
            if(is_xort(map[0][i]) && is_xort(map[1][i]) && is_xort(map[2][i]) && is_xort(map[3][i]))
            {
                status=XW; 
                goto end_now;
            }
            
            //判断列O
            if(is_oort(map[0][i]) && is_oort(map[1][i]) && is_oort(map[2][i]) && is_oort(map[3][i]))
            {
                status=OW; 
                goto end_now;
            }
        }

        //判断对角线X
        if( (is_xort(map[0][0])) && is_xort(map[1][1]) && is_xort(map[2][2]) && is_xort(map[3][3])|| (is_xort(map[0][3]) && is_xort(map[1][2]) && is_xort(map[2][1]) && is_xort(map[3][0])))
        {
            status=XW;
            goto end_now;
        }
        
        //判断对角线O
        if( (is_oort(map[0][0])) && is_oort(map[1][1]) && is_oort(map[2][2]) && is_oort(map[3][3])|| (is_oort(map[0][3]) && is_oort(map[1][2]) && is_oort(map[2][1]) && is_oort(map[3][0])))
        {
            status=OW; 
            goto end_now;
        }        
        //判断平局或者未完成
        for(i=0;i<N;i++)
        {
            for(j=0;j<N;j++) 
            {
                if(map[i][j]=='.') 
                {
                    status=NC;
                    goto end_now;
                }
            }
        }

end_now:
        //用switch case来处理四种状态的输出。之后num++.
        switch(status)
        {
        case(XW):
            printf("Case #%d: X won\n",num);
            break;
        case(OW):
            printf("Case #%d: O won\n",num);
            break;
        case(DRAW):
            printf("Case #%d: Draw\n",num);
            break;
        case(NC):
            printf("Case #%d: Game has not completed\n",num);
            break;
        }
        num++;
    }

    fclose(stdin);
    fclose(stdout);
    return 0;
}

int is_xort(char c)
{
    if(c=='X' || c=='T')
        return 1;
    return 0;
}

int is_oort(char c)
{
    if(c=='O' || c=='T')
        return 1;
    return 0;
}
