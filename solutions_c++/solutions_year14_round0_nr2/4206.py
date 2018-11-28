#include <stdio.h>
#include <iostream>
#include <math.h>
#include <vector>
#include <utility>
#include <algorithm>
#include <string>
#include <set>

using namespace std;

int main() {
    freopen("B-large.in", "r",stdin);
    freopen("output.txt", "w",stdout);
    int n,k=1;
    scanf("%d",&n);
    while(n--){
		
		double c,f,x,t,p=2,aux=0,co;
		scanf("%lf %lf %lf",&c,&f,&x);
		t=x/p;
		if(x>c){
		while(true){
			aux+=c/p;
			p+=f;
			co=aux+x/p;
			if(t>co)
				t=co;
				else
				break;
			}
		}
		
		printf("Case #%d: %.07lf\n",k,t);	
		k++;
	}
   
} 
