#include<iostream>
#include<cstring>
using namespace std;
int main(){
	bool v[10];
	int t;
	cin >> t;
	int n;
	for (int tt=0;tt<t;tt++){
		memset(v,false,sizeof(v));
		cin >> n;
		long long now=n;
		int x=0,ved=0;
		for (int i=0;i<1000000;i++){
			int now2=now;
			while (now2>0){
				int w=now2%10;
				if (!v[w]){
					v[w]=true;
					ved++;
				} 
				now2/=10;
			}
			x=now;
			now+=n;
			if (ved==10) break; 
		}
		cout << "Case #" << tt+1 << ": ";
		if (ved==10)
			cout << x << endl;
		else
			cout << "INSOMNIA" << endl;
	}
	return 0;
}

