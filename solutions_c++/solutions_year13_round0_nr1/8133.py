#include<stdio.h>
#include<string.h>
using namespace std;
bool Win,Empty,Draw,Incomp;
char Input[6][6],PR;
void Mid(char C,int I){
    if((Input[0][I]==C||Input[0][I]=='T')&&(Input[1][I]==C||Input[1][I]=='T')&&(Input[2][I]==C||Input[2][I]=='T')&&(Input[3][I]==C||Input[3][I]=='T'))
    Win=true;
    if(Input[0][I]!='T') PR=Input[0][I];
    else PR=Input[1][I];
}

void First(char C){
    if((Input[0][0]==C||Input[0][0]=='T')&&(Input[0][1]==C||Input[0][1]=='T')&&(Input[0][2]==C||Input[0][2]=='T')&&(Input[0][3]==C||Input[0][3]=='T')){
        Win=true;
        if(Input[0][0]!='T') PR=Input[0][0];
        else PR=Input[0][1];
    }
    if(!Win){
        if((Input[0][0]==C||Input[0][0]=='T')&&(Input[1][1]==C||Input[1][1]=='T')&&(Input[2][2]==C||Input[2][2]=='T')&&(Input[3][3]==C||Input[3][3]=='T'))
        Win=true;
        if(Input[0][0]!='T') PR=Input[0][0];
        else PR=Input[1][1];
    }
    if(!Win){
        Mid(C,0);
    }
}

void Last(char C){
    if((Input[0][3]==C||Input[0][3]=='T')&&(Input[1][2]==C||Input[1][2]=='T')&&(Input[2][1]==C||Input[2][1]=='T')&&(Input[3][0]==C||Input[3][0]=='T')){
        Win=true;
        if(Input[0][3]!='T') PR=Input[0][3];
        else PR=Input[0][2];
    }
    if(!Win){
        Mid(C,3);
    }
}

bool Check(char *Input){
    if(Input[0]=='.'||Input[1]=='.'||Input[2]=='.'||Input[3]=='.') return true;
    return false;
}
int main()
{
    int I,K,L,M,N,Tcase;
    FILE *F;
    F=fopen("D:\\Output.txt","w");
    scanf("%d",&Tcase);
    N=0;
    while(Tcase--){
        ++N;
        Win=0;Empty=0;Draw=0;Incomp=0;
        scanf("\n");
        gets(Input[0]);
        if(Check(Input[0])) Empty=true;
        gets(Input[1]);
        if(Check(Input[1])) Empty=true;
        gets(Input[2]);
        if(Check(Input[2])) Empty=true;
        gets(Input[3]);
        if(Check(Input[3])) Empty=true;
        
        if(!Win&&Input[0][0]!='.'){
            First(Input[0][0]);
            if(Win){
              printf("Case #%d: %c won\n",N,PR);
              fprintf(F,"Case #%d: %c won\n",N,PR);
            }
        }
        if(!Win&&Input[0][1]!='.'){
            Mid(Input[0][1],1);
            if(Win){
              printf("Case #%d: %c won\n",N,PR);
              fprintf(F,"Case #%d: %c won\n",N,PR);
            }
        }
        if(!Win&&Input[0][2]!='.'){
            Mid(Input[0][2],2);
            if(Win){
              printf("Case #%d: %c won\n",N,PR);
              fprintf(F,"Case #%d: %c won\n",N,PR);
            }
        }
        if(!Win&&Input[0][3]!='.'){
            Last(Input[0][3]);
            if(Win){
              printf("Case #%d: %c won\n",N,PR);
              fprintf(F,"Case #%d: %c won\n",N,PR);
            }
        }
        if(!Win&&!Empty){
            printf("Case #%d: Draw\n",N);
            fprintf(F,"Case #%d: Draw\n",N);
        }
        if(!Win&&Empty){
        printf("Case #%d: Game has not completed\n",N);
        fprintf(F,"Case #%d: Game has not completed\n",N);
        }
    }
    return 0;
}
