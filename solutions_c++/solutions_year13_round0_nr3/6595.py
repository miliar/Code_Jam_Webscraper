#include <iostream>
#include <string>
#include <cstring>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <climits>
#include <cctype>
#include <cmath>
#include <sstream>
#include <cstdlib>
#include <climits>
#include <ctime>
#include <set>
#include <map>
#include <numeric>
#include <utility>
#include <deque>
#include <queue>
#include <stack>
#include <iomanip>
#include <complex>
#include <list>
#include <bitset>
#include <fstream>
#include <limits>
#include <memory.h>

using namespace std;

#define READ(s) freopen(s, "r", stdin)
#define WRITE(s) freopen(s, "w", stdout)

bool Palindrome(string str){
	stack<char>LOL;
	bool flag=true;
	for(int i=0;i<str.size();i++) LOL.push(str[i]);
	
	for(int i=0;i<str.size();i++){
		char ch=LOL.top();
		if(ch==str[i]){
			LOL.pop();
			continue;
		}
		else {
			flag=false;
			break;	
		}
	}	
	if(flag)return true;
	return false;
}
bool Square(unsigned long long int n){
	if (n < 0)
        return false;
    unsigned long long int root(round(sqrt(n)));
    return n == root * root;

}
unsigned long long int Square2(unsigned long long int n){
	if (n < 0)
        return 0;
    unsigned long long int root(round(sqrt(n)));
    if(n == root * root)
		return root;

}

int main()
{
	READ("C-small-attempt0.in");    // esm l downloaded file ay 7aga 
    WRITE("C-large.txt");  // esm l output file w dah hn3melo upload m3 l source pp
	vector<string>re;
	int TestCases=0,counter=1;;
	cin>>TestCases;
	
	while(TestCases>0){
		string A,B,temp="Case #",s,ko="";
		stringstream ss;
		ss<<counter;
		ss>>s;
		temp+=s;
		
		cin>>A>>B;
		int kamWa7ed=0;
		stringstream ss2,ss3;
		unsigned long long int xx,xxx;
		ss2<<A;
		ss2>>xx;
		
		ss3<<B;
		ss3>>xxx;
		
	//	cout<<xx<<" "<<xxx<<endl;
		for(unsigned long long int i=xx;i<=xxx;i++){
			string x;
			stringstream ss;
			ss<<i;
			ss>>x;
			
			unsigned long long int G=Square2(i);
	//		cout<<G<<endl;
			string yy;
			stringstream zz;
			zz<<G;
			zz>>yy;
			if(Square(i)&&Palindrome(x)&&Palindrome(yy)) kamWa7ed++;
			
			//else continue;
		}
//		cout<<kamWa7ed<<endl;
		stringstream sx;
		string o;
		sx<<kamWa7ed;
		sx>>o;
		ko=temp+": "+o;
		re.push_back(ko);
		
	TestCases--;counter++;
	}

	for(int i=0;i<re.size();i++)cout<<re[i]<<endl;

	return 0;
	
}
