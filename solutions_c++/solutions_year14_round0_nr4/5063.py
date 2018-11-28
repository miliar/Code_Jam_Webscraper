#include <iostream>
#include <cstdio>
#include <deque>
#include <algorithm>
#define MAX 1005
using namespace std;

double C[MAX];
double D[MAX];

deque<double> A,B;

int main(){
	FILE* o = fopen("ansD.txt","w");
	int T,N,i,s=0,j,ans1,ans2;
	scanf("%d",&T);
while(T--){
	scanf("%d",&N);
	s++;
	ans1=0;
	ans2=0;
	for(i=0;i<N;i++){
		scanf("%lf",&C[i]);
		A.push_back(C[i]);
	}
		
	for(i=0;i<N;i++){
		scanf("%lf",&D[i]);
		B.push_back(D[i]);
	}
	sort(A.begin(),A.end());
	sort(B.begin(),B.end());
	sort(D,D+N);
	sort(C,C+N);

	int f1=0,f2=0;
	for(i=N-1;i>=f1;)
	for(j=N-1;j>=f2;){
		if(C[i]>D[j]){
			i--;
			f2++;	
			ans2++;
		}
		else{
			i--;
			j--;
		}
	}

	while(!A.empty()){
		if(A.back()>B.back()){
			ans1++;
			A.pop_back();
			B.pop_back();		
		}
		else{
			A.pop_front();
			B.pop_back();
		}

	}	

	fprintf(o,"Case #%d: %d %d\n",s,ans1,ans2);
	
	
}


return 0;
} 
