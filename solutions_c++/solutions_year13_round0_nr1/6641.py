/*
ID: ankitgu1
LANG: C++
TASK: holstein
*/
#include <iostream>
#include <fstream>
#include <cstring>
#include <string>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>

using namespace std;

FILE *in,*out;

#define MAX(a,b) ((a)>(b)?(a):(b))

typedef long long LL;
typedef long L;

int is_prime(long long num){
    for(long long t=2;t<=sqrt(num);t++){
    if(num%t==0)return 0;
    }return 1;
}
LL gcd(LL a,LL b){
    if(a%b==0)return b;
    return gcd(b,a%b);
}
int compare (const void * a, const void * b)
{
    return ( *(int*)a - *(int*)b );
}
int dec_compare (const void * a, const void * b)
{
    return ( - *(int*)a + *(int*)b );
}
//////////////////////////

int main(){
    in=fopen("input.in","r");
    out=fopen("output.in","w");
    int cases;
    fscanf(in,"%d",&cases);
    for(int test=0;test<cases;test++){
        char str[5][5];
        for(int t=0;t<4;t++)fscanf(in,"%s",str[t]);
        //for(int t=0;t<4;t++)cout<<str[t]<<endl;cout<<endl;

        //checking for X
        int won=0,complete=1;
        for(int t=0;t<4;t++){
            if(complete)for(int tt=0;tt<4;tt++)if(str[t][tt]=='.'){complete=0;break;}
            if((str[t][0]=='X' || str[t][0]=='T')&&(str[t][1]=='X' || str[t][1]=='T')&&(str[t][2]=='X' || str[t][2]=='T')&&(str[t][3]=='X' || str[t][3]=='T')){
                won=1;break;
            }
            if((str[0][t]=='X' || str[0][t]=='T')&&(str[1][t]=='X' || str[1][t]=='T')&&(str[2][t]=='X' || str[2][t]=='T')&&(str[3][t]=='X' || str[3][t]=='T')){
                won=1;break;
            }if((str[t][0]=='O' || str[t][0]=='T')&&(str[t][1]=='O' || str[t][1]=='T')&&(str[t][2]=='O' || str[t][2]=='T')&&(str[t][3]=='O' || str[t][3]=='T')){
                won=2;break;
            }
            if((str[0][t]=='O' || str[0][t]=='T')&&(str[1][t]=='O' || str[1][t]=='T')&&(str[2][t]=='O' || str[2][t]=='T')&&(str[3][t]=='O' || str[3][t]=='T')){
                won=2;break;
            }
        }

        if((str[0][0]=='X' || str[0][0]=='T')&&(str[1][1]=='X' || str[1][1]=='T')&&(str[2][2]=='X' || str[2][2]=='T')&&(str[3][3]=='X' || str[3][3]=='T'))won=1;
        if((str[3][0]=='X' || str[3][0]=='T')&&(str[2][1]=='X' || str[2][1]=='T')&&(str[1][2]=='X' || str[1][2]=='T')&&(str[0][3]=='X' || str[0][3]=='T'))won=1;
        if((str[0][0]=='O' || str[0][0]=='T')&&(str[1][1]=='O' || str[1][1]=='T')&&(str[2][2]=='O' || str[2][2]=='T')&&(str[3][3]=='O' || str[3][3]=='T'))won=2;
        if((str[3][0]=='O' || str[3][0]=='T')&&(str[2][1]=='O' || str[2][1]=='T')&&(str[1][2]=='O' || str[1][2]=='T')&&(str[0][3]=='O' || str[0][3]=='T'))won=2;


        fprintf(out,"Case #%d: ",test+1);
        if(won==1)fprintf(out,"X won\n");
        else if(won==2)fprintf(out,"O won\n");
        else if(!complete)fprintf(out,"Game has not completed\n");
        else fprintf(out,"Draw\n");
    }
    return 0;
}
