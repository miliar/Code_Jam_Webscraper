#include<bits/stdc++.h>
#define forn(i,N) for(int i=0;i<(N);i++)
#define forVec(it,ARR) for(IntArr::iterator it=ARR.begin();it<ARR.end();++it)
#define pEndLine std::cout<<std::endl
#define pPrint(p) print(p)
#define pStr(p) std::cout<<p
using namespace std;

char getFlipVal(char p, int cnt) {
	if(cnt%2==0)
		return p;
	else 
		return p=='+'?'-':'+';
}
void solve(int p) 
{	
 	std::string str;
	std::cin >> str;
	int cnt = 0;
	for(int i = str.length()-1; i >= 0; --i) 
	{
		if (getFlipVal(str[i], cnt)=='-') 
			cnt++;
	}	
	std::cout << "Case #"  << p+1 << ": " << cnt << endl;
}

int main() 
{	
	int tc;
	cin >> tc;
	forn(p, tc) 
	{
    	solve(p);
	}
  	cout << endl;
	return 0;
}

