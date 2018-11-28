#include<bits/stdc++.h>
using namespace std;
long long int check_prime(long long int x){
	long long int i;
	for(i=2;i*i<=x;i++){
		if(x%i==0)
			return 0;
	}
	return 1;
}

//working
long long int base(long long int x,int b){
	long long int converted=0,i,temp;
	for(i=0;x!=0;i++){
		temp=x%10;
		converted=converted+pow(b,i)*temp;
		x=x/10;
	}
	return converted;
}

long long int binary_convert(long long int x){
	long long int sum=0,i=1,rem;
	do{
		rem=x%2;
		sum=sum+rem*i;
		x=x/2;
		i=i*10;
	}while(x>0);
	return sum;
}

long long int divisior(long long int x){
	long long int i;
	for(i=2;i<x;i++){
		if(x%i==0)
			return i;
	}
}

int main(){
	long long int t,n,jam,k,i,j,jamcoin[9],temp,num;
	int count=0;
	FILE *input, *output;
	input=fopen("C-small.in","r");
	if(input==NULL){
		printf("ERROR");
		exit(0);
	}
	output=fopen("output.txt","w");
	if(output==NULL){
		printf("ERROR");
		exit(0);
	}
	fscanf(input,"%lld",&t);
	while(t--){
		fscanf(input,"%lld %lld",&n,&jam);
		fprintf(output,"Case #1:\n");
		for(i=0;i<pow(2,n-2);i++){
			int flag=0;
			temp=binary_convert(i);
			num=10*(pow(10,n-2)+temp)+1;
			for(j=0;j<=8;j++){
				jamcoin[j]=base(num,j+2);
				if(check_prime(jamcoin[j])==1){
					flag=1;
					break;
				}
			}
			if(flag==0){
				if(count==jam)
					break;
				fprintf(output,"%lld ",num);
				for(k=0;k<9;k++){
					int d=divisior(jamcoin[k]);
					fprintf(output,"%lld ",d);
				}
				fprintf(output,"\n");
			count++;
			}
		}
	}
return 0;
}
