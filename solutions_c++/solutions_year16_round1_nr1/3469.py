#include <iostream>
#include <sstream>
using namespace std;

int main() {
	freopen("A-large.in","r",stdin);
	freopen("output.out","w",stdout);
	int cases;
	string s;
	string res = "";
	char letter;
	int i = 0;
	int caseNumber = 1;
	scanf("%d\n",&cases);
	while(cases > 0){
		cin >> s;
		for(;i<s.size();i++){
			if(res.size() <= 0){
				res = s[i];
			}else{
				if(s[i] >= res[0]){
					res = s[i] + res;
				}else{
					res = res + s[i];
				}
			}
		}
		i = 0;
		cout << "Case #" << caseNumber << ": " << res << endl;
		caseNumber++;
		cases--;
		res = "";
	}
	return 0;
}