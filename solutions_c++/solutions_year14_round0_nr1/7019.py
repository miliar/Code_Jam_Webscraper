#include <stdio.h>

int N;
int firstRow;
int secondRow;
int a[4], b[4], t[4];


int main ()
{
  FILE * in;
  FILE * out;

  in = fopen ("A-small-attempt0.in","r");
  out = fopen("output.txt","w");


  fscanf(in,"%d",&N);
  for(int i=0; i<N; i++){
    fscanf(in,"%d",&firstRow);
      firstRow--;   
    for(int j=0; j<4; j++){
      if(j == firstRow){
        fscanf(in,"%d %d %d %d",a,a+1,a+2,a+3); 
      } else {
        fscanf(in,"%d %d %d %d",t,t+1,t+2,t+3); 
      }
    }

    fscanf(in,"%d",&secondRow);
      secondRow--;   
    for(int j=0; j<4; j++){
      if(j == secondRow){
        fscanf(in,"%d %d %d %d",b,b+1,b+2,b+3); 
      } else {
        fscanf(in,"%d %d %d %d",t,t+1,t+2,t+3); 
      }
    }

    int numOfClashes = 0;
    int clash;
    for(int j=0; j<4; j++){
      for(int k=0; k<4; k++){
        if(a[j] == b[k]){
          numOfClashes++;
          clash = a[j];
        }
      }
    }

    fprintf(out,"Case #%d: ", i+1);
    switch(numOfClashes){
      case 0: fprintf(out,"Volunteer cheated!\n"); break;
      case 1: fprintf(out,"%d\n",clash); break;
      default: fprintf(out,"Bad magician!\n"); break;
    }

    //printf("%d %d %d %d\n",a[0],a[1],a[2],a[3]);
    //printf("%d %d %d %d\n",b[0],b[1],b[2],b[3]);
  }

  fclose(in);
  fclose(out);

  /*
  char str [80];
  float f;
  
  


  fprintf (pFile, "%f %s", 3.1416, "PI");
  rewind (pFile);
  fscanf (pFile, "%f", &f);
  fscanf (pFile, "%s", str);
  fclose (pFile);
  printf ("I have read: %f and %s \n",f,str);
  */
  return 0;
}