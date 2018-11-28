#include <iostream>
using namespace std;

void flipper(string& s,int index,int flip){
	for(int i=0;i<flip;i++){
		if(s[index+i]=='+'){
			s[index+i]='-';
		}
		else{
			s[index+i]='+';
		}
	}
}
int firstZeroCalc(string s,int firstZero){
	int i;
	for(i=firstZero;i<s.length();i++){
		if(s[i]=='-'){
			return i;
		}
	}
	return i;
}

int main(){
	int q; cin >>q;
	int tops=q+1;
	while(q>0){
		string s; cin >>s;
		int flip; cin >>flip;
		int flag=0;
		for(int i=0;i<s.length();i++){
			if(s[i] != '+'){
				break;
			}
			if(i == s.length()-1){
				
				cout<<"Case #"<< tops-q<< ": 0"<<endl;
				flag=1;
			}
		}
		if(flag ==1){
			q--;
			continue;
		}
		if(s.length() < flip ){
			q--;
			cout<<"Case #"<< tops-q<< ": " <<"IMPOSSIBLE "<<endl;
			continue;
		}
		int firstZero=0;
		int count=0;
		while(1){
				firstZero=firstZeroCalc(s,firstZero);
				if(firstZero==s.length()){
					cout<<"Case #"<< tops-q<< ": " << count<<endl;
					break;
				}
				if(firstZero+flip > s.length()){
					cout<<"Case #"<< tops-q<< ": " << "IMPOSSIBLE "<<endl;
					break;
				}
				
				flipper(s,firstZero,flip);
				count++;
				
		}


		q--;
	}


	return 0;
}