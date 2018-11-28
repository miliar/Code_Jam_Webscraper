#include<iostream>
#include<cstring>

using namespace std;

bool mark[10];

void check(int x){
	while(x){
		mark[x%10]=true;
		x/=10;
	}
	return;
}

int main(){
	int t;
	cin>>t;
	for(int l=1;l<=t;l++){
		memset(mark,0,sizeof(mark));
		int n;
		cin>>n;
		if(n==0){
			cout<<"Case #"<<l<<": INSOMNIA"<<endl;
			continue;
		}
		for(int i=1;i<=1000;i++){
			check(i*n);
			int cnt=0;
			for(int j=0;j<10;j++)if(mark[j])cnt++;
			if(cnt==10){
				cout<<"Case #"<<l<<": "<<i*n<<endl;
				break;
			}
		}
	}
	return 0;
}
