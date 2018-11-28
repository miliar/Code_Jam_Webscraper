#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<string>
#include<cstring>
#include<map>
#include<algorithm>
#include<vector>
#include<queue>
using namespace std;
typedef long long ll;
bool used[10];
void addDigits(int n){
	while(n) {
		used[n%10] = 1;
		n/=10;
	}
}
bool allUsed(){
	for(int i=0;i<10;++i) {
		if(!used[i])
			return false;
	}
	return true;
}
void deal() {
	int n;
	cin>>n;
	memset(used, 0, sizeof(used));
	if(n==0) {
		cout<<"INSOMNIA"<<endl;
		return;
	}
	int tmp = 0;
	while(!allUsed()) {
		tmp+=n;
		addDigits(tmp);
	}
	cout<<tmp<<endl;
}
void openFile() {
	freopen("A-large.out","w", stdout);
	freopen("A-large.in","r",stdin);
}
int main() {
	int t;
	openFile(); 
	cin>>t;
	for(int i=0;i<t;++i) {
		cout<<"Case #"<<i+1<<": ";
		deal();
	}
}