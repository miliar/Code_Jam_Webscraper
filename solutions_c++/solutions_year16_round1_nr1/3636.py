#include <iostream>
#include <deque>
#include <string>
using namespace std;
int main(){
	int n;
	cin >> n;
	string str;
	for(int i=0;i<n;i++){
		cout << "Case #" << i+1 << ": ";
		cin >> str;
		deque<char> deq;
		for(int j=0;j<str.length();j++){
			if(j==0){
				deq.push_back(str[j]);
			}
			else{
				if(deq[0]<=str[j]){
					deq.push_front(str[j]);
				}
				else{
					deq.push_back(str[j]);
				}
			}
		}
		for(int k=0;k<str.length();k++){
			cout << deq[k];
		}
		cout << endl;
	}
	return 0;
}