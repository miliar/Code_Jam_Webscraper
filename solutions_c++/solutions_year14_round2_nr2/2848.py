#include <stdio.h>
#include <algorithm>
#include <iterator>
#include <math.h>

using namespace std;

int main(){
FILE*input;
FILE*output;

input=fopen("B-small-attempt0.in","r");
output=fopen("output.txt","w");

int t=0,a=0,b=0,k=0,r=0,ans=0;

fscanf(input,"%d",&t);
for(int s=1;s<=t;s++){
    fscanf(input,"%d %d %d",&a, &b, &k);
    for(int i=0;i<a;i++){
        for(int j=0;j<b;j++){
            r=i&j;

            if(r<k){
                ans++;
            }
        }
    }

    fprintf(output, "Case #%d: %d\n",s,ans);
    ans=0;
    r=0;
}

fclose(input);
fclose(output);
}

