/*
ID: jesusvillegon
LANG: C++
TASK: Magic Trick
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

using namespace std;

int x,y,T, i,j, cad[20],pos,rep,op,act,num;

int main() {

FILE *s = fopen( "A-small-attempt1.in","r");
FILE *sa = fopen( "A-small-attempt1.out","w");

fscanf(s,"%d",&y);

for(x=0; x<y; x++) {

memset(cad,0,sizeof(cad));

fscanf(s,"%d",&op);
for(i=0; i<4; i++){
for(j=0; j<4; j++){
  fscanf(s,"%d",&act);
  if(i+1 == op) {
     cad[act] ++;
  }
  
}
}

fscanf(s,"%d",&op);
for(i=0; i<4; i++){
for(j=0; j<4; j++){
  fscanf(s,"%d",&act);
  if(i+1 == op) {
     cad[act] ++;
  }
  
}
}

pos = num = 0;

for(i=1; i<=16; i++) {
  if(cad[i] == 2) {
     pos = i;
     num++;
  }
}

if(num == 1) {fprintf(sa,"Case #%d: %d\n",x+1,pos);}
else if(num == 0)  {fprintf(sa,"Case #%d: Volunteer cheated!\n",x+1);}
else if(num > 1)  {fprintf(sa,"Case #%d: Bad magician!\n",x+1);}




}





fclose(s);
fclose(sa);


return 0;
}

