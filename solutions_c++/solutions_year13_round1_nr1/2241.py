#include<stdio.h>
#include<stdlib.h>
#include<conio.h>
# define PI 3.14

  
 


 

	FILE * in;
	FILE * out;
	int T;
	unsigned long long int s,r,t,nbRing;

 main(){
 	 
	


	
	in=fopen("A-small-1.in","r");
	out=fopen("A-small-1.out","w");
	//if( (in!=NULL) && (out!=NULL) )
	fscanf(in,"%i\n",&T);

	
       
    for(int i=0;i<T;i++){
    	fscanf(in,"%llu %llu\n",&r,&t);
    	printf("%llu %llu\n\n",r,t);
    
       nbRing=0;
       s=(r+1)*(r+1)-r*r;
       while(t >=s){
       	nbRing++;
       	t=t-s;
       	r=r+2;
       	s=(r+1)*(r+1)-r*r;
      }
    
    		
    		fprintf(out,"Case #%i: %llu\n",i+1,nbRing);
            printf("Case #%i: %llu\n",i+1,nbRing);
  	
    }    
	

 }


//************************* 


//  
   







/*
int maxInMatrix(int maxPrec){
	int maxCour=-1;
	
	for(int i=0;i<N;i++){
		for(int j=0;j<M;j++){
			if( (matrix[i][j] < maxPrec) && (maxCour <= matrix[i][j]) ){
			 maxCour=matrix[i][j];
			 	
			}
			
		}
		
		
		
	}
	
	return maxCour;
	
}
//******************
int maxLine(int indexLine){
	int max=0;
	for(int j=0;j<M;j++){
		if(matrix[indexLine][j]>max){
			max=matrix[indexLine][j];
		}
	}
	return max;
}
//ù********************
int maxColumn(int indexComlumn){
	int max=0;
	for(int i=0;i<N;i++){
		if(matrix[i][indexComlumn]>max){
			max=matrix[i][indexComlumn];
		}
	}
	return max;
}
// is possible to build ?

 int  isPossible(int max){
	int maxPrec=maxInMatrix(max);
	while(maxPrec>=0){
	for(int i=0;i<N;i++){
		for(int j=0;j<M;j++){
			if(matrix[i][j]==maxPrec){
				if(matrix[i][j]< maxColumn(j) && matrix[i][j]< maxLine(i)){
					return 0;
					
				}
			}
		}
		
	}
	maxPrec=maxInMatrix(maxPrec);
	
	
	
	}
	  return 1;
	
	}








 
 //*************************************************
     int isNoCompleted(){
        
        for(int i=0;i<4;i++)
        { for(int j=0;j<4;j++){
          if( matrix[i][j]=='.'){
               return 1;
           }
         }
        
        } 
       return 0;
     
    }
  //********************************************  
    int whoWon(char symbole){
      
      int xNumber=0;
      int tNumber=0;
      
     
      
      //searching in matrix
         for(int i=0;i<4;i++)
        { for(int j=0;j<4;j++){
          if(matrix[i][j]==symbole) {xNumber++;}
           
          if(matrix[i][j]=='T'){tNumber++;}
     
         }
        
        if((xNumber==4)|| (xNumber==3 && tNumber==1)){
                      return 1;}
       xNumber=0;
       tNumber=0;
    
      }
         
       //searching in columns
       xNumber=0;
       tNumber=0;
       for(int i=0;i<4;i++)
        {  for(int j=0;j<4;j++){
           if(matrix[j][i]==symbole) {xNumber++;}
           if(matrix[j][i]=='T') {tNumber++;}
     
          }
        
        if((xNumber==4)|| (xNumber==3 && tNumber==1)){
                      return 1;
					   }
       xNumber=0;
       tNumber=0;
    
        }
        
         //searching in diag 1
       xNumber=0;
       tNumber=0;
       for(int i=0;i<4;i++){
        
          if(matrix[i][i]==symbole){xNumber++;}
          if(matrix[i][i]=='T'){tNumber++;}
     
         }
        
        if((xNumber==4)|| (xNumber==3 && tNumber==1)){
                      return 1; 
					  }
       
         //searching in diag 2
       xNumber=0;
       tNumber=0;
       for(int i=0;i<4;i++){
        
          if(matrix[i][3-i]==symbole) {xNumber++;}
          if(matrix[i][3-i]=='T') {tNumber++;}
     
         }
        
        if((xNumber==4)|| (xNumber==3 && tNumber==1)){
                      return 1;
					   }
        
    
     
     return 0;
  }//end of whoWon
    
    
    //*************************************
     void gameStat(int i){
     if(whoWon('X')){
     
         fprintf(out,"Case #%i: X won\n",i+1);
    }
     else {
		    if(whoWon('O')==1){
		     
		         fprintf(out,"Case #%i: O won\n",i+1);
		     }
		     else{
		            if(isNoCompleted()==1){
		              fprintf(out,"Case #%i: Game has not completed\n",i+1);
		             }
		             else {
		                  fprintf(out,"Case #%i: Draw\n",i+1);
			              }
		      
		      
		         }
        }
    
    }
 
 */
