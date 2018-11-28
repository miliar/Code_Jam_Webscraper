#include <iostream>
using namespace std;
int main(){
	freopen("input_2.in","r",stdin);
	freopen("output_2.out","w",stdout);
	int t,a=1;
	cin >> t;
	while(t--){
		string str;
		int len,count=0;
		char check ='+';
		cin >> str;
		len = str.length();
		check = str[0];
		for(int i=1;i<len;i++){
			if(str[i]!=str[i-1]) {
				count++;
				check = str[i];
			}
		}
		if(str[len-1]=='-') count++;
		cout << "Case #" << a++ <<": " <<  count << endl;
	}
	return 0;

}
