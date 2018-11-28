#include <bits/stdc++.h>
using namespace std;
string toString(long long int asd){
	stringstream ss;
	ss<<asd;
	return ss.str();
}
int main(){
	freopen ("A-large.in","r",stdin);
	freopen ("A-large.out","w",stdout);
	int t;
	long long n;
	cin>>t;
	for(int tc = 1; tc <= t; tc++){
		vector<bool> dig(10,false);
		int s = 1;
		cin>>n;
		cout<<"Case #"<<tc<<": ";
		if(n == 0)cout<<"INSOMNIA"<<endl;
		else{
			while(count(dig.begin(),dig.end(),true) != 10){
				long long int aux = n * s;
				string a = toString(aux);
				for(int i = 0; i < a.size();i++){
					dig[a[i]-'0'] = true;
				}
				s++;
			}
			cout<< n * (s-1)<<endl;
		}
	}
	return 0;
}