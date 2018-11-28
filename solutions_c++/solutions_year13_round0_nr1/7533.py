#include<stdio.h>

char pan[5][5];

int nerhae(char a[5]){
    int i;
    char c;

    c=a[0];
    if(c=='T')
        c=a[1];
    for(i=0;i<4;i++){
        if(a[i]=='.')
            return 0;
        if(c!=a[i] && a[i]!='T')
            return 0;
    }
    if(c=='X')
        return 2;

    return 1;
}
int yahhae(void){
    int i,j,w=0;
    int k;
    char a[5];

    for(i=0;i<4;i++){

        //heritage
        for(j=0;j<4;j++){
            a[j]=pan[i][j];
            if(pan[i][j]=='.')
                w++;
        }

        k=nerhae(a);
        if(k>0)
            return k;

        //ver
        for(j=0;j<4;j++){
            a[j]=pan[j][i];
        }

        k=nerhae(a);
        if(k>0)
            return k;
    }

    //right-down diagonal
    for(j=0;j<4;j++){
        a[j]=pan[j][j];
    }

     k=nerhae(a);
    if(k>0)
        return k;

    //left-down diagonal
    for(j=0;j<4;j++){
        a[j]=pan[j][3-j];
    }

     k=nerhae(a);
    if(k>0)
        return k;

    if(w>0)
        return -1;
    return 0;
}

int main(void)
{
    FILE *in,*out;
    int i,j,t,k;

    in=fopen("input.txt","r");
    out=fopen("output.txt","w");

    fscanf(in,"%d",&t);

    for(i=1;i<=t;i++){
        for(j=0;j<4;j++){
            fscanf(in,"%s",pan[j]);
        }

        k=yahhae();

        if(k==-1){
            fprintf(out,"Case #%d: Game has not completed\n",i);
        }else if(k==0){
            fprintf(out,"Case #%d: Draw\n",i);
        }else if(k==1){
            fprintf(out,"Case #%d: O won\n",i);
        }else{
            fprintf(out,"Case #%d: X won\n",i);
        }
    }
    return 0;
}
