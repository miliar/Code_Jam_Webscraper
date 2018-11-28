#include<cstdio>
#include<cstdlib>

using namespace std;

int main(){
    int t,ans,x,y,g;
    char mem[4][4],pivot,pivot1,pivot2,l,r;

    scanf("%d",&t);
    for(int no=1;no<=t;no++){
        g=0; getchar();
        for(int l=0;l<4;l++){
            for(int ll=0;ll<4;ll++){
                scanf("%c",&mem[l][ll]);
                if(g==0 && mem[l][ll]=='.')g=1;
            }getchar();
        }
        ans='z';
        for(int l=0;l<4;l++){
            if(mem[l][l]=='.')continue;

            x=y=0; pivot=mem[l][l];
            if(pivot!='T'){
                pivot1=pivot2=pivot;
            }else{
                if(l+1<4){
                    pivot1=mem[l][l+1]; if(pivot1=='.')x=1;
                    pivot2=mem[l+1][l]; if(pivot2=='.')y=1;
                }else{
                    pivot1=mem[l][l-1]; if(pivot1=='.')x=1;
                    pivot2=mem[l-1][l]; if(pivot2=='.')y=1;
                }
            }
            for(int ll=0;ll<4;ll++){
                if(x==0 && (mem[l][ll]!=pivot1 && mem[l][ll]!='T'))x=1;
                if(y==0 && (mem[ll][l]!=pivot2 && mem[ll][l]!='T')) y=1;
            }

            if(x==0){
                if(pivot1=='X')ans='x';
                else ans='y';
            }else if(y==0){
                if(pivot2=='X')ans='x';
                else ans='y';
            }
            if(ans!='z')break;
        }

        if(ans=='z'){
            x=y=0;

            if(mem[0][0]=='.')x=1;
            else if(mem[0][0]!='T') pivot1=mem[0][0];
            else pivot1=mem[1][1];

            if(mem[0][3]=='.')y=1;
            else if(mem[0][3]!='T') pivot2=mem[0][3];
            else pivot2=mem[1][2];

            for(int l=0;l<4;l++){
                if(x==0 && mem[l][l]!=pivot1 && mem[l][l]!='T')x=1;
                if(y==0 && mem[l][3-l]!=pivot2 && mem[l][3-l]!='T')y=1;
            }
            if(x==0){
                if(pivot1=='X')ans='x';
                else ans='y';
            }else if(y==0){
                if(pivot2=='X')ans='x';
                else ans='y';
            }
        }
        if(no>1)printf("\n");
		printf("Case #%d: ",no);
        if(ans=='z'){
            if(g==1) printf("Game has not completed");
            else printf("Draw");
        }else if(ans=='x') printf("X won");
        else if(ans=='y') printf("O won");
    }
return 0;
}
