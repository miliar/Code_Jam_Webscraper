#include<stdio.h>
#include<iostream>
int main(){
    FILE *op=fopen("output.in","w");
   FILE *ip=fopen("D-small-attempt0.in","rt");
    int t ,x,r,c,p=1 ;
    fscanf(ip,"%d",&t) ;
    while(t--){
    fscanf(ip,"%d",&x) ;
    fscanf(ip,"%d",&r) ;
    fscanf(ip,"%d",&c) ;
    if(x==1){
        fprintf(op,"Case #%d: GABRIEL\n",p);

    }
    else if(x==2){
        if(r%2==0||c%2==0){
            fprintf(op,"Case #%d: GABRIEL\n",p);
        }
        else
            fprintf(op,"Case #%d: RICHARD\n",p);
    }
    else if (x==3){
        if(r>=2&&c>=2&&(r*c)%3==0)
            fprintf(op,"Case #%d: GABRIEL\n",p);
            else
            fprintf(op,"Case #%d: RICHARD\n",p);
    }
    else if(x==4)
        if(r>=3&&c>=3&&(r*c)%4==0)
        fprintf(op,"Case #%d: GABRIEL\n",p);
        else
        fprintf(op,"Case #%d: RICHARD\n",p);
    else if(x==5)
        if(r*c>=20&&(r*c)%5==0)
        fprintf(op,"Case #%d: GABRIEL\n",p);
        else
        fprintf(op,"Case #%d: RICHARD\n",p);
    else if(x==6)
        if((r*c)>=30&&(r*c)%6==0)
        fprintf(op,"Case #%d: GABRIEL\n",p);
        else
        fprintf(op,"Case #%d: RICHARD\n",p);
    else
    {
     fprintf(op,"Case #%d: RICHARD\n",p);

    }
    p++;

    }
    return 0;
}
