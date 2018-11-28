#include<iostream>
#include<map>
using namespace std;

string process(string s){
	if(s.length() == 0)return "";
	else if(s.length() == 1)return s;
	else{
		int max = -1;
		for(int i = 0; i < s.length(); i++){
			int t = s[i] - 'A';
			if(t >= max)max = t;
		}
		//cout << max << endl;
		map<int,bool> m;

		int count = 0;
		for(int i = 0; i < s.length(); i++){
			m[i] = false;
			if(s[i] - 'A' == max){
				m[i] = true;
				count++;	
			}
		}
		//cout << count << endl;
		string b = "";
		int i = 0, j = 0;
		int l = s.length();
		while(i < l && j < l){
			//cout <<i << " " << j << endl;
			while(m[i]&&i<l)i++;
			j = i;
			while(!m[j]&&j<l)j++;
			if(i == 0)b+=process(s.substr(i, j - i));
			else b+=s.substr(i, j - i);
			i = j;
		}
		//cout << j << endl;
		string ans = "";
		char r = 'A' + max;
		for(int k = 0; k < count; k++)ans += r;
		ans += b;
		return ans; 
	}
}


int main(){
	//cout<<process("CAB")<<endl;
	
	int t;
	cin >> t;
	for(int i = 0; i < t; i++){
		string s;
		cin >> s;
		cout << "Case #" << i +1 << ": " << process(s) << endl; 
	}
	
	return 0;
}
