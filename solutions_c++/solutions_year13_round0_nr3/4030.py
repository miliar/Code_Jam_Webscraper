#include<iostream>
#include<cmath>
//#include<fstream>

using namespace std;
long long int A[100],ten=1,k=3;

bool palindrom(long long int i){
	long long int num,len=0,j,B[50];
	num=i;
	while (num>0){
		B[len++]=num%10;
		num/=10;
	}for (j=0;j<len/2;j++){
		if (B[j]!=B[len-j-1])
			break;
	}if (j>=len/2)
		return true;
	return false;
}

int main(){
	long long int n,a,b,i,j,fair=0;
	bool cek=false;
	//freopen("C-large-1.in","r",stdin);
	//freopen("C-large-1.txt","w",stdout);
	A[0]=1;
	A[1]=4;
	A[2]=9;
	for (i=1;i<7;i++){
		ten*=10;
		A[k++]=(2*ten+2)*(2*ten+2);
		if (i%2==0)
			A[k++]=(2*ten+2+sqrt(ten))*(2*ten+2+sqrt(ten));
	}ten=10;
	for (j=1;j<7;j++){
		for (i=ten;i<ten*2;i++){
			if (palindrom(i)){
				cek=palindrom(i*i);
				if (cek)
					A[k++]=i*i;
			}cek=false;
		}ten*=10;
	}cin>>n;
	for (i=0;i<n;i++){
		cin>>a>>b;
		for (j=0;j<k;j++){
			if (A[j]>=a && A[j]<=b)
				fair++;
		}cout<<"Case #"<<i+1<<": "<<fair<<endl;
		fair=0;
	}
}
