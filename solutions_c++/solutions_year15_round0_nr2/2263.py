#include <iostream>
#include <cstring>

using namespace std;

void solve(int zap){
	int korak[1003];
	memset(korak,0,sizeof(korak));
	int n;
	cin >> n;
	for(int i=0;i<n;i++){
		int tr;
		cin >> tr;
		for(int j=1;j<tr;j++){
			int st = tr/j;
			if(tr%j==0)st--;
			korak[j]+=st;
		}
	}
	int ret = 1000000;
	for(int i=1;i<=1000;i++){
		if(i+korak[i]<ret)ret=i+korak[i];
	}
	cout << "Case #" << zap << ": " << ret << "\n";
}


int main(){
	int t;
	cin >> t;
	for(int i=1;i<=t;i++)solve(i);
	return 0;
}
