#include <bits/stdc++.h>
using namespace std;

int main(){

	int test,t=1,ctr[100];
	string ans;
	char in[2002];
	
	for( scanf("%d",&test) ; test-- ; printf("Case #%d: %s\n",t++,ans.c_str()) ){
		scanf("%s",in);
		memset(ctr,0,sizeof(ctr));
		ans = "";
		for( int i=0 ; in[i] ; i++ ){
			ctr[in[i]]++;
		}
		
		for(; ctr['Z'] ;){
			ans += "0";
			ctr['Z']--;
			ctr['E']--;
			ctr['R']--;
			ctr['O']--;	
		}
		for(; ctr['W'] ;){
			ans += "2";
			ctr['T']--;
			ctr['W']--;
			ctr['O']--;	
		}
		for(; ctr['X'] ;){
			ans += "6";
			ctr['S']--;
			ctr['I']--;
			ctr['X']--;	
		}
		for(; ctr['G'] ;){
			ans += "8";
			ctr['E']--;
			ctr['I']--;
			ctr['G']--;
			ctr['H']--;	
			ctr['T']--;	
		}
		for(; ctr['T'] ;){
			ans += "3";
			ctr['T']--;
			ctr['H']--;
			ctr['R']--;
			ctr['E']--;	
			ctr['E']--;	
		}
		for(; ctr['R'] ;){
			ans += "4";
			ctr['F']--;
			ctr['O']--;
			ctr['U']--;
			ctr['R']--;	
		}
		for(; ctr['O'] ;){
			ans += "1";
			ctr['O']--;
			ctr['N']--;
			ctr['E']--;	
		}
		for(; ctr['F'] ;){
			ans += "5";
			ctr['F']--;
			ctr['I']--;
			ctr['V']--;
			ctr['E']--;	
		}
		for(; ctr['S'] ;){
			ans += "7";
			ctr['S']--;
			ctr['E']--;
			ctr['V']--;
			ctr['E']--;
			ctr['N']--;	
		}
		for(; ctr['N'] ;){
			ans += "9";
			ctr['N']--;
			ctr['I']--;
			ctr['N']--;
			ctr['E']--;	
		}
		
		for( int i ='A'; i<='Z' ; i++ ) assert(ctr[i]==0);
		sort(ans.begin(),ans.end());
			
	}
	return 0;
}

