#include <iostream>
#include <list>
#include <string>
#include <algorithm>
using namespace std;

void exe();
int main(void)
{	
	int T;	cin >> T;
	for(int caseNum=1; caseNum<=T ; ++caseNum){
		cout << "Case #" << caseNum << ": ";
		exe();
		cout << endl;	
	}
	return 0;
}

void exe()
{
	string str;
	cin >> str;
	list<char> lt{str[0]};
	for(auto i=str.cbegin()+1 ; i!=str.cend() ; ++i)
		if(*i >= lt.front()) lt.push_front(*i);
		else lt.push_back(*i);
	for(auto i : lt) cout << i;
}
