#include <bits/stdc++.h>

using namespace std;

void convertInt(string s, int people[]){
	for(int i=0; i<s.size(); i++){
		people[i] = s[i]-'0';
	}
}

int main(){
	int t,Smax;
	string s;
	cin>>t;
	for(int i=1; i<=t; i++){
		int parados=0,sentados=0,amigos=0;
		cin>>Smax;
		cin>>s;
		int people[Smax+1];
		convertInt(s,people);
		for(int j=0; j<= Smax; j++){
			sentados += people[j];
		}
		if(people[0] != 0) {
			parados += people[0];
			sentados -= people[0];
		}
		for(int j=1; j<= Smax; j++){
			if(people[j] != 0){
				if(j <= parados){
					parados += people[j];
					sentados -= people[j];
				}
				else{
					amigos += j - parados;
					parados += amigos + people[j];
					sentados -= people[j];
				}
			}
		}

		cout<<"Case #"<<i<<": "<<amigos<<endl;
	}
	return 0;
}