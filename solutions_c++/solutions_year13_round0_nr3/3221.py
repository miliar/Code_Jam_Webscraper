#include <algorithm>  
#include <iostream>  
#include <sstream>  
#include <string>  
#include <vector>  
#include <queue>  
#include <set>  
#include <map>  
#include <cstdio>  
#include <cstdlib>  
#include <cctype>  
#include <cmath>  
#include <list>  
#include <cassert>
#include <cstring>
using namespace std; 

long long size=1000;
bool isp[1001];

string numberToString ( long long n )
{
	ostringstream ss;
	ss << n;
	return ss.str();
}

bool isPalindrome(string s) {
	for (int i = 0; i < s.length() / 2; i++)
    {
        if (s[i] != s[s.length() - 1 - i]) return false;
    }
    return true;
}

void check(){
	memset(isp,false,sizeof(isp));
	string s,ss;
	for(long long i=1;i<=(int)sqrt(size)+1;i++){
		s=numberToString(i);
		long long ii=i*i;
		if(ii<=size){
			ss=numberToString(ii);
			if(isPalindrome(s)&&isPalindrome(ss))
				isp[ii]=true;
		}
	}
}

int main()
{
	string filedir="D:\\Dropbox\\Contest\\Algorithm\\GCJ\\2013Q\\";
    string fname = "C-small-attempt0";
    freopen((filedir+fname+".in").c_str(), "r", stdin);
    freopen((filedir+fname+".out").c_str(), "w", stdout);

	check();

	int T=0;
	cin>>T;

	long long A,B;
	for(int t=1;t<=T;t++){
		cin>>A>>B;
		int count=0;
		for(int i=A;i<=B;i++){
			if(isp[i])
				count++;
		}
		cout<<"Case #"<<t<<": "<<count<<endl;
	}
}