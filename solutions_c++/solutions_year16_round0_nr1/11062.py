#include<iostream>
#include<cmath>
using namespace std;
int T,count=0,arr[10][2];
long long int N;
void del(int a){
	count=0;
	while(a!=0){
		int k=a%10;
		arr[k][1]=0;
		a=a/10;
	}
	for(int m=0;m<10;m++){
		if(arr[m][1]==0)
			count++;
	}

}
int main(){
	int j=1;
	for(int i=0;i<10;i++){
		arr[i][0]=i;
	}
	cin>>T;
	if(T>=1 && T<=100){
	for(int m=0;m<T;m++){
		cin>>N;
		if(N>=0 && N<=pow(10,6)){
		j=0;
		for(int l=0;l<10;l++){
			arr[l][1]=-1;
		}
		count=0;
		if(N==0)
			cout<<"Case #"<<m+1<<": INSOMNIA\n";
		else{
			while(count!=10){
				del(j*N);
				j++;
			}
			cout<<"Case #"<<(m+1)<<": "<<(j-1)*N<<"\n";
		}
	}    }
   }
}
