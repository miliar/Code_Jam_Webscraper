#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cstdlib>
#include <ctime>
#include <cstdio>
#include <functional>
#include <set>
#include <sstream>
#include <map>
#include <queue>
#include <stack>

using namespace std;

string get_bin(long long x){
	string res;
	while(x){
		res=(char)(x%2+'0')+res;
		x/=2;
	}
	return res;
}

long long interpret(string s,int base){
	long long res=0;
	for(int i=0;i<s.size();i++){
		res=res*base+(s[i]=='1');
	}
	return res;
}

// x is not prime( base 2~10 )
bool solve(long long x){
	string s=get_bin(x);

	vector<long long> ans;
	for(int base=2;base<=10;base++){
		long long num=interpret(s,base);
		for(long long d=2;d*d<=num;d++){
			if(num%d==0){
				ans.push_back(d);
				break;
			}
		}
	}
	
	
	if(ans.size()==9){
		cout<<s;
		for(int i=0;i<9;i++) cout<<" "<<ans[i];
		cout<<endl;
		/*
		for(int i=2;i<=10;i++){
			cout<<i<<" "<<interpret(s,i)<<endl;
		}
		*/
		
		return true;
	}else{
		return false;
	}
	
}

int main()
{
		
	int n,t,j;
	cin>>t>>n>>j;
	
	cout<<"Case #1:"<<endl;

	for(int x=(1<<(n-1))+1;j;x+=2){
		if(solve(x)) j--;
	}
    
    return 0;
}