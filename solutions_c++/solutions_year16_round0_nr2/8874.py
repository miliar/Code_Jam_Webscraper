#include <iostream>
#include <string>
using namespace std;

class solution{
	string str;
	int ans;
public:
	solution(string in) : str(in), ans(0){
		removeRedundency();
		removeLastHappy();
		ans += removeFirstHappy();
		ans += str.size();
		cout << ans << endl;
	}
	void removeRedundency(){
		for(int i=1;i<str.size();i++){
			if(str[i]==str[i-1]){
				str.erase(str.begin()+i);
				i--;
			}
		}
	}
	void removeLastHappy(){
		while(str.back()=='+')
			str.pop_back();
	}
	bool removeFirstHappy(){
		if(str.front()=='+'){
			str.erase(str.begin());
			return true;
		}
		else 
			return false;
	}
	void printSTR(){
		cout << str << endl;
	}
};

int main(){
	int count;
	cin >> count;
	string tmp;
	for(int i=0;i<count;i++){
		cin >> tmp;
		cout << "Case #" << i+1 << ": ";
		solution a(tmp);
	}

}