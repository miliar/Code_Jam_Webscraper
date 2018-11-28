#include <iostream>
using namespace std;
int main(){
	freopen("input2.in","r",stdin);
	freopen("output2.out","w",stdout);
	int t,c=1;
	cin >> t;
	while(t--){
		string str,result;
		char temp;
		cin >> str;
		int len;
		len = str.length();
		result+=str[0];
		for(int i=1;i<len;i++){
			if(str[i]<result[0]) result+=str[i];
			else result = str[i]+result;
		}	
		cout << "Case #"<< c++ <<": " << result << endl;
	}
	return 0;
}
