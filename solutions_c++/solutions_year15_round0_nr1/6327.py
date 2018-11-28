#include <iostream>
#include <stdlib.h>
#include <string.h>

using namespace std;

int main(void){

FILE *input, *output;
input = fopen("A-large.in", "r");
output = fopen("output.txt", "w");

int ip=0; //in piedi
int am=0; //amici

int t;
fscanf (input, "%d", &t);

int n;
char m;
int ci[1000]; //char to int;

for(int j=0; j<t; j++){

fscanf (input, "%d", &n);

for(int i=0; i<n+3; i++){
fscanf (input, "%c", &m);

if(i>0)ci[i-1]=m - '0';

}
/////////////////////////////////////////////////////////////////////////////////////////////

for(int s=0; s<n+1; s++){

if(ip<s){ am+=s-ip; ip+=s-ip; }
if(ip>=s)ip+=ci[s];

}

/////////////////////////////////////////////////////////////////////////////////////////////
fprintf(output, "Case #%d: %d\n", j+1, am);
ip=0;
am=0;
}

fclose(input);
fclose(output);
return 0;
}
