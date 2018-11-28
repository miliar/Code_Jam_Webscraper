#include <iostream>
#include <string>
using namespace std;
int T;
string S;


long long solve()
{
	long long ret=0;
	int begin=0;
	int end=S.length()-1;
	
	bool wentIn= false;
	while(S[end] == '+'){
		wentIn=true;
		--end;
		if(end<begin){
			return ret;
		}
	}

	wentIn = false;
	while(S[begin] == '-'){
		wentIn = true;
		++begin;
		if(begin>end){
			ret += 1;
			return ret;
		}
	}
	if(wentIn){
		ret += 1;
	}

	//come from right
	for(;;){
		wentIn = false;
		while(S[end] == '-'){
			wentIn = true;
			--end;
			if(end<begin){
				ret += 2;
				return ret;
			}
		}

		while(S[end] == '+'){
			wentIn = true;
			--end;
			if(end<begin){
				ret += 2;
				return ret;
			}
		}
		if(wentIn){
			ret += 2;
		}

		wentIn = false;
		while(S[begin] == '+'){
			wentIn = true;
			++begin;
			if(begin>end){
				ret += 2;
				return ret;
			}
		}
		while(S[begin] == '-'){
			wentIn = true;
			++begin;
			if(begin>end){
				ret += 2;
				return ret;
			}
		}
		if(wentIn){
			ret += 2;
		}

	}

	return 0;
}
int main()
{
	cin>>T;
	for(int xx=1; xx<=T; ++xx){
		cin>>S;
		long long ret = solve();
		cout<<"Case #"<<xx<<": "<<ret<<endl;
	}
	return 0;
}
