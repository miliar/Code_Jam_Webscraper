#include <cstdio>
#include <sstream>
#include <vector>
#include <list>
#include <cmath>
#include <algorithm>
#include <numeric>
#include <iostream>
#include <functional>
#include <cstdlib>
#include <stack>
#include <queue>
#include <deque>
#include <string>
#include <climits>
using namespace std;
//
#define mAX 9999999999999
#define pi 3.14159265358979323846264338327950288419716939
#define  print "Case #"<<t1<<": "

typedef unsigned long long ull;
typedef long double ld;
typedef long long ll;
typedef vector<long long>vi;
typedef vector<long double> vd;
typedef vector<string> vs;
typedef deque<long long> di;
typedef vector<vector <long long> > vvi;
//
int fromDecimal(int n, int b){int r=0,m=0;while(n>0){r+=n%b*m; m*=10; n/=b;} return r;}
string fromDecimal2(int n, int b){  string chars="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";  string result=""; while(n>0) {  result=chars.at(n%b) + result; n/=b; }  return result;}
int toDecimal(int n, int b){ int r=0;int m=0; while(n>0){ r+=n%10*m; m*=b; n/=10; } return r; }
int GCD(int a, int b){ if (b==0) return a; return GCD(b,a%b);}
int LCM(int a, int b) {  return b*a/GCD(a,b); }
string DoubleToString(double val, string precession)
{
	char str[256];
	string format = "%" + precession;
	sprintf(str, format.c_str(), val);

	return string(str);
}
int ToInt(string data)
{
	int n;
	istringstream is( data );
	is >> n;

	return n;
}


double ToDouble(string data)
{
	double n;
	istringstream is( data );
	is >> n;

	return n;
}

bool isPrime(ll n)
{
	if(n <= 1) return false;
	if(n == 2 || n == 3) return true;
	if(n%2 == 0) return false;

	long long count = sqrt((double)n);
	for(long long i = 2; i <= count; i+=2)
	{
		if(n % i == 0)
			return false;
	}

	return true;
}

vector<ll> getPrimeNumberList(ll n)
{
	vector<ll> list;

	ll * sPrime = new ll [n + 1];
	fill_n(sPrime, n+1, 1);
	sPrime[0] = 0;
	sPrime[1] = 0;
	ll m = sqrt((double)n);

	for(ll i = 2; i<=m; i++)
	{
		if(sPrime[i])
		{
			for(ll k = i*i; k<=n; k+=i)
				sPrime[k] = 0;
		}
	}

	for(ll j = 0; j<=n+1; j++)
	{
		if(sPrime[j])
			list.push_back(j);
	}
	
	delete [] sPrime;

	return list;
}

vector<string> split(string str, char delim)
{
	vector<string> list;
	std::stringstream ss(str);
    std::string item;
    while (std::getline(ss, item, delim)) {
        list.push_back(item);
    }

	return list;
}

//
bool isCon(string s,int n)
{
	int count=0;
	for(int i=0;i<s.size();i++)
	{
		count=0;
		if(( s[i]=='a') || (s[i]=='e') || (s[i]=='i') || (s[i]=='o') || (s[i]=='u'))
			continue;
		else
		{
			count++;
			if(count==n) return true;

			for(int j=i+1;j<s.size();j++)
			{
				
				if ((s[j]=='a') || (s[j]=='e') || (s[j]=='i') || (s[j]=='o') || (s[j]=='u'))
				{
					i=j;
					break;
				}
				else
				{
					count++;
				}
				if(count==n) return true;
			}
		}
	}
	return false;
}
void main()
{
	freopen("input.txt","r",  stdin);
	freopen("output.txt", "w", stdout);
	int T;
	cin>>T;
	for(int t1=1;t1<=T;t1++)
	{
		string s;
		int n;
		cin>>s;
		cin>>n;
		ll value=0;
		for(int i=0;i<s.size();i++)
		{
			int j=s.size()-i;
			while(j>=n)
			{
				string sub;
				sub=s.substr(i,j);
				if(isCon(sub,n))
					value++;
				j--;
			}

		}
		cout<<print<<value<<endl;
	}//end of t
}