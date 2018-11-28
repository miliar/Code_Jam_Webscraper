#include <stdio.h>
#include <math.h>

int N;
double C;
double F;
double X;

double timePassed;
double bestTime;
double rate;
double timeAtThisRate;


int main ()
{
  FILE * in;
  FILE * out;

  in = fopen ("B-large.in","r");
  out = fopen("outputLarge.txt","w");


  fscanf(in,"%d",&N);
  for(int i=0; i<N; i++){
    fscanf(in,"%lf %lf %lf",&C,&F,&X);
    
    rate = 2.0;
    timePassed = 0;
    bestTime = INFINITY;
//   int j=0;
    do{
/*      printf("Round %d",j);
        printf("\tRate: %lf\n",rate);
        printf("\tPassed: %lf\n",timePassed);
        printf("\tBest: %lf\n",bestTime);
*/

      // How long would it take at this rate
      timeAtThisRate = X / rate + timePassed;
      if(timeAtThisRate < bestTime){
        bestTime = timeAtThisRate;
      }
/*      printf("\tAt rate: %lf\n",timeAtThisRate);
        printf("\tNew Best: %lf\n",bestTime);
*/


      // Let's potentionally upgrade farm
      timePassed += C / rate;
      rate += F;

//      j++;
    } while(timePassed < bestTime);

    fprintf(out,"Case #%d: %.7lf\n",i+1,bestTime);
  }

  fclose(in);
  fclose(out);
  return 0;
}