#include<cstdio>
int t,x,r,c,nc;
FILE *f,*g;
int main(){
    f=fopen("d.in","r");
    g=fopen("d.out","w");
    fscanf(f,"%d",&t);
    while(t--){
        nc++;
        fscanf(f,"%d%d%d",&x,&r,&c);
        if(x==1){
            fprintf(g,"Case #%d: GABRIEL\n",nc);
            continue;
        }
        if(x==2){
            if(r%2==0||c%2==0)
                fprintf(g,"Case #%d: GABRIEL\n",nc);
            else
                fprintf(g,"Case #%d: RICHARD\n",nc);
            continue;
        }
        if(x==3){
            if( (r==2&&c==3) || (r==3&&c==2) || (r==3&&c==3) || (r==3&&c==4) || (r==4&&c==3) )
                fprintf(g,"Case #%d: GABRIEL\n",nc);
            else
                fprintf(g,"Case #%d: RICHARD\n",nc);
            continue;
        }
        if(x==4){
            if( (r==3&&c==4) || (r==4&&c==3) || (r==4&&c==4) )
                fprintf(g,"Case #%d: GABRIEL\n",nc);
            else
                fprintf(g,"Case #%d: RICHARD\n",nc);
            continue;
        }
    }
    fclose(f);
    fclose(g);
    return 0;
}
