#include <stdio.h>
#include <deque>
#include <stdlib.h>
#include <algorithm>
#include <iostream>

using namespace std;

void war(int x, deque<float> ken, deque<float> naomi){

	sort(ken.begin(),ken.end());
	sort(naomi.begin(),naomi.end());

	int cont=0;

	for(int i=0; i<x; i++){
		if(naomi.front() > ken.front()){
			naomi.pop_back();
			ken.pop_front();
			cont++;
		}else{
			naomi.pop_front();
			ken.pop_front();
		}
			
	}
	
	printf("%d\n",cont);

}

void dwar(int x, deque<float> ken, deque<float> naomi){

	sort(ken.begin(),ken.end());
	sort(naomi.begin(),naomi.end());


	int cont=0;

	for(int i=0; i<x; i++){
		if(naomi.front() > ken.front()){
			naomi.pop_front();
			ken.pop_front();
			cont++;
		}else{
			naomi.pop_front();
			ken.pop_back();
		}
			
	}
	
	printf("%d ",cont);

}


int main(){

int T, n=0;
scanf("%d\n",&T);

while(n++<T){
	printf("Case #%d: ",n);

	int x;
	scanf("%d\n",&x);

	deque<float> naomi;
	deque<float> ken;

	for(int i=0; i<x; i++){
		float a;
		scanf("%f", &a);
		naomi.push_back(a);
	}

		for(int i=0; i<x; i++){
		float a;
		scanf("%f", &a);
		ken.push_back(a);
	}

	dwar(x,ken,naomi);

	war(x,ken,naomi);
	
}


return 0;
}
