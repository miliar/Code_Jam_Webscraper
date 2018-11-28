#include <iostream>
#include <string>
#include <list>

using namespace std;

int main(){
	int t;
	cin >> t;
	int id=1;
	while(t--){
		string s;
		list<char> lc;
		cin >> s;
		lc.push_back(s[0]);

		for(int i=1; i< s.size();i++){
			if(s[i] >= lc.front()) lc.push_front(s[i]);
			else lc.push_back(s[i]);
		}
		printf("Case #%d: ",id++ );
		while(lc.size()>0)
		{
			printf("%c",lc.front());
			lc.pop_front();
		}
		printf("\n");
	}	



	return 0;
}