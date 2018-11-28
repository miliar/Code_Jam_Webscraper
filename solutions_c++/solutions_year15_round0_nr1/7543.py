#include<cstdio>
#include<iostream>
#include<string>

using namespace std;

int A[1002];
int partSum[1002];//이전까지 원래있었던 사람수


int main(){
	
	int T, S;
	scanf("%d", &T);
	FILE* fp=fopen("result.txt", "w");

	for(int test=0; test<T; test++){
		cin>>S;

		string tmp;
		cin>>tmp;
		
		for(int i=0; i<S+1; i++){
			A[i]=((int)tmp[i]-48);
			if(i==0)
				partSum[i]=0;
			else
				partSum[i]=partSum[i-1]+A[i-1];

			//printf("%d\n", partSum[i]);
		}
		
		int invited=0;

		for(int shyness=0; shyness<S+1; shyness++){
			if(shyness==0){
				invited+=0;
			}
			else if(A[shyness]==0){
				invited+=0;
			}
			else{
				if(shyness>=partSum[shyness]+invited){
					invited+=shyness-(partSum[shyness]+invited);
				}
			}
		}
		

		printf("Case #%d:%d\n", test+1, invited);
		fprintf(fp, "Case #%d: %d\n", test+1, invited);
	}

	return 0;
}