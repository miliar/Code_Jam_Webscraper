#include <iostream>
#include <vector>
#include <algorithm>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define N 1001
#define TOL 0.000001


#define max(a,b) ((a) >= (b) ? (a) : (b))
#define min(a,b) ((a) <= (b) ? (a) : (b))

using namespace std;

int mycomp(const void * a, const void * b)
{
   float pa = *(float *) a;
   float pb = *(float *) b;
   
   return (pa > pb) - (pa < pb); 
}


float v[N], u[N];
int a[N];

int main () {

	int t, tst, z, i, j, p, m, n, r, l, vmin, vmax, umin, umax, s1, nr;
	float tol = TOL, x, y;
	
	scanf("%d", &tst);

	for (t = 0; t < tst; t++) {
		scanf("%d", &n);
		
		
		for (i = 0; i < n; i++) 
			scanf("%f", &v[i]);
			
		for (i = 0; i < n; i++) 
			scanf("%f", &u[i]);
		
		
		qsort(v, n, sizeof(v[0]), mycomp);
		qsort(u, n, sizeof(u[0]), mycomp);
		
		
		//deceit war
		s1 = vmin = umin = 0;
		vmax = umax = n-1;
		nr = n;
	
		while (nr > 0){
		
			if (v[vmax] < u[umin]) {
			
				break; //v loses the remaining steps
			}
			
			if (v[vmin] > u[umax]) {
				
				s1 += nr;
				break; //v wins the remaining steps
			}
		
			if ((v[vmin] < u[umin] || v[vmax] < u[umax])){
					    
				//v loses curr step
				vmin++;
				umax--;	
				nr--;	
			}
			
			else { //umin < vmax, vmin< umax, vmin > umin, vmax > umax
				
				vmax--;	
				umax--;
				s1++; //v wins this step
				nr--;
			
			}
		
		}
		
		printf("Case #%d: %d ",t+1, s1);
		
		
		//onest war
		
		s1 = umin = 0;
		umax = n-1;
		
		for (i = 0; i < n; i++) {
			x = v[i];	
			
			if (v[i] < u[umin]) {	
				j = umin;
				umin++;
				y = u[j];
			}
			
			else if (v[i] > u[umax]) {
				j = umin;
				umin++;	
				s1 += n-i;
				y = u[j];
				break;
			
			}
			
			else {
			
				l = umin;
				r = umax+1;
				
				while (l < r) {
					m = (l+r) /2;
					if (x < u[m]) {
						r = m;
					}
					else
						l = m+1;
				}
				
				y = u[l];
				
				if (umax - l < l - umin) {
					for (j = l; j < umax; j++) 
						u[j] = u[j+1];
					umax--;
				}
				
				else {
					for (j = l; j > umin; j--) 
						u[j] = u[j-1];
					umin++;
				}
			}
			
			s1 += (x>y);	
		}
		
		printf("%d\n", s1);
		
	
		
		
	}
	
	
	
	return 0;

}
		

