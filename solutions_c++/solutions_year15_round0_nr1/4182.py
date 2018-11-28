#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define ull unsigned long long
#define pb push_back
#define ft first
#define se second
#define mp make_pair

int main(int argc, char const *argv[]){
	int t,p;
	cin>>t;
	p=t;
	while(t--){
		int s;
		cin>>s;
		int tot=0,act=0, tmp;
		char x;
		for (int i = 0; i < s+1; ++i){
			cin>>x;
			tmp=(int)(x-'0');
			tot=max(tot,i);
			tot+=tmp;
			act+=tmp;	
		}
		cout<<"Case #"<<p-t<<": "<<tot-act<<endl;
	}
	return 0;
}