#include<bits/stdc++.h>
using namespace std;

long long int convert(long long int a){
	long long int sum=0,i=1,rem;
	do{
		rem=a%2;
		sum=sum+rem*i;
		a=a/2;
		i=i*10;
	}while(a>0);
	return sum;
}

long long int base(long long int a,int b){
	long long int xyz=0,i,temp;
	for(i=0;a!=0;i++){
		temp=a%10;
		xyz=xyz+pow(b,i)*temp;
		a=a/10;
	}
	return xyz;
}

long long int prime(long long int a){
	long long int i;
	for(i=2;i*i<=a;i++){
		if(a%i==0)
			return 0;
	}
	return 1;
}

long long int div(long long int a){
	long long int i;
	for(i=2;i<a;i++){
		if(a%i==0)
			return i;
	}
}

int main(){
	long long int t,n,jam_count,k,i,j,jamcoin[9],temp,num;
	int d,c=0;
	FILE *ip, *op;
	ip=fopen("C-small-attempt0.in","r");
	if(ip==NULL){
		printf("error!!");
		exit(0);
	}
	op=fopen("output.txt","w");
	if(op==NULL){
		printf("error!!");
		exit(0);
	}
	fscanf(ip,"%lld",&t);
	while(t--){
		fscanf(ip,"%lld %lld",&n,&jam_count);
		fprintf(op,"Case #1:\n");
		for(i=0;i<pow(2,n-2);i++){
			int flag=0;
			temp=convert(i);
			num=10*(pow(10,n-2)+temp)+1;
			for(j=0;j<=8;j++){
				jamcoin[j]=base(num,j+2);
				if(prime(jamcoin[j])==1){
					flag=1;
					break;
				}
			}
			
			if(flag==0){
				if(c==jam_count)
					break;
				fprintf(op,"%lld ",num);
				for(k=0;k<9;k++){
					d=div(jamcoin[k]);
					fprintf(op,"%lld ",d);
				}
				fprintf(op,"\n");
			c++;
			}
		}
	}
return 0;
}
