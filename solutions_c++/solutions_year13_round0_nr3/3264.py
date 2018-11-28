#include <iostream>
#include <string>
#include <cmath>
#include <fstream>
using namespace std;
long long Case,n,A,B,ans,i,h[23333];
bool hw(int x){
	int i=0;
	char ch[2333];
	string s;
	sprintf(ch,"%d",x);
	s=ch;
	for(i=0;i<=s.length()/2;++i)
		if(s[i]!=s[s.length()-i-1])
			return 0;
	return 1;
}
int main(){
	ofstream cout ("C.out");
	ifstream cin ("C.in");
	cin >> n;
	for(Case=1;Case<=n;++Case){
		cout << "Case #" << Case << ": ";
		cin >> A >> B;
		ans=0;
		i=(int)sqrt(A);
		if(i*i<A) ++i;
		while(i*i<=B){
			if(hw(i)&&hw(i*i)){
				++ans;
				//cout << i << ' ' << i*i << endl;
			}
			++i;
		}
		cout << ans << endl;
	}
	return 0;
}
