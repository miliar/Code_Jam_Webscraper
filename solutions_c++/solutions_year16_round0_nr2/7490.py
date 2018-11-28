#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
	int i;
	cin>> i;
	int joker = 1;
	while(joker<=i) {
		int count =0;
		string str;
		cin >> str;
		int minus=0;
		int len = str.length();
		for(int j=0;j<len;j++) {
			if(str[j]=='-') {
				minus++;
			}
		}
		int index=0;
		if(len==minus) {
			count=1;
		}
		else {
			for(int i=index;i<len;i++) {
				if(str[i]=='+' && str[0]=='-') {
					count=count+1;
					break;
				}
			}
			for(int j=index;j<len-1;j++) {
				if(str[j]=='+' && str[j+1]=='-')
					count+=2;
			}
		}
		cout<< "Case #"<<joker<<": "<<count<<endl;
		++joker;
	}
}