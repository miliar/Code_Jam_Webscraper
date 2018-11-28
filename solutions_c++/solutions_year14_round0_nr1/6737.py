#include <stdio.h>
#include <algorithm>

using namespace std;

int main(){
FILE* input;
FILE* output;

input = fopen("A-small-attempt0.in","r");
output = fopen("output.txt", "w");

int t=0,ans1=0,ans2=0,b=0,n=0,ans=0,rubbish=0;
int possible[4]={0};

fscanf(input, "%d", &t);
for(int k=1;k<=t;k++){
    fscanf(input, "%d", &ans1);
    for(int i=0;i<4*(ans1-1);i++){
        fscanf(input,"%d", &rubbish); //skip n-1 lines of the map
    }
    for(int col=0;col<4;col++){
        fscanf(input, "%d", &possible[col]);
    }
    for(int i=0;i<4*(4-ans1);i++){
        fscanf(input,"%d", &rubbish);
    }
    fscanf(input, "%d", &ans2);
    for(int i=0;i<4*(ans2-1);i++){
        fscanf(input,"%d", &rubbish); //skip n-1 lines of the map
    }
    for(int col=0;col<4;col++){
        fscanf(input, "%d", &b);
        for(int i=0;i<4;i++){
            if(possible[i]==b){
                n++;
                ans=b;
            }
        }
    }
    for(int i=0;i<4*(4-ans2);i++){
        fscanf(input,"%d", &rubbish);
    }
    fprintf(output, "Case #%d: ",k);
    if(n==1){
        fprintf(output, "%d", ans);
    }
    else if(n==0){
        fprintf(output,"Volunteer cheated!");
    }
    else{
        fprintf(output,"Bad magician!");
    }
    fprintf(output,"\n");
    n=0;
}

fclose(input);
fclose(output);
}
