#include <iostream>
#include <stdlib.h>
#include <string.h>

using namespace std;

int main(){

FILE *input, *output;
input = fopen("D-small-attempt2.in", "r");
output = fopen("output.txt", "w");

int t;
fscanf (input, "%d", &t);

int x, r, c;
for(int i=0; i<t; i++){

fscanf (input, "%d", &x);
fscanf (input, "%d", &r);
fscanf (input, "%d", &c);
////////////////////////////////////////////////////////////////////////////////////////

//x==1

if(x==1 && r==1 && c==1)fprintf(output, "Case #%d: GABRIEL\n", i+1);
if(x==1 && r==1 && c==2)fprintf(output, "Case #%d: GABRIEL\n", i+1);
if(x==1 && r==1 && c==3)fprintf(output, "Case #%d: GABRIEL\n", i+1);
if(x==1 && r==1 && c==4)fprintf(output, "Case #%d: GABRIEL\n", i+1);

if(x==1 && r==2 && c==1)fprintf(output, "Case #%d: GABRIEL\n", i+1);
if(x==1 && r==2 && c==2)fprintf(output, "Case #%d: GABRIEL\n", i+1);
if(x==1 && r==2 && c==3)fprintf(output, "Case #%d: GABRIEL\n", i+1);
if(x==1 && r==2 && c==4)fprintf(output, "Case #%d: GABRIEL\n", i+1);

if(x==1 && r==3 && c==1)fprintf(output, "Case #%d: GABRIEL\n", i+1);
if(x==1 && r==3 && c==2)fprintf(output, "Case #%d: GABRIEL\n", i+1);
if(x==1 && r==3 && c==3)fprintf(output, "Case #%d: GABRIEL\n", i+1);
if(x==1 && r==3 && c==4)fprintf(output, "Case #%d: GABRIEL\n", i+1);

if(x==1 && r==4 && c==1)fprintf(output, "Case #%d: GABRIEL\n", i+1);
if(x==1 && r==4 && c==2)fprintf(output, "Case #%d: GABRIEL\n", i+1);
if(x==1 && r==4 && c==3)fprintf(output, "Case #%d: GABRIEL\n", i+1);
if(x==1 && r==4 && c==4)fprintf(output, "Case #%d: GABRIEL\n", i+1);

//x==2

if(x==2 && r==1 && c==1)fprintf(output, "Case #%d: RICHARD\n", i+1);
if(x==2 && r==1 && c==2)fprintf(output, "Case #%d: GABRIEL\n", i+1);
if(x==2 && r==1 && c==3)fprintf(output, "Case #%d: RICHARD\n", i+1);
if(x==2 && r==1 && c==4)fprintf(output, "Case #%d: GABRIEL\n", i+1);

if(x==2 && r==2 && c==1)fprintf(output, "Case #%d: GABRIEL\n", i+1);
if(x==2 && r==2 && c==2)fprintf(output, "Case #%d: GABRIEL\n", i+1);
if(x==2 && r==2 && c==3)fprintf(output, "Case #%d: GABRIEL\n", i+1);
if(x==2 && r==2 && c==4)fprintf(output, "Case #%d: GABRIEL\n", i+1);

if(x==2 && r==3 && c==1)fprintf(output, "Case #%d: RICHARD\n", i+1);
if(x==2 && r==3 && c==2)fprintf(output, "Case #%d: GABRIEL\n", i+1);
if(x==2 && r==3 && c==3)fprintf(output, "Case #%d: RICHARD\n", i+1);
if(x==2 && r==3 && c==4)fprintf(output, "Case #%d: GABRIEL\n", i+1);

if(x==2 && r==4 && c==1)fprintf(output, "Case #%d: GABRIEL\n", i+1);
if(x==2 && r==4 && c==2)fprintf(output, "Case #%d: GABRIEL\n", i+1);
if(x==2 && r==4 && c==3)fprintf(output, "Case #%d: GABRIEL\n", i+1);
if(x==2 && r==4 && c==4)fprintf(output, "Case #%d: GABRIEL\n", i+1);

//x==3

if(x==3 && r==1 && c==1)fprintf(output, "Case #%d: RICHARD\n", i+1);
if(x==3 && r==1 && c==2)fprintf(output, "Case #%d: RICHARD\n", i+1);
if(x==3 && r==1 && c==3)fprintf(output, "Case #%d: RICHARD\n", i+1);
if(x==3 && r==1 && c==4)fprintf(output, "Case #%d: RICHARD\n", i+1);

if(x==3 && r==2 && c==1)fprintf(output, "Case #%d: RICHARD\n", i+1);
if(x==3 && r==2 && c==2)fprintf(output, "Case #%d: RICHARD\n", i+1);
if(x==3 && r==2 && c==3)fprintf(output, "Case #%d: GABRIEL\n", i+1);
if(x==3 && r==2 && c==4)fprintf(output, "Case #%d: RICHARD\n", i+1);

if(x==3 && r==3 && c==1)fprintf(output, "Case #%d: RICHARD\n", i+1);
if(x==3 && r==3 && c==2)fprintf(output, "Case #%d: GABRIEL\n", i+1);
if(x==3 && r==3 && c==3)fprintf(output, "Case #%d: GABRIEL\n", i+1);
if(x==3 && r==3 && c==4)fprintf(output, "Case #%d: GABRIEL\n", i+1);

if(x==3 && r==4 && c==1)fprintf(output, "Case #%d: RICHARD\n", i+1);
if(x==3 && r==4 && c==2)fprintf(output, "Case #%d: RICHARD\n", i+1);
if(x==3 && r==4 && c==3)fprintf(output, "Case #%d: GABRIEL\n", i+1);
if(x==3 && r==4 && c==4)fprintf(output, "Case #%d: RICHARD\n", i+1);

//x==4

if(x==4 && r==1 && c==1)fprintf(output, "Case #%d: RICHARD\n", i+1);
if(x==4 && r==1 && c==2)fprintf(output, "Case #%d: RICHARD\n", i+1);
if(x==4 && r==1 && c==3)fprintf(output, "Case #%d: RICHARD\n", i+1);
if(x==4 && r==1 && c==4)fprintf(output, "Case #%d: RICHARD\n", i+1);

if(x==4 && r==2 && c==1)fprintf(output, "Case #%d: RICHARD\n", i+1);
if(x==4 && r==2 && c==2)fprintf(output, "Case #%d: RICHARD\n", i+1);
if(x==4 && r==2 && c==3)fprintf(output, "Case #%d: RICHARD\n", i+1);
if(x==4 && r==2 && c==4)fprintf(output, "Case #%d: RICHARD\n", i+1);

if(x==4 && r==3 && c==1)fprintf(output, "Case #%d: RICHARD\n", i+1);
if(x==4 && r==3 && c==2)fprintf(output, "Case #%d: RICHARD\n", i+1);
if(x==4 && r==3 && c==3)fprintf(output, "Case #%d: RICHARD\n", i+1);
if(x==4 && r==3 && c==4)fprintf(output, "Case #%d: GABRIEL\n", i+1);

if(x==4 && r==4 && c==1)fprintf(output, "Case #%d: RICHARD\n", i+1);
if(x==4 && r==4 && c==2)fprintf(output, "Case #%d: RICHARD\n", i+1);
if(x==4 && r==4 && c==3)fprintf(output, "Case #%d: GABRIEL\n", i+1);
if(x==4 && r==4 && c==4)fprintf(output, "Case #%d: GABRIEL\n", i+1);

////////////////////////////////////////////////////////////////////////////////////////
}


fclose(input);
fclose(output);
return 0;
}
