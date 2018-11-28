#include<iostream>
#include<algorithm>
#include<bitset>
#include<string>
using namespace std;
int main(){
	
	int n;
	cin >> n;
	for(int j = 1 ; j <= n; j++){
		string s;
		cin >> s;
		bool mode = false;
		int i = 0;
		int count = 0;
		//	cout << s.size() << endl;
		while(s.size() >= i){
			//cout << (s.size()-i)-1 << " ";
			if(mode){
				if(s[(s.size()-i)-1] == '+'){
					//cout << s[(s.size()-i)-1] << endl;
					count++;
					mode = false;
				}	
			}else{
				if(s[(s.size()-i)-1] == '-'){
					//cout << s[(s.size()-i)-1] << endl;
					count++;
					mode = true;
				}			
			}
			i++;
		}
		cout <<"Case #" << j <<": "<< count << endl;
	}	
	return 0;
}
