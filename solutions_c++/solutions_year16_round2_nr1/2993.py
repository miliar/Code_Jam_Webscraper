// IN THE NAME OF GOD!

#include <bits/stdc++.h>
using namespace std;

typedef long long int lld;

#define pb push_back
#define mp make_pair




main(){
//	 ifstream cin;
//	 ofstream cout;
//	cin.open("B-small-attempt0 (2).in"); cout.open("out.txt");
	int t;
	cin >> t;
	int j = 0;
	while(t--){
		j++;
		cout << "Case #" << j << ": ";
		string s1, s2;
		cin >> s1 >> s2;
		int ll =s1.length();
		int mk=0;
		for(int i=0; i<ll;i++){
			if(s1[i]!='?' && s2[i]!='?' && s1[i]>s2[i] && mk==0) mk=1;
			else if(s1[i]!='?' && s2[i]!='?' && s1[i]<s2[i] && mk==0) mk=2;
			if(s1[i]=='?' && s2[i]!='?' && mk==0){
				s1[i]=s2[i];
			}
			else if(s1[i]=='?' && s2[i]!='?' && mk==1){
				s1[i]='0';
			}
			else if(s1[i]=='?' && s2[i]!='?' && mk==2){
				s1[i]='9';
			}
			
			if(s2[i]=='?' && s1[i]!='?' && mk==0){
				s2[i]=s1[i];
			}
			else if(s2[i]=='?' && s1[i]!='?' && mk==1){
				s2[i]='9';
			}
			else if(s2[i]=='?' && s1[i]!='?' && mk==2){
				s2[i]='0';
			}
		//	cout << mk << endl;
			if(s1[i]==s2[i] && s2[i]=='?'){
				if(mk==0){
					s1[i]='0';
					s2[i]='0';
				}
				else if(mk==1){
					s1[i]='0';
					s2[i]='9';
				}
				else if(mk==2){
					//cout << "*\n";
					s1[i]='9';
					s2[i]='0';
				}
			}
		}
		cout << s1 <<" " <<s2 << endl;
	}	
}
