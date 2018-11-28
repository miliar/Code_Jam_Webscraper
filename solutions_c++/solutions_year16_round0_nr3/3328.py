#include<cstdio>
#include<fstream>
#include<cmath>
#include<iostream>
using namespace std;
long long T,N,J,coin[32],factors[11],numbers[11],initNum;
int checkPrime(long long num){
	for(long long i=3;i<sqrt(num);++i){
		if(num%i==0) return i;
	}
	return -1;
}
long long pow(long long a,long long b){
	if(b==0){
		return 1;
	}
	else if(b==1){
		return a;
	}
	else if(b%2==0){
		return pow(a,b/2)*pow(a,b/2);
	}
	else{
		return a*pow(a,b-1);
	}
}
int main(){
	
	ifstream fin;
	fin.open("inputC.txt");
	ofstream fout;
	fout.open("outputC.txt");
	
	fin>>T>>N>>J;
	
	initNum=pow(2,N-1)-1;
	
	fout<<"Case #1:"<<endl;
	
	while(J>0){
		initNum+=2;
		for(int i=0;i<32;++i) coin[i]=0;
		for(int i=0;i<11;++i){
			factors[i]=0;
			numbers[i]=0;
		}
		long long tmp=checkPrime(initNum);
		printf("Num: %lld | Prime: %lld\n",initNum,tmp);
		bool fail=false;
		if(tmp==-1) continue;
		else{
			numbers[2]=initNum;
			factors[2]=tmp;
		}
		for(int i=N-1;i>=0;i--){
			if(initNum&(1<<i)) coin[i]=1;
			else coin[i]=0;
		}
		printf("CurCoin: ");
		for(int j=N-1;j>=0;j--){
			printf("%d",coin[j]);
		}
		printf("\n");
		for(long long j=3;j<=10;j++){
			long long tmpNum=0;
			for(long long k=0;k<32;++k){
				if(coin[k]==1){
					tmpNum+=pow(j,k);
				}
			}
			tmp=checkPrime(tmpNum);
			printf("tmpNum: %lld | %lld\n",tmpNum,tmp);
			if(tmp!=-1){
				numbers[j]=tmpNum;
				factors[j]=tmp;
			}
			else{
				fail=true;
				continue;
			}
		}
		if(fail) continue;
		for(int i=N-1;i>=0;i--) fout<<coin[i];
		for(int i=2;i<11;++i) fout<<" "<<factors[i];
		fout<<endl;
		J--;
	}
	
	fin.close();
	fout.close();
	
	system("PAUSE");
	return 0;
}
