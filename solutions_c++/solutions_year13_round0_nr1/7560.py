#include<stdio.h>

char pan[5][5];

int make_more(int a[])
{
    int i;
    char c;

    c=a[0];
    if(c=='T')
        c=a[1];
    if(c=='.')
        return 0;
    for(i=0;i<4;i++){
        if(c!=a[i] && a[i]!='T')
            return 0;
    }

    if(c=='X')
        return 1;
    return 2;
}


int make(void)
{
    int i,j,k,e=0;
    int a[5];

    for(i=0;i<4;i++){
        for(j=0;j<4;j++){
            a[j]=pan[i][j];
            if(pan[i][j]=='.'){
                e++;
            }
        }

        k=make_more(a);
        if(k>0)
            return k;

        for(j=0;j<4;j++){
            a[j]=pan[j][i];

        }
         k=make_more(a);
        if(k>0)
            return k;
    }

    for(i=0;i<4;i++){

    }

    for(i=0;i<4;i++){
        a[i]=pan[i][i];
    }
    k=make_more(a);
    if(k>0)
        return k;

    for(i=0;i<4;i++){
        a[i]=pan[i][3-i];
    }
    k=make_more(a);
    if(k>0)
        return k;
    if(e>0)
        return -1;
    return 0;
}




int main(void)
{
    int i,j,t,k;

    FILE *in,*out;
    in=fopen("input.txt","r");
    out=fopen("out.txt","w");

    fscanf(in,"%d",&t);

    for(i=1;i<=t;i++){
        for(j=0;j<4;j++){
            fscanf(in,"%s", pan[j]);
        }
        k=make();

        if(k==-1){
        fprintf(out,"Case #%d: Game has not completed\n",i);
        }else if(k==0){
            fprintf(out,"Case #%d: Draw\n",i);
        }else if(k==1){
            fprintf(out,"Case #%d: X won\n",i);
        }else if(k==2){
            fprintf(out,"Case #%d: O won\n",i);
        }
    }

    return 0;
}

