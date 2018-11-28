#include<bits/stdc++.h>
using namespace std;
string literal[]={"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
int freq_dist[26];
void subtract(string str,int n){
	int l=str.length();
	for(int i=0;i<l;i++){
		freq_dist[str[i]-'A']-=n;
	}	
}
void make_freq_dist(string str){
	for(int i=0;i<26;i++){
		freq_dist[i]=0;
	}
	int l=str.length();
	for(int i=0;i<l;i++){
		freq_dist[str[i]-'A']++;
	}
}
inline int freq(char x){
	return freq_dist[x-'A'];
}
int order[] = {0,2,6,8,7,5,3,4,1,9};
int letter[] = {'Z','O','W','T','F','V','X','S','G','I'};
int main(){
	int t;
	cin>>t;
	string str;
	string ans;
	int counts[10];
	for(int tcase=1;tcase<=t;++tcase){
		cin>>str;
		ans="";
		for(int i=0;i<10;i++)counts[i]=0;
		make_freq_dist(str);
		for(int i=0;i<10;i++){
			int digit=order[i];
			counts[digit]=freq(letter[digit]);
			subtract(literal[digit],counts[digit]);
			// cout<<counts[digit]<<' '<<digit<<endl;
		}

		for(int i=0;i<10;i++){
			ans.append(counts[i],'0'+i);
		}
		cout<<"Case #"<<tcase<<": "<<ans<<endl;
	}
	return 0;

}