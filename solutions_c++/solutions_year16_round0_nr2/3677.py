#include <iostream>



using namespace std;



int main(){

	int tc;
	string s;
	cin>>tc;
	for(int i = 0; i < tc; i++){
		cin>>s;
		int ans = 0;
		string res;
		int n = s.length();
		int idx = n -1;
		while(s[idx] == '+'){
			idx--;
		}
		if(idx == -1){
			res = "Case #" + to_string(i+1) +": " + to_string(ans);
			cout<<res<<endl;
			continue;
		}
		
		while(1){
			int k = 0;	
			if(s[0] == '+'){
				ans += 1;
				while(s[k] == '+'){
					s[k++] = '-';
				}
			}
			else{
				ans += 1;

				reverse(s.begin(),s.begin()+idx+1);
				for(int j = 0; j <= idx; j++){
					if(s[j] == '+')s[j] = '-';
					else s[j] = '+';
				}
				while(s[idx] == '+'){
					idx--;
				}
				if(idx == -1){
					res = "Case #" + to_string(i+1) +": " + to_string(ans);
					break;
				}
			}	
						
		

	   }
	   cout<<res<<endl;
    }

}