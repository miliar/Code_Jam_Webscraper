#include <iostream>
#include<string>
#include<map>
#include<vector>
using namespace std;
bool vis[100000]={0};
string s;
string toString(int x){
	vector<int> v;
	while(x > 0){
		int lastDigit = x % 10;
		v.push_back(lastDigit);
		x /= 10;
	}
	string ans = "";
	while(v.size() > 0){
		ans += (v.back() + '0');
		v.pop_back();
	}
	return ans;
}
int main() {
	int t ,c=0;
	cin>>t;
	for (int i =0 ; i<t ; i++) {
	bool vis[100000]={0};
		int n ; 
		cin>>n;
		int tr;
		bool r=0;
		for (int j =1 ; j<=100000000 ; j++) {
			int x=n;
			x*=j;
			s=toString(x);
			//cout<<s<<endl;
			for (int k =0 ; k<s.size() ; k++) {
				vis[s[k]]++;
			}
			if (vis['9']==1 &&vis['1']==1 &&vis['2']==1 &&vis['3']==1 &&vis['4']==1 &&vis['5']==1 &&
				vis['6']==1 &&vis['7']==1 &&vis['8']==1 &&vis['0']==1){
					tr=x;
					r=1;
					break;
				
				}
			}
			if (r){
		cout<<"Case #"<<i+1<<": "<<tr<<endl;
			}else {
				cout<<"Case #"<<i+1<<": "<<"INSOMNIA"<<endl;
			}
		
	}
	return 0;
}