#include<cstdio>
int xc[4],xl[4],oc[4],ol[4],od,xd,od2,xd2;
int t,f;
int main(){
    int w=0,h=0;
    scanf("%d",&t);
    here:
    w=0;
    h=0;
    for(int i=0;i<4;i++){
        xc[i]=0;
        xl[i]=0;
        oc[i]=0;
        ol[i]=0;
    }
    od=0;
    xd=0;
    od2=0;
    xd2=0;
    for(int i=0;i<4;i++){
        for(int j=0;j<4;j++){
            char c;
            scanf(" %c",&c);
            if(c=='T'){
                xc[i]++;
                xl[j]++;
                oc[i]++;
                ol[j]++;
            }
            if(c=='O'){
                oc[i]++;
                ol[j]++;
            }
            if(c=='X'){
                xc[i]++;
                xl[j]++;
            }
            if(c=='.'){
                h++;
            }
            if(i+j==3){
                if(c=='T'){
                    od++;
                    xd++;
                }
                if(c=='O'){
                    od++;
                }
                if(c=='X'){
                    xd++;
                }
            }
            if(i==j){
                if(c=='T'){
                    od2++;
                    xd2++;
                }
                if(c=='O'){
                    od2++;
                }
                if(c=='X'){
                    xd2++;
                }
            }
        }
    }
    if(h==0){
        w=-1;
    }
    for(int i=0;i<4;i++){
        if(xc[i]==4 || xl[i]==4){
            w=1;
        }
        if(oc[i]==4 || ol[i]==4){
            w=2;
        }
        //printf("-->xc[%d]=%d\n",i,xc[i]);
        //printf("-->xl[%d]=%d\n",i,xl[i]);
        //printf("-->oc[%d]=%d\n",i,oc[i]);
        //printf("-->ol[%d]=%d\n",i,ol[i]);
        
    }
    if(xd==4){
        w=1;
    }
    if(od==4){
        w=2;
    }
    if(xd2==4){
        w=1;
    }
    if(od2==4){
        w=2;
    }
    if(w==-1){
        printf("Case #%d: Draw\n",f+1);
    }
    else if(w==0){
        printf("Case #%d: Game has not completed\n",f+1);
    }
    else if(w==1){
        printf("Case #%d: X won\n",f+1);
    }
    else if(w==2){
        printf("Case #%d: O won\n",f+1);
    }
    if(f<t-1){f++;goto here;}
    return 0;
}
