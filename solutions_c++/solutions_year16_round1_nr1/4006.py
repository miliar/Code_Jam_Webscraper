#include <iostream>

using namespace std;

int cmp(char a, char b){
	if(a<b) return -1;
	else if(a>b) return 1;
	else return 0;
}

int main(){
	int t,c=1;cin>>t;
	string word, win;
	while(c<=t){
		cin>>word;
		win = word[0];
		char b = word[0], s = word[0];
		for(int i=1;i<word.length();i++){
			if(cmp(word[i],b)==-1){
				win = win + word[i];
				s = word[i];
			}else if(cmp(word[i],b)>=0){
				win = word[i] + win;
				b = word[i];
			}
		}
		cout<<"Case #"<<c++<<": "<<win<<endl;
	}
}