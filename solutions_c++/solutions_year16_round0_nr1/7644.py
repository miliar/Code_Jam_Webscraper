#include <iostream>
#include <cstring>

using namespace std;

int seen[10];

bool isAllSeen(){
	for(int i=0;i<10;i++){
		if(seen[i]==0) return false;
	}
	return true;
}

void updateSeen(unsigned long long num){
	while(num>0){
		seen[num%10] = 1;
		num /= 10;
	}
}

int main(){
	int t,c=1;cin>>t;
	unsigned long long n;
	while(c<=t){
		memset(seen, 0, sizeof(seen));
		cin>>n;
		if(n<1) cout<<"Case #"<<c<<": INSOMNIA"<<endl;
		else{
			int i = 1;
			while(!isAllSeen()){
				updateSeen(i*n);
				i++;
			}
			if(isAllSeen()) cout<<"Case #"<<c<<": "<<(i-1)*n<<endl;
			else cout<<"Case #"<<c<<": INSOMNIA"<<endl;
		}
		c++;
	}
	return 0;
}