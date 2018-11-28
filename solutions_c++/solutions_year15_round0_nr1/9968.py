#include <bits/stdc++.h>

using namespace std;

int main(){
	int T;
	cin>>T;
	int n;
	string s;
	for (int z = 0; z < T; z++){
		cin>>n>>s;
		int help = 0;
		int acum = (int)s[0] -48;
		for(int i=1; i<n+1; i++){
			if((int)s[i]-48!=0){
				if(i-acum>0){ help+=i-acum; acum+=help; }
			}
			acum+=(int)s[i]-48;
			//cout<<"State: "<<i<<" "<<help<<" "<<acum<<endl;
		}

		cout<<"Case #"<<z+1<<": "<<help<<endl;
	}
}