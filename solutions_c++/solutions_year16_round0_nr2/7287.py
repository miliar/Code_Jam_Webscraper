#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <climits>
 
#define MAXSIZE 10000000
#define oo 1000000000
#define WHITE 0
#define GREY 1
#define BLACK 2
#define X first
#define Y second
 
#ifndef MAX
#define MAX(a,b) (a>b)?a:b
#endif
 
#ifndef MIN
#define MIN(a,b) (a>b)?b:a;
#endif
 
using namespace std;
 
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<float> vf;
 
 
int main() {
	// your code goes here
	int t;
	cin>>t;

	int j = t;
	while(t--){
		string s;
		cin>>s;
		int len = s.size();
		int i = 0;
		while(i<len && s[i]=='-') i++;
		int count = 0;
		if(i>0) count++;


		while(i<len){
			if(s[i]=='+') i++;
			else {
				count+=2;;
				while(i<len && s[i]=='-') i++;
			}
		}


		cout<<"Case #"<<(j-t)<<": "<<count<<"\n";

	}
	return 0;
}
