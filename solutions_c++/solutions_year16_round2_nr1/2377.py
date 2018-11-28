#include<bits/stdc++.h>
using namespace std;
map<char,int> mape;
vector<int> ans;
int T;
string input;
int len,cnt;
int main(){
	freopen("A-large.in","r",stdin);
	freopen("Aout2.txt","w",stdout);
	cin>>T;
	for(int i=1;i<=T;i++){
		mape.clear();
		ans.clear();
		cin>>input;
		len=input.length();
		
		for(int i=0;i<len;i++){
			mape[input[i]]++;
		}
		
		cnt=mape['Z']; //zero
		while(cnt--){
			//cout<<0<<endl;
			mape['Z']--;
			mape['E']--;
			mape['R']--;
			mape['O']--;
			ans.push_back(0);
		}
		
		cnt=mape['U']; //four
		while(cnt--){
			//cout<<4<<endl;
			mape['F']--;
			mape['O']--;
			mape['U']--;
			mape['R']--;
			ans.push_back(4);
		}
		
		cnt=mape['X']; //six
		while(cnt--){
			//cout<<6<<endl;
			mape['S']--;
			mape['I']--;
			mape['X']--;
			ans.push_back(6);
		}
		
		cnt=mape['G']; //eight
		while(cnt--){
			//cout<<8<<endl;
			mape['E']--;
			mape['I']--;
			mape['G']--;
			mape['H']--;
			mape['T']--;
			ans.push_back(8);
		}
		
		cnt=mape['W']; //two
		while(cnt--){
			//cout<<2<<endl;
			mape['T']--;
			mape['W']--;
			mape['O']--;
			ans.push_back(2);
		}
		
		cnt=mape['S']; //seven
		while(cnt--){
			//cout<<7<<endl;
			mape['S']--;
			mape['E']--;
			mape['V']--;
			mape['E']--;
			mape['N']--;
			ans.push_back(7);
		}
		
		cnt=mape['V']; //five
		while(cnt--){
			//cout<<5<<endl;
			mape['F']--;
			mape['I']--;
			mape['V']--;
			mape['E']--;
			ans.push_back(5);
		}
		
		cnt=mape['I']; //nine
		while(cnt--){
			//cout<<9<<endl;
			mape['N']--;
			mape['I']--;
			mape['N']--;
			mape['E']--;
			ans.push_back(9);
		}
		
		cnt=mape['R']; //three
		while(cnt--){
			//cout<<3<<endl;
			mape['T']--;
			mape['H']--;
			mape['R']--;
			mape['E']--;
			mape['E']--;
			ans.push_back(3);
		}
		
		cnt=mape['O']; //one
		while(cnt--){
			//cout<<1<<endl;
			mape['O']--;
			mape['N']--;
			mape['E']--;
			ans.push_back(1);
		}
		
		sort(ans.begin(),ans.end());
		cout<<"Case #"<<i<<": ";
		for(auto it:ans)
			cout<<it;
		cout<<endl;
	}
} 
