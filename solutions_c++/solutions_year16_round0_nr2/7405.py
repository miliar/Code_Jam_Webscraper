#include "iostream"
#include "string"
#include "algorithm"
using namespace std;

int count(string str){
	int k = 0;
	int length=str.length();

	for (int i = 0; i < length; ++i){
		if(str[i] == '+')
			k++;
	}
	return k;
}

int first_of(string str , char s){
	int length=str.length();
	for(int i = 0 ; i < length; i++ ){
		if(str[i] == s)
			return i;
	}
}

int replace(string &str , int pos){
	int length=str.length();
	for(int i = 0 ; i < pos+1 ; i++){
		if(str[i] == '+')
			str[i] = '-';
		else str[i] = '+';
	}
}
int last_of(string str, char s){
	int length=str.length();
	for(int i = length ; i >=0  ; i--){
		if(str[i] == s)
			return i;
	}
}

int count(string str, char s){
	int length = str.length() , k = 0;
	for(int i=  0 ; i < length ; i++){
		if(str[i] ==s)
			k++;
	}
	return k;
}

int main(int argc, char const *argv[])
{
	string str;
	int t;
	cin >> t;
	for(int j = 1 ; j <= t ; j++){
	cin >> str;
	int cnt = 0;
	int length = str.length();
	int n = count(str);
	int min = count(str,'-');
	if(n == length)
		cout << "Case #" << j << ": 0" << endl; // all are happy
	else if(length == min ){
		cout << "Case #" << j << ": 1" << endl;
	}
	else{
		while(count(str) != length){
			int last =last_of(str,'-');
			int first = first_of(str,'+');
			if(last < first){
				replace(str,last);
			}else if(last > first){
				replace(str,last);
			}
			cnt++;
		}
		cout << "Case #" << j << ": " << cnt << endl;
	}
}
	return 0;
}