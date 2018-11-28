#include <string>
#include <iostream>
using namespace std;
bool b[105];
int n,l,ans;
void reverse(int x){
	bool t[105];
	for(int i=1; i<=x; ++i)
		t[i]=!b[x-i+1];
	for(int i=1; i<=x; ++i) b[i]=t[i];
	++ans;
}
int main(){
	cin>>n;
	for(int i=1; i<=n; ++i){
		ans=0;
		string s;
		cin>>s;
		l=s.length();
		for(int j=0; j<l; ++j) b[j+1]=s[j]=='+';
		int R=l;
		while(1){
			while(R>=1&&b[R]) --R;
			if (R<1) break;
			int L=1;
			while(L<R&&b[L]==b[L+1]) ++L;
			if (b[L]) reverse(L);
			reverse(R);
		}
		cout<<"Case #"<<i<<": "<<ans<<"\n";
	}
	return 0;
}
