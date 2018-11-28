#include <iostream>
#include <vector>
#include <string>
#include <bitset>
using namespace std;
void exe();

int main(void)
{	
	int T;
	cin >> T;
	for(int caseNum=1; caseNum<=T ; ++caseNum){
		cout << "Case #" << caseNum << ": ";
		exe();
		cout << endl;	
	}
	return 0;
}

using boolCIt = vector<bool>::const_iterator;
using boolCRIt = vector<bool>::const_reverse_iterator;
int minStep(boolCIt begin, boolCIt end, bool happySide);
int minStep(boolCRIt begin, boolCRIt end, bool happySide);

void exe()
{
	string s;
	cin >> s;
	vector<bool> stk(s.size(), false);
	auto stkIt = stk.begin();
	for(auto ch : s) *stkIt = ch=='+' ? true : false, ++stkIt;
	cout << minStep(stk.cbegin(), stk.cend(), true);
}

int minStep(boolCIt begin, boolCIt end, bool happySide)
{
	if(begin==end) return 0;
	if(*(end-1)==happySide){
		auto last = end-1;
		while(last!=begin && last[-1]==happySide) --last;
		return minStep(begin, last, happySide);
	}
	else{
		auto newBegin = begin;
		while(*newBegin==happySide) ++newBegin;
		if(newBegin==begin) return minStep(boolCRIt{end}, boolCRIt{begin}, !happySide) + 1;
		else return minStep(boolCRIt{end}, boolCRIt{newBegin}, !happySide) + 2;
	}
} 
int minStep(boolCRIt begin, boolCRIt end, bool happySide)
{
	if(begin==end) return 0;
	if(*(end-1)==happySide){
		auto last = end-1;
		while(last!=begin && last[-1]==happySide) --last;
		return minStep(begin, last, happySide);
	}
	else{
		auto newBegin = begin;
		while(*newBegin==happySide) ++newBegin;
		if(newBegin==begin) return minStep(end.base(), begin.base(), !happySide) + 1;
		else return minStep(end.base(), newBegin.base(), !happySide) + 2;
	}
} 
