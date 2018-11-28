//*/
#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <deque>
#include <set>
#include <map>
#include <list>
#include <limits>
#include <queue>
#include <stdexcept>
#include <iomanip> 
#include <sstream>

using namespace std;

#define TRY
//#define SMALL
#define LARGE

int Solve();
string Flip(string a);
bool Judge(string a);

void main() 
{
#ifdef TRY
	freopen("1.txt", "rt", stdin);
	//freopen("2.out","wt",stdout);
#endif
#ifdef SMALL
	freopen("B-small-attempt0.in","rt",stdin);
	freopen("B-small.txt","wt",stdout);
#endif
#ifdef LARGE
	freopen("B-large.in","rt",stdin);
	freopen("B-large.txt","wt",stdout);
#endif
	int Numcase;
	cin>>Numcase;
	for(int test=1;test<=Numcase;test++)
	{
		cout<<"Case #"<<test<<": ";
		cout<<Solve()<<endl;
	}
}
int Solve(){
	map<string, int>::iterator it;
	int cnt=0;
	string st;
	cin>>st;
	int len ;
	int last_minos, first_minos;
	while(!Judge(st)) {		
		len = st.length();
		last_minos=len-1, first_minos=0;
		while(st[last_minos]=='+' && last_minos>=0 ) last_minos--;
		if(last_minos==-1) return cnt;
		if(st[first_minos]=='-') {
			cnt++;
			st = Flip(st.substr(0,last_minos+1));
		}
		else{
			while(st[first_minos]=='+' && first_minos<len) first_minos++;
			for(int i=0;i<first_minos;i++) st[i]='-';
			cnt++;
		}
	}
	return cnt;

}
string Flip(string a){
	reverse(a.begin(),a.end());
	int len=a.length();
	for(int i=0;i<len;i++){
		if(a[i]=='+') a[i]='-';
		else a[i]='+';
	}
	return a;
}
bool Judge(string a){
	int len=a.length();
	for(int i=0;i<len;i++){
		if(a[i]=='-') return false;
	}
	return true;
}