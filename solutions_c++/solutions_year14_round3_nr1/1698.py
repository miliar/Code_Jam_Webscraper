#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>

using namespace std;

#define PRODUCTION
string input_name = "A-small-attempt0 (2).in";

long long gcd(long long a, long long b)
{
	if(b==0) return a;
	if(a<b) return gcd(b,a);
	return gcd(b, a%b);
}

long long fromString(string str, int start, int end)
{
	long long res = str[start]-'0';
	for(int i = start+1; i<end;i++)
	{
		res*=10;
		res+=str[i]-'0';
	}
	return res;
}

bool is2pow(long long int x)
{
	if(x==0 || x==1) return true;
	if(x%2 != 0) return false;
	return is2pow(x/2);
}

void run()
{
	string str;
	cin>>str;
	int pos = str.find('/');
	
	long long P = fromString(str,0,pos);
	long long Q = fromString(str,pos+1,str.length());

	int D = gcd(P,Q);
	P/=D;
	Q/=D;

	if(!is2pow(Q))
	{
		cout<<"impossible\n";
		return;
	}

	int res = 0;
	while(P<Q) 
	{
		res++;
		P*=2;
	}

	cout<<res<<endl;
}


int main()
{
#ifdef PRODUCTION 
	string output_name = "output.txt";
	freopen(input_name.c_str(),"r",stdin);
	freopen(output_name.c_str(),"w",stdout);
#endif

	long long int test;
	cin>>test;
	for(long long int i = 1;i<=test;i++)
	{
		cout<<"Case #"<<i<<": ";
		run();
	}
	return 0;
}