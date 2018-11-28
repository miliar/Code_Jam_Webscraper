#include <bits/stdc++.h>
using namespace std;
#define ll long long

ifstream inf("test.txt");
ofstream of("out.txt");

int check(int mark[]){
	for (int i=0;i<10;i++) if (mark[i]==0) return 0;
	return 1;
}

int init(){
	ofstream of("test.txt");
	of<<2000000<<endl;
	for(int i=0;i<2000000;i++) of << i << endl;
	return 0;
}

int main(){
	//init();
	int t;
	inf>>t;
	int cs=1;
	while(t--){
		ll int n;
		inf>>n;
		if (n==0){
			of << "Case #" << cs++ << ": ";
			of << "INSOMNIA\n";
			continue;
		}
		int mark[10];
		memset(mark,0,sizeof(mark));
		int f=0;
		of << "Case #" << cs++ << ": ";
		ll int x=n;
		while(1){
			ll int temp=n;
			while(temp){
				mark[temp%10]=1;
				temp/=10;
			}
			if (check(mark)==1){
				of << n << endl;
				break;
			}
			n+=x;
		}
	}
	return 0;
}

