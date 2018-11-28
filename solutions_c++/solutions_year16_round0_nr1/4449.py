#include<bits/stdc++.h>
using namespace std;
int a[10];
int cnt;
void check(string s) {
	for(int i=0;i<s.length();i++) 
		if(a[s[i]-'0']==0){
			a[s[i]-'0']=1;
			cnt++;
		}
}
int main() {
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	int t,cases=0;
	scanf("%d",&t);
	while(t--) {
		long long n,k;
		scanf("%lld",&n);
		string cur;
		int j=1;
		cnt=0;
		memset(a,0,sizeof(a));
		if(n==0)
			cout << "Case #" <<++cases <<": " << "INSOMNIA" << endl;
		else {
			while(cnt<10) {
				k=n*j;
				stringstream ss;
				ss << k;
				cur = ss.str();
				check(cur);
				j=j+1;
			}
			cout << "Case #" << ++cases << ": " << (long long) (n*(j-1)) << endl;
		}
	}
	//fclose(stdout);
	return 0;
}
