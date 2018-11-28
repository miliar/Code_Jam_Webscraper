#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <list>
#include <algorithm>
#include <cmath>
#include <stack>
#include <map>
#include <iomanip>

using namespace std;
typedef long long lint;

void swapblins(string &a,int i){
	reverse(a.begin()+i,a.end());
	for(;i<a.length();i++)
	{
		a[i]=(a[i]=='+'?'-':'+');
	}
}

int main() {
	ifstream cin("123.in");
	ofstream cout("123.out");
	int T;
	cin>>T;
	for(int i=0;i<T;i++){
		string s;
		cin>>s;
		s+='+';
		int v=0;
		for(int j=0;j<s.length()-1;j++){
			if(s[j]!=s[j+1])v++;
		}
		cout<<"Case #"<<(i+1)<<": "<<v<<endl;
	}
	cin.close();
	cout.close();
}