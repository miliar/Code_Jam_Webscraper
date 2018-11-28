#include <stdio.h>

int l;  
long long x;
int mult [10000][10000];
int part [5];  

int quat[5][5]={{0,0,0,0,0},
                      {0,1,2,3,4},
					  {0,2,-1,4,-3},
					  {0,3,-4,-1,2},
					  {0,4,3,-2,-1}};
  
int multiply  (int a , int b) { 
  if (a < 0 && b < 0)
    return quat[-a][-b];
	
  if (a < 0 && b > 0)
    return -quat[-a][b];
	
  if (b < 0) return -quat[a][-b]; 
  
  return quat[a][b];
}

bool valid (int i1 , int i2) {
  int total = 0;
  bool bi,bj,bk = false;
  
  for (int i = 0; i < 5; i++)
    if (multiply(part[i],mult[0][i1])== 2){
      bi = true;
      total = i;
      break;
	} 
	
  for (int i = 0; i < 5; i++)
    if (multiply(mult[i2][l-1],part[i])== 4){
      bk = true;
      total += i;
      break;
	}	
    
  if (!bi || !bk) return false;
  
  int left=1;
  int right=1;
  
  if (i1 != l-1)
    left = mult[i1+1][l-1];

   if (i2 > 0)
     right = mult[0][i2-1];
     
  //case1
  if (i1+1 < i2){
  	bj = (mult[i1+1][i2-1]== 3);
  	
  	if (bj && total + 1 <= x && ((x-1)%4 == total%4)) return true;
  }
  
  //case 2
  for (int i = 0; i < 5; i++)
    if (multiply(multiply(left,part[i]),right) == 3){
      bj=true;
      total += i;
      break;
	}
  
  return (bj && total + 2 <= x && ((x-2)%4 == total%4));
}

bool solution () {
  for (int j=0; j < l; j++)  
     if (multiply(part[0],mult[0][j])== 2 || multiply(part[1],mult[0][j])== 2 || multiply(part[2],mult[0][j])== 2 
	    || multiply(part[3],mult[0][j])== 2 || multiply(part[4],mult[0][j])== 2){
	  for (int k=l-1; k >= 0; k--) {
	  	if (valid(j,k)){	  		
	  	  return true;
		} 	  	  
	}
   }
  return false;
}


int main () {
  int t;        
  
  FILE* fin = fopen("C-large.in","r");
  FILE* fout = fopen("c.out","w"); 
  
  fscanf (fin,"%d",&t);
  
  for (int i=1; i <= t; i++) {
    fscanf (fin,"%d %I64d\n",&l,&x);	
    
	for (int j=0; j < l; j++) {
      char c;
      fscanf (fin,"%c",&c);
      mult[j][j] = c - 'i' + 2;            
	}
	
	for (int j=0; j < l; j++)
	  for (int k=j+1; k < l; k++)
	    mult[j][k] = multiply (mult[j][k-1],mult[k][k]);

   part[0] = 1;
   part[1] = mult[0][l-1];
   part[2] = multiply (part[1],part[1]);
   part[3] = multiply (part[2],part[1]);
   part[4] = multiply (part[3],part[1]);         
	    
   if (solution())     
     fprintf (fout,"Case #%d: YES\n",i);
   else 
     fprintf (fout,"Case #%d: NO\n",i);   	    	        
  }                                
  
  fclose (fin);
  fclose (fout);
  
  return 0;
}
