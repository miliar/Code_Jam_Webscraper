#include <iostream>
#include <cstdio>
using namespace std;

bool visited[10];
int cnt=10;
long long getLastNumber(long long n){
	long long val;
	for(int i=1;;i++){
		val = i*n;
		if (val<=0){
			return -1;
		}
		while(val>0){
			int tmp=val%10;
			if(!visited[tmp]){
				visited[tmp]=true;
				cnt--;
			}
			val/=10;
		}
		if(cnt==0){
			return i*n;
		}

	}
	return -1;
}
int main(){
	freopen("in.txt","r",stdin);
	long long T,N;
	cin>>T;
	for(long long i=0;i<T;i++){
		cin>>N;
		for(long long j=0;j<10;j++){ 
			visited[j]=false;
		}
		cnt=10;
		cout<<"Case #"<<i+1<<": ";
		long long result = getLastNumber(N);
		if(result<=0){
			cout<<"INSOMNIA";
		}else{
			cout<<result;
		}
		cout<<endl;
	}
	return 0;
}