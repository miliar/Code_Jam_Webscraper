// {{{ Boilerplate Code <--------------------------------------------------
//
// vim:filetype=cpp foldmethod=marker foldmarker={{{,}}}

#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>

#define FOR(I,A,B)	for(int I = (A); I < (B); ++I)
#define REP(I,N)	FOR(I,0,N)
#define ALL(A)		(A).begin(), (A).end()

using namespace std;

// }}}

int is_palindrome(string in){
	if(in=="")
		return 0;
	string s;
	int i=0;
	while(in[i]=='0')
		i++;
	for(;i<in.size();i++)
		s+=in[i];

	FOR(i,0,s.size())
		if(s[i]!=s[s.size()-1-i])
			return 0;
	return 1;

}

string square(string in){
	string ans;
	FOR(i,0,110)
		ans+="0";

	FOR(i,0,in.length()){
		FOR(j,0,in.length()){
			ans[109-i-j]+=((in[i]-'0')*(in[j]-'0'))%10;
			ans[108-i-j]+=((in[i]-'0')*(in[j]-'0'))/10;

			if(ans[109-i-j]>'9'){
				ans[109-i-j]-=10;
				ans[108-i-j]++;
			}
			int look=108-i-j;
			while(ans[look]>'9'){
				ans[look]-=10;
				ans[--look]++;
			}
		}
	}
	return ans;

	
}

string make_palindrome(string in, string center){
	string ans=in;
	ans+=center;
	FOR(i,0,in.size())
		ans+=in[in.size()-1-i];

	return ans;
}

vector <string> ans_list;

void search(int digits, string in,int sum){
	if(in.length()==digits){
		string s=square(make_palindrome(in,""));
		if(is_palindrome(s))
			ans_list.push_back(s);
		s=square(make_palindrome(in,"0"));
		if(is_palindrome(s))
			ans_list.push_back(s);

		s=square(make_palindrome(in,"1"));
		if(is_palindrome(s))
			ans_list.push_back(s);

		s=square(make_palindrome(in,"2"));
		if(is_palindrome(s))
			ans_list.push_back(s);

		s=square(make_palindrome(in,"3"));
		if(is_palindrome(s))
			ans_list.push_back(s);
		return;
	}
	FOR(i,0,4){
		if(in=="" && i==0)
			continue;
		if(sum+i*i<5)
			search(digits,in+(char)('0'+i),sum+i);
		else
			break;
	}
}

int main(){
	FOR(i,0,26){
		cerr<<i<<"\n";
		search(i,"",0);
	}
	cerr<<"complete\n";
	
	sort(ans_list.begin(),ans_list.end());
	cerr<<ans_list[ans_list.size()-1]<<"\n";

	int T;
	cin>>T;

	FOR(counter,0,T){
		cout<<"Case #"<<(counter+1)<<": ";
		string A,B;
		cin>>A>>B;

		while(A.length()<110)
			A="0"+A;
		while(B.length()<110)
			B="0"+B;

		int count=0;
		FOR(i,0,ans_list.size()){
			if(A<=ans_list[i] && B>=ans_list[i])
				count++;
		}

		cout<<count<<"\n";
	}
}
