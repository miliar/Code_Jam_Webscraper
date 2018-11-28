#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;
int isPalindrome(long x){
	long rev = 0;
	long num = x;
	while(x>0){
		rev = rev*10 + x%10;
		x = x/10;
	}
	if(rev == num){
		return 1;
	}
	return 0;
}

int main(){
	
	long sqr = sqrt(100000000000000);
	vector<long> v;
	for(long i=1;i<=sqr;i++){
		if( isPalindrome(i) && isPalindrome(i*i)){
			v.push_back(i*i);	
		}
	
	
	}

	int testCases;
	scanf("%d",&testCases);
	for(int t=1;t<=testCases;t++){
		
		long A, B;
		scanf("%ld%ld",&A,&B);
		int count = 0;
		
		for(int i=0;i<v.size();i++){
			if(v[i] > B)
				break;
			if(v[i] >= A && v[i] <=B){
				count++;
			}	
		
		}
		printf("Case #%d: %d\n",t,count);
	}	
}
