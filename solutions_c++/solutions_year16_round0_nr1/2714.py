#include<stdio.h>

#include<vector>
using namespace std;
int main(){
int N, T;


  freopen ("A-large.in","r",stdin);
  freopen("A_large_output", "w", stdout);

//Getting number of times
	scanf("%d", &T);


//For each number
for(int t=1;t<=T;t++){

	scanf("%d", &N);
	
	if(N==0){
		printf("Case #%d: INSOMNIA\n",t);
		continue;
	}

	bool check[10]={0};
	int Norig = N;
	
	for(int mult=1;;mult++){
	
		N = mult* Norig;	
		//printf("Number: %d\n", N);

		//converting into digits
		vector<int> digits;

		for(int temp=N;temp>0;temp/=10){
			digits.push_back(temp%10);
		}

		/*//Test printing digits
		for(int i=0;i<digits.size();i++){
			printf("%d ", digits[i]);
		}
		printf("\n");
		*/

		for(int i=0;i<digits.size();i++){
			check[digits[i]]=1;
		}

		bool test=1;
		for(int i=0;i<10;i++){
			test=check[i];
			if(!test) break;
		}
		
		if(test){
			printf("Case #%d: ",t);
			for(int i=digits.size()-1;i>=0;i--){
				printf("%d", digits[i]);
			}
			printf("\n");
			break;
		}	
		//Multiplying N

		/*//Test printing check array
		for(int i=0;i<10;i++){
			printf("%d ", check[i]);
		}
		printf("\n");*/
	}
	  

}

return 0;
}