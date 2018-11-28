#include <iostream>
#include <string>
using namespace std;

int main(){
	int t;
	cin >> t;
	int k = 1;
	while(t--){
		int sMax;
		cin >> sMax;
		string s;
		cin >> s;
		int friends = 0;
		int stand = 0;
		for(int i = 0 ; i <= sMax ;i++){
			if(s[i] != '0'){
				//¼öÁİÀ½
				if(i - stand > 0){
					friends+=(i-stand);
					stand+=(i-stand);
				}
				stand+=(s[i]-'0');
			}
		}
		cout<< "Case #"<<k<<": "<<friends <<endl;
		k++;
	}
	return 0;

}