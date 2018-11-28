#include<iostream>
#include<string.h>
#include<math.h>
using namespace std;
char str[50];
int num[10];

int pow(int a,int n,int mod){
	int sum=1;
	for(int i=0;i<n;i++){
		sum=sum*a%mod;
	}
	return sum;
}
long long pow(int a,int n){
	long long sum=1;
	for(int i=0;i<n;i++){
		sum=sum*a;
	}
	return sum;
}
bool check(int k,int N){
	if(N<=16){
		long long sum=0, maxn;
		for(long long i=N-1;i>=0;i--){
			if(str[i]==1) 
			sum+=pow(k,i);
		}
		maxn=N>9?11:sqrt(sum)+1;
		for(long long i=2;i<=maxn;i++){
			if(sum%i==0){
				num[k]=i;
				return true;
			}
		}
	}else{
		long long sum=0, maxn;
		for(int i=15;i>=0;i--){
			if(str[i]==1) 
			sum+=pow(k,i);
		}
		for(long long i=2;i<=11;i++){
			if((sum+pow(k,N-1,i))%i==0){
				num[k]=i;
				return true;
			}
		}
	}
	return false;
}
void creatCoinJam(int N,int J){
	int cnt=0;
	for(int i=0;i<(1<<(N-2));i++){
		memset(str,0,sizeof(str));
		str[0]=1;str[N-1]=1;
		int t=i,pos=1;
		while(t>0){
			str[pos++]=t%2;
			t/=2;
		}
		bool found=true;
		memset(num,0,sizeof(num));
		for(int j=2;j<=10;j++){
			if(!check(j,N)){
				found=false;
				break;
			}
		}
		if(found){
			for(int j=N-1;j>=0;j--){
				printf("%d",str[j]);
			}
			for(int j=2;j<=10;j++){
				printf(" %d",num[j]);
			}
			cout<<endl;
			cnt++;
			if(cnt==J){
				return ;
			}
		}
	}
}
int main(){
//	freopen("c.in","r",stdin);
//	freopen("c.out","w",stdout);
	int T;
	cin>>T;
	for(int i=1;i<=T;i++){
		int N,J;
		cin>>N>>J;
		cout<<"Case #"<<i<<":"<<endl;
		creatCoinJam(N,J); 
	}
	return 0;
}
