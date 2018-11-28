#include <stdio.h>
#include <stdlib.h>
#include <string.h>



int totale = 0;


struct s_partito {
  int persone;
  int pos;
} partito;

s_partito persone[1000];

int compare (const void * a, const void * b)
{
  return ( ((s_partito*)b)->persone - ((s_partito*)a)->persone );
}

void togli( int pos ){
    persone[pos].persone--;
    totale--;
    printf("%c", persone[pos].pos + 'A'); 
  
}


//Elabora ogni singolo caso e stampa il risultato senza andare accapo.
void elabora(){
  int partiti;
  scanf("%i",&partiti);
  char tmp;
  int tempvalue;
  for( int i = 0; i < partiti; i++){
    scanf("%d%c", &tempvalue, &tmp); 
    totale += tempvalue;
    persone[i].persone = tempvalue;
    persone[i].pos = i;
    
  }
  
  if( totale % 2 ){
    qsort(&persone, partiti,sizeof(partito),compare);
    persone[0].persone--;
    totale--;
    printf("%c", persone[0].pos + 'A');    
    if(totale)
      printf(" ");

  }
  while( totale) {
     qsort(&persone, partiti,sizeof(partito),compare);
     togli(0);
     qsort(&persone, partiti,sizeof(partito),compare);
     togli(0);
     if(totale)
       printf(" ");
      
  }
}




int main( int argc, char **argv){
	//Legge il numero di casi
	int T = 0;
	scanf("%i",&T);

	for (int i = 1; i <= T; i++){
		printf("Case #%i: ",i);
		elabora();
		printf("\n");
	}

	return 0;
}