#include<iostream>
#include<string.h>
using namespace std;
int num[10],r=0;

bool check(int n){
	while(n>0){
		if(!num[n%10]){
			num[n%10]=1;
			r++;
			if(r==10)
				return true;
		}
		n/=10;
	}
	return false;
}

int main(){
//	freopen("a.in","r",stdin);
//	freopen("a.out","w",stdout);
	int ca;
	cin>>ca;
	for(int i=1;i<=ca;i++){
		int n;
		cin>>n;
		memset(num,0,sizeof(num));
		r=0;
		cout<<"Case #"<<i<<": ";
		if(n==0) cout<<"INSOMNIA"<<endl;
		else{
			int i=1;
			while(!check(i*n)) i++;
			cout<<i*n<<endl;
		}
	}
	return 0;
}
