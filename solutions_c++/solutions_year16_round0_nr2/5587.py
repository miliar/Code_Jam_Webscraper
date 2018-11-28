#include<bits/stdc++.h>
using namespace std;

int main() {
	freopen("test.txt","rt",stdin);
	freopen("o.txt","wt",stdout);

	ios::sync_with_stdio(false);

	int test;
//	cin>>test;
//	scanf("%d",&test);
	cin>>test;
	for(int tt=1;tt<=test;tt++){
		string s;
		cin>>s;
		int nums=0;
		int len = s.length();
		for(int i=0;i<len;i++){
			if(s[i] == '+')
				s[i] = '0';
			else s[i] = '1';
		}

		for(int i=len-1;i>=0;i--){
			if(((s[i]-'0')+nums )%2){
				nums++;
			}
		}
		cout<<"Case #"<<tt<<": "<<nums<<endl;
	}


	return 0;
}
