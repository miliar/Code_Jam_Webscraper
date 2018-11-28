#include <iostream>
#include <stdlib.h>

using namespace std;

int main(void){

FILE *input, *output;
input = fopen("A-small-attempt1.in", "r");
output = fopen("output.txt", "w");

int t;
int r1, r2;
int test, test2;

int c[4][4], c2[4][4];
fscanf (input, "%d", &t);

for(int i=0; i<t; i++){ ////////////t

test=0;

fscanf (input, "%d", &r1);
for(int j=0; j<4; j++){
for(int k=0; k<4; k++){
fscanf (input, "%d", &c[j][k]);
}}

fscanf (input, "%d", &r2);
for(int j=0; j<4; j++){
for(int k=0; k<4; k++){
fscanf (input, "%d", &c2[j][k]);
}}

for(int j=0; j<4; j++){
for(int k=0; k<4; k++){

if(c[r1-1][j]==c2[r2-1][k]){ 
test2=c[r1-1][j];
test=test+1;
}


}}
if(test==1)fprintf(output, "Case #%d: %d\n", i+1, test2);
if(test>1)fprintf(output, "Case #%d: Bad magician!\n", i+1);
if(test==0)fprintf(output, "Case #%d: Volunteer cheated!\n", i+1);


}///////////////////t
fclose(input);
fclose(output);
return 0;
}
