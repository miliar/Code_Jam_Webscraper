#include <iostream>
#include <string>
#include <bitset>
#include <math.h>
using namespace std;

int main()
{
	int T;
	int index = 1;
	cin >> T;
	while(T--){
		string str;
		cin >> str;
		int len = strlen(str.c_str());
		string curr = "";
		curr += str[0];
		for (int i=1;i<len;i++){
			int currlen = strlen(curr.c_str());
			int l=0,r=0;
			if (str[i]>=curr[0]){
				string tmp = str[i]+ curr;
				curr = tmp;
			}
			else{
				string tmp = curr+str[i];
				curr = tmp;
			}
		}
		cout << "Case #"<<index++<<": " << curr << endl;
	}
	return 0;
}