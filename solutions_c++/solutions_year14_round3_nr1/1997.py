/*--------------------- Author - Akshit ----------------------*/

#include<iostream>
#include<cstdio>
#include<cmath>
#include<string>
#include<cstring>
#include<algorithm>
#include<vector>
#include<stack>
#include<list>
#include<queue>
#include<cstdlib>
#include<numeric>
#include<set>
#include<map>
#include<deque>
#include<climits>
#include<cassert>
#include<cctype>
#include<ctime>
#include<iterator>
#include<iomanip>
#include<functional>
#include<fstream>
#include<ostream>
#include<istream>
#include<sstream>
using namespace std;

#define sf(n)                scanf("%d",&n) 
#define pf(n)                printf("%d",n)          
#define pfln(n)              printf("%d\n",n)         

#define vi                   vector <int > 
#define pb                   push_back()
#define debug(in)             printf("n = %d\n",n)
#define PI 3.14159265358979
#define LL 1000000007

long long StringToNumber (  string &Text )
{               
	stringstream ss(Text);
	long long result;
	return ss >> result ? result : 0LL;
}
long long int gcd(long long a, long long b ){
	if(a%b == 0)
		return b;
	else
		return gcd(b,a%b);
}
int isPowerOfTwo (int x)
{
	 while (((x % 2) == 0) && x > 1) /* While x is even and > 1 */
		    x /= 2;
	  return (x == 1);
}
int main()
{
	std::ios_base::sync_with_stdio(false);
	int t,no;
	no = 1; 
	cin>>t;
	while(no<=t){
		string s;
		string s1;string s2;s1.clear();s2.clear();
		cin>>s;
		int i;
		for( i = 0 ; s[i]!='/' ; i++){
			s1+=s[i];
		}
		int idx = i;
		for(int j = idx+1 ; j<s.size() ; j++){
			s2+=s[j];
		}
		//cout<<"s1 = "<<s1<<"  s2 = "<<s2<<endl;
		bool flag = 0;
		long long int p = StringToNumber(s1);long long int q = StringToNumber(s2);
		long long div = gcd(p,q);
		p/=div;q/=div;
		int gen = 0;
		if(isPowerOfTwo(q) == 0)
		{
			cout<<"Case #"<<no<<": "<<"impossible\n";
			flag = 1;
		}

		double cal;
		double num = (double)p;
		double den = (double)q;
		int ans = 0;
		cal = 2.0*(num/den);
		while(1){
			gen++;
			if(cal >= 1.00000000){
				ans = gen;
				break;
			}
			cal = 2.0*cal; 
			if(gen >40){
				cout<<"Case #"<<no<<": "<<"impossible\n";
				flag = 1;
				break;}
		}
		//cout<<p<<" "<<q<<endl;
		if(flag == 0)
			cout<<"Case #"<<no<<": "<<ans<<endl;
		no++;
	}
	return 0;
}
