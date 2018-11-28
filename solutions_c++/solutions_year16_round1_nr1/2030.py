#include <iostream>
#include <unordered_map>
#include <string>
#include <set>
using namespace std;

int main(){
	int T;
	cin>>T;
	string s;
	int x=0;
	while(T--){
		cin>>s;
		x++;
		string re = "";
		for(auto c:s){
			if(re.size()==0)re+=c;
			else{
				if(c>=re[0])re = c+re;
				else re+=c;
			}
		}
		
		cout << "Case #"<<x<<": "<<re<<endl;
		
	}
	return 0;
}
