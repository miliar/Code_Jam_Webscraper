#include<iostream>
#include<string>
#include<sstream>
using namespace std;

int main(){
	int t;
	
	cin >> t;
	
	for(int i = 0; i < t; i++){
		int num;
		cin >> num;
		if(num == 0){
			cout << "Case #"<<(i+1)<<": INSOMNIA "<< endl;
			continue;
		}
		int num_iter = 0;
		int new_num = 0;
		char track[] = {'0', '1', '2', '3', '4', '5', '6', '7', '8' ,'9'};
		while(true){
			new_num = num * (num_iter+1);
			string num_str;          // string which will contain the result

			ostringstream convert;   // stream used for the conversion
	
			convert << new_num;      // insert the textual representation of 'Number' in the characters in the stream

			num_str = convert.str();
			//string num_str = static_cast<ostringstream*>( &(ostringstream() << new_num) )->str();
			
			for(int j = 0; j < num_str.length(); j++){
				for(int k = 0; k < 10; k++){
					
					if(num_str[j] == track[k]){
						track[k] = 'D';
					}
				}
			}
			bool chk = false;
			for(int l = 0; l < 10; l++){		
				if(track[l] != 'D'){
					chk = true;
					break;
				}
			}
			if(chk == false){
				cout << "Case #"<<(i+1)<<": " << num_str<< endl;
				break;
			}else{
				num_iter++;
			}
		}
	}
	return 0;
}