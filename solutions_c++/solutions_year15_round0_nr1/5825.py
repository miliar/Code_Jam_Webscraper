#include<iostream>
#include<cstdio>

int main(){

	int test_cases;
	scanf("%d",&test_cases);
	for(int i=0;i<test_cases;i++){
		int num;
		scanf("%d",&num);
		char input[num+2];
		scanf("%s",input);
		long long int count=0;
		int diff;
		int a = (int)(input[0] - 48);
		for(int j=1;j<=num;j++){
			if(j > a ){
				diff = j - a;
			}
			else{
				diff = 0;
			}
			count+=diff;
			a = ((int)(input[j] - 48)) + a + diff;
		}
		printf("Case #%d: %lld\n",i+1,count);
	}
	return 0;
}
