#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>


using namespace std;

int compare (const void * a, const void * b)
{
  return ( *( long long*)a - *(long long *)b );
}

int main()
{
	FILE * fin;
    FILE * fout;


	fin=fopen("A-small.in","r");
	fout=fopen("A-small.out", "w");
	
    long long  myMote = 0;
    long long myMoteTemp = 0;
    
    int tmpCount =0;
    
    int numMotes = 0;
    long long motes[100] = {0};
      
    int num = 0 ;
	int iter = 0 ;
    
    //printf("%d \n" , sizeof(long));
	//printf("%d", sizeof(long long));
	fscanf(fin,"%d\n", &iter);
	
	printf("%d\n", iter);

	
	for(int j=0;j<iter;j++) {
            
      for (int i=0; i < 100 ;i++)
      {
          motes[i] = 0 ;
          
      }
      
      num = 0;
      myMote = 0;
      numMotes = 0;
            
      fscanf(fin, "%lld %d\n", &myMote, &numMotes);
      printf("%lld %d\n", myMote, numMotes);
      
      for (int i=0; i < numMotes ;i++)
      {
          fscanf(fin, "%lld ", &motes[i]);
          printf("%lld ", motes[i]);
          
      }
      
     printf("\n\n");
     
     qsort (motes, numMotes, sizeof(long long), compare);
     
     for (int i=0; i < numMotes ; i++) {
         
         printf("%lld ", motes[i]);
         
         }
         
         printf("Up Sorted\n\n");
         
     for (int i=0; i < numMotes ; i++)
      {
          
         myMoteTemp = 0;
         tmpCount = 0;
         
         if ( motes[i] < myMote ) {
              
              myMote += motes[i] ;
              
              continue;              
              
         }
         else {           //if ((motes[i] - myMote + 1) < myMote) {
              
              myMoteTemp = myMote;
              
              
              if(myMoteTemp >= 2) {
              while (motes[i] >= myMoteTemp ){
                      
                        
              //if(myMoteTemp -1 <= 100){           
              myMoteTemp += (myMoteTemp - 1);
             /* }
              else {
              myMoteTemp += 100;
              }*/
              
                           
              tmpCount++;
              }
              
                            
              if(tmpCount < (numMotes - i)){
                          
                          myMote = myMoteTemp;
                          myMote += motes[i]; 
                          num += tmpCount;
                          continue;
                          
              }
              
              }
              
              
         }
         
         
         num++;     
         
              
      }
      
      printf("Pergjigja : %d\n\n", num);
     	    
	  fprintf(fout,"Case #%d: %d\n", j+1, num);
	 
	}

    system("PAUSE");
	fclose(fin);
	fclose(fout);

	return 0;
}

