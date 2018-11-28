#include <iostream>
#include <string>

using namespace std;

int main(){
	int T;
	cin >> T;
	for(int t=0;t<T;t++){
		int n;
		string s;
		cin >> n >> s;

		int stand = 0;
		int invite = 0;
		for(int i=0;i<=n;i++){
			if(stand>=i){
				stand += s[i]-'0';
			}else{
				invite += i-stand;
				stand += (s[i]-'0')+(i-stand);
			}
		}
		printf("Case #%d: %d\n", t+1, invite);
	}
}