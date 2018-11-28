#include<bits/stdc++.h>

using namespace std;
int main(){

	int t,cnt,step_cnt=0;
	string s;
	cin>>t;
	for(int j=1;j<=t;j++){
		cin>>s;
		//cout<<s.length();
		int plus_cnt = 0;
		int min_cnt = 0;
		for(int i=0;i<s.length();i++){
			if(s[i] == '+')
				plus_cnt++;
			else{
				min_cnt++;
			}
		}
		if(plus_cnt == s.length()){
			cout << "Case #" << j << ": " <<0<< endl;
		}else if (min_cnt == s.length()){
			cout << "Case #" << j << ": " <<1<< endl;
		}else{
			cnt = 0;
			int i = 0;
			while(i < s.length()){	
				char c = s[0];
				i = 0;
				if(c == '+'){
					step_cnt = 0;
					while(s[i] == '+' && i < s.length()){
						s[i] = '-';
						i++;
						step_cnt++;
					}
					if(step_cnt == s.length()){
						//cnt = 0;
						break;
					}
					cnt++;
					
				}else{
					step_cnt = 0;
					while(s[i] == '-' && i < s.length()){
						s[i] = '+';
						step_cnt++;
						i++;
					}
					if(step_cnt == s.length()){
						//cnt = 0;
						break;
					}
					cnt++;
					
				}
			}
			if(s[0] == '-'){
				cout << "Case #" << j << ": " <<cnt<< endl;
			}else{
				cout << "Case #" << j << ": " <<cnt+1<< endl;
			}
		}
	}
	return 0;
}