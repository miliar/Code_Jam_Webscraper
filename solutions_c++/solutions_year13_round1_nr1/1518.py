#include <cstdio>
#include <algorithm>

using namespace std;

int main(){
FILE* input;
FILE* output;

input = fopen("A-small-attempt0.in","r"); //dont forget to change to .in
output = fopen("output.in","w");

int num=0,t=0,r=0,change=0,ans=0;
fscanf(input,"%d",&num);

for(int i=1;i<=num;i++){
    fscanf(input,"%d",&r);
    fscanf(input,"%d",&t);
    while(t>0){
        t=t-((r+1+change)*(r+1+change)-(r+change)*(r+change));
        if(t<0){
            break;
        }
        ans++;
        change+=2;
    }
    fprintf(output,"Case #%d: %d\n",i,ans);
    ans=0;
    change=0;
}


fclose(input);
fclose(output);
}
