#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<sys/types.h>
#include<sys/stat.h>
#include<fcntl.h>
#include<math.h>

int board[4][4];

int draw()
{
    for(int i=0;i<4;i++)
        for(int j; j<4;j++)
            if (board[i][j]==0)
                return 1;
    return 0;
}
int hor()
{
    int n,ref;
    for(int i=0;i<4;i++)
    {
        n=0;
        ref=i;
        for (int j=0; j<4;j++)
        {
            if (board[ref][0]==3)
                ref=i+1;
            if ( board[i][j]==0 || (board[i][j]!=board[ref][0] && board[i][j]!=3))
                break;
            else
                n++;
        }
        if (n==4)
        {
            return board[ref][0];
        }
    }
    return 0;
}
int vert()
{
    int n,ref;
    for(int i=0;i<4;i++)
    {
        n=0;
        ref=i;
        for (int j=0; j<4;j++)
        {
            if (board[0][ref]==3)
                ref=i+1;
            if ((board[j][i]!=board[0][ref] && board[j][i]!=3)||board[j][i]==0)
                break;
            else
                n++;
        }
        //printf("%d \n", n);
        if (n==4)
        {
            return board[0][ref];
        }
    }
    return 0;
}
int diag()
{
    int n=0, ref=0;
    for(int i=0; i<4;i++)
    {
        if (board[ref][ref]==3)
            ref=1;
        if ((board[i][i]!=board[ref][ref] && board[i][i]!=3) || board[i][i]==0)
            break;
        else
            n++;
    }
    if (n==4)
    {
        return board[ref][ref];
    }
    n=0;
    ref=0;
    for(int i=0; i<4;i++)
    {
        if (board[ref][3-ref]==3)
            ref=1;
        if ((board[i][3-i]!=board[ref][3-ref] && board[i][3-i]!=3) || board[i][3-i]==0)
            break;
        else
            n++;
    }
    if (n==4)
    {
        return board[ref][3-ref];
    }
    return 0;
}

int readFile(FILE* pf)
{
    char s[6];
    int c,j=0;
    for(int i=0; i<4 ; i++)
    {
        j=0;
        while((c=fgetc(pf))!=10)
        {
            //printf("%c  : %d\n", c,c);
            s[j]=(char)c;
            j++;
        }
        for(int j=0;j<4;j++)
        {
            switch (s[j])
            {
                case 'X':
                    board[i][j]=1;
                    break;
                case 'O':
                    board[i][j]=2;
                    break;
                case 'T':
                    board[i][j]=3;
                    break;
                case '.':
                    board[i][j]=0;
                    break;
            }
            //printf("%c", s[j]);
        }
        //printf("\n");
    }
}
int whoswinning()
{
    int v,h,d,di;
    v=vert();
    h=hor();
    di=diag();
    d=draw();
    if(!v && !h && !di && !d)
        return 3;
    else if(!v && !h && !di && d)
        return 4;
    else if(v)
        return v;
    else if(h)
        return h;
    else if(di)
        return di;
    return 0;
}
int main(int argc, char* argv[])
{
    FILE* pf;
    int fd;
    int c;
    char nbr[4];
    int nb=0;
    char* path=argv[1];
    int win;
    if((pf=fopen(path,"r"))==NULL)
    {
        perror("fopen");
        exit(EXIT_FAILURE);
    }
    int j=0;
    while((c=fgetc(pf))!=10)
    {
        nbr[j]=c;
        //printf("%c : %d \n", c,c);
        //printf("%c : %d \n", nbr[j],nbr[j]);
        j++;
    }
    j--;
    for(int i=0; i<j ; i++)
    {
        int k=0;
        k=(int)nbr[i]%'0';
        nb+=k*pow(10,j-i);
    }
    //printf("%d cas \n", nb);
    for (int j=0 ; j<nb ; j++)
    {
        readFile(pf);
        /*for(int i=0; i<4;i++)
        {
            for(int j=0;j<4;j++)
                printf("%d ", board[i][j]);
            printf("\n");
        }*/
        printf("Case #%d: ",j+1);
        //printf("Vert : %d \n" ,vert());
        //printf("Hor : %d \n" ,hor());
        //printf("Diag : %d \n" ,diag());
        //printf("Draw : %d \n" ,draw());
        switch (win=whoswinning())
        {
            case (1):
                printf("X won\n");
                break;
            case (2):
                printf("O won\n");
                break;
            case (4):
                printf("Game has not completed\n");
                break;
            default:
                printf("Draw\n");
                break;
                
        }
        fseek(pf,1,SEEK_CUR);
    }
    fclose(pf);
    return 0;
}