#include <cstring>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
#include <climits>
#include <cctype>
#include <bitset>
#include <list>
#include <fstream>
using namespace std;
typedef	long long ll;
typedef unsigned long long ULL;
#define all(v) ((v).begin()),((v).end())
#define sz(v) ((int)((v).size()))
#define PI(n) ((double)acos(n))
#define pw2(n) (1LL<<(n))
int dx8[8] = { 1, -1, 0, 0, 1, 1, -1, -1 };
int dy8[8] = { 0, 0, 1, -1, 1, -1, 1, -1 };
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	cin >> t;
	for(int i=1;i<=t;i++){
		string x;
		cin >> x;
		cout << "Case #"<<i<<": ";
		int c = 0,c2=0;
		if(count(all(x),'-')==0){
			cout<<0<<endl;
			continue;
		}
		string y;
		int j;
		for(j=x.size()-1;j>=0;j--)
		  if(x[j]=='-') break;
		for(int ii=0;ii<=j;ii++)
		  y+=x[ii];
			 x=y;
		for(int j=0;j<x.size();j++){
			if(x[j]=='+'){
				while(x[++j]=='+');
				c++;
			}
		}
		for(int j=0;j<x.size();j++){
			if(x[j]=='-'){
				while(x[++j]=='-');
				c2++;
			}
		}
		cout<<c+c2<<endl;
		
	}
}

