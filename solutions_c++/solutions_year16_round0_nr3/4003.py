#include <cstdio>
#include <bitset>
#include <string>
#include <cmath>
#define T 1
#define N 16
#define J 50
long long int divisor(long long int n);
long long int* interpret(int n);

int main(){
	const int start=(1<<(N-1))+1;
	const int end=(1<<N)-1;
	int found=0;
	printf("Case #%d:\n",T);
	for(int current=start;current<=end;current+=2){
		const long long int* value=interpret(current);
		if(value!=NULL){
			printf("%s",std::bitset<N>(current).to_string().c_str());
			for(int base=2;base<=10;base++){
				printf(" %d",value[base]);
			}
			puts("");
			found++;
			if(found==J){
				return 0;
			}
		}
	}
}

long long int divisor(long long int n){
	for(long long int i=2;i<=sqrt(n+1);i++){
		if(n%i==0){
			return i;
		}
	}
	return -1;
}

long long int power(int base, int j){
	long long int result=1LL;
	if(j==0){
		return result;
	}else{
		for(int i=0;i<j;i++){
			result*=(long long int)base;
		}
	}
	return result;
}

long long int* interpret(int n){
	long long int* value=new long long int[11];
	const std::string binary=std::bitset<N>(n).to_string();
	for(int base=2;base<=10;base++){
		long long int sum=0;
		for(int i=binary.size()-1,j=0;i>=0;i--,j++){
			if(binary[i]=='1'){
				sum+=power(base,j);
			}
		}
		const long long int v=divisor(sum);
		value[base]=v;
		if(v==-1){
			delete[] value;
			return NULL;
		}
	}
	return value;
}