#include <iostream>
#include <algorithm>
using namespace std;

void change(int last, string &s){
	int start = 0;
	//cout<<"          " <<s<<"     ";
	for(;start<last;start++,last--){
		if(s[start]=='-') s[start]='+';
		else s[start]='-';
		if(s[last]=='-') s[last]='+';
		else s[last] = '-';
		swap(s[start],s[last]);
	}
	if(start==last){
		if(s[start]=='-')s[start]='+';
		else s[start] = '-';
	}
	//cout<<s<<endl;
}


int main() {
	// your code goes here
	int t,ii=0;
	cin>>t;
	while(ii++<t){
		string s;
		cin>>s;
		int last,nlast;
		int count =0;

		last = 0;
		bool found = false;
		//cout<<s<<"            ";
		cout<<"Case #"<<ii<<": ";
		for(int i=last;last<s.size();last++){
			if(s[last]=='-'){
				continue;
			}
			if(last)count++;
			for(int j=last;j<s.size();last++){
				if(s[last]=='+')continue;
				else break;
			}
			//cout<<"last="<<last<<endl;
			if(last == s.size()){ //all positive
				cout<<count<<endl;
				found = true;
			}
			else count++;


		}
		if(!found){
			if(last == s.size() && s[last-1]=='-')cout<<count+1<<endl;
			else cout<< count<<endl;
		}
	}
	return 0;
}
