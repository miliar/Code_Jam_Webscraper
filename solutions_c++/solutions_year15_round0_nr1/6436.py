#include<bits/stdc++.h>
using namespace std;
int main(){
	int t,elimcount,sum,j,i,l,pp;
	string str;
	cin >> t;
	for(i=1;i<=t;++i){
		elimcount = 0;
		cin >> l;
		cin >> str;
		sum = str[0]-'0';
		for(j=1;j<=l;++j){
			pp=str[j]-'0';
			if(sum<j){ elimcount +=(j-sum);sum=j;}
			sum+=pp;
		}
		cout << "Case #"<<i << ": " << elimcount << endl;
	}
}
