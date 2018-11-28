#include <cstdio>
void printwin(FILE* fout,int win)
{
    if(win==1)
    {
        fprintf(fout,"X won\n");
    }
    else
    {
        if(win==2)
        {
            fprintf(fout,"O won\n");
        }
    }
}
void process(FILE* fin,FILE* fout,int n)
{
    int hor[4],ver[4],diag[2],to,win=0,havedot=0;
    char str[5];
    fprintf(fout,"Case #%d: ",n);
    for(int i=0;i<=3;i++)
    {
        hor[i]=3;
        ver[i]=3;
    }
    diag[0]=3;
    diag[1]=3;
    for(int i=0;i<=3;i++)
    {
        fscanf(fin,"%s",str);
        for(int j=0;j<=3;j++)
        {
            switch(str[j])
            {
            case 'X':
                to=1;
                break;
            case 'O':
                to=2;
                break;
            case 'T':
                to=3;
                break;
            case '.':
                to=0;
                havedot=1;
                break;
            }
            hor[i]&=to;
            ver[j]&=to;
            if(i==j)
            {
                diag[0]&=to;
            }
            if(i+j==3)
            {
                diag[1]&=to;
            }
        }
    }
    for(int i=0;i<=3;i++)
    {
        if(hor[i])
        {
            printwin(fout,hor[i]);
            return;
        }
        if(ver[i])
        {
            printwin(fout,ver[i]);
            return;
        }
    }
    if(diag[0])
    {
        printwin(fout,diag[0]);
        return;
    }
    if(diag[1])
    {
        printwin(fout,diag[1]);
        return;
    }
    if(havedot==0)
    {
        fprintf(fout,"Draw\n");
    }
    else
    {
        fprintf(fout,"Game has not completed\n");
    }
}
int main()
{
    FILE* fin;
    FILE* fout;
    int n;
    fin=fopen("1.in.large.txt","r");
    fout=fopen("1.out.large.txt","w");
    fscanf(fin,"%d",&n);
    for(int i=1;i<=n;i++)
    {
        process(fin,fout,i);
    }
    fclose(fin);
    fclose(fout);
    return 0;
}
