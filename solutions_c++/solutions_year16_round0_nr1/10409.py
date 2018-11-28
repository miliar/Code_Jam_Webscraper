#include <bits/stdc++.h>

using namespace std;

int main(){
	int n;
	cin >> n;
	for(int i=0;i<n;i++){
		int a;
		cin >> a;
		if(a == 0){
			cout << "CASE #" << i+1 << ": INSOMNIA" << endl;
			continue;
		}
		int s=0;
		bool b[10] = {0};
		while(1){
			s+=a;
			for(int i=1;i<=s;i*=10){
				b[(s/i)%10]=true;
			}
			bool f=true;
			for(int i=0;i<10;i++){
				f&=b[i];
			}
			if(f){
				cout << "CASE #" << i+1 << ": " << s << endl;
				break;
			}
		}
	}
	
	return 0;
}