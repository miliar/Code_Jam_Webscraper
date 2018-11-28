#include <string.h>
#include <stdio.h>
#include <iostream>
#include <map>
#include <vector>
#include <algorithm>

#define N 4

using namespace std;

char b[N][N+3];

int main() {

int tst, n=N, i, j, k, t, c, nmax, nb, f = 0, x=0, o=0, no, nx;
char a;

scanf("%d\n", &tst);
for (c=0; c<tst; c++) {
  f = 0;
  x = o = 0;
  for (i=0; i<n; i++) 
  	scanf("%s", b[i]);
  
  for (i=0; i<n; i++) {
  	no = nx = t = 0 ;
  	for (j=0; j<n; j++){
		a = b[i][j];
		if (a == 'T')
			t = 1;
		else if (a == 'O')
			no++;
		else if (a == 'X')
			nx++;
		else f = 1;
  	}
 
  	//cout <<nx<<" "<<no<<" "<<t<<" "<<f<<" "<<c+1<<endl;	
  	if ((nx+t) == n) {
  		x = 1; 
  		break;
  	}
  	else if ((no+t) == n) {
  		o = 1; 
  		break;
  	}
  }
  
 
  
  if (!x && !o) {
  	for (i=0; i<n; i++) {
	  	no = nx = t = 0 ;
	  	for (j=0; j<n; j++){
			a = b[j][i];
			if (a == 'T')
				t = 1;
			else if (a == 'O')
				no++;
			else if (a == 'X')
				nx++;
			else 
				f = 1;
	  	}
	  	
	  	//cout <<nx<<" "<<no<<" "<<t<<" "<<f<<" "<<c+1<<endl;	
	  	if (nx+t == n) {
	  		x = 1; 
	  		break;
	  	}
	  	else if (no+t == n) {
	  		o = 1; 
	  		break;
	  	}
	  }
  }
  	
  if (!x && !o) {
  	no = nx = t = 0 ;
  	for (i=0; i<n; i++) {
			a = b[i][i];
			if (a == 'T')
				t = 1;
			else if (a == 'O')
				no++;
			else if (a == 'X')
				nx++;
			else 
				f = 1;
	  	}
	  	//cout <<nx<<" "<<no<<" "<<t<<" "<<f<<" "<<c+1<<endl;	
	  	if (nx+t == n) {
	  		x = 1; 
	  	}
	  	else if (no+t == n) {
	  		o = 1; 
	  	}
   }
   
   if (!x && !o) {
  	no = nx = t = 0 ;
  	for (i=0; i<n; i++) {
			a = b[i][n-i-1];
			if (a == 'T')
				t = 1;
			else if (a == 'O')
				no++;
			else if (a == 'X')
				nx++;
			else 
				f = 1;
	  	}
	  //cout <<nx<<" "<<no<<" "<<t<<" "<<f<<" "<<c+1<<endl;	
	  	if (nx+t == n) {
	  		x = 1; 
	  	}
	  	else if (no+t == n) {
	  		o = 1; 
	  	}
   }
   
   if (x)
   	printf("Case #%d: X won\n", c+1);
   else if (o)
   	printf("Case #%d: O won\n", c+1);
   else if (!x && !o && !f)
   	printf("Case #%d: Draw\n", c+1);
   else 
   	printf("Case #%d: Game has not completed\n", c+1);  	
  }
  
return 0;

} 
