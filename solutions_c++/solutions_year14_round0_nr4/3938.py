/*  AMAN MITTAL
    Computer Science and Engineering Sophomore
    M.N.N.I.T. Allahabad
    INDIA   */
#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <cassert>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <cmath>
#include <numeric>
#include <bitset>
#include <cstdio>
#include <cstring>
#include <limits>

using namespace std;

#define LL long long int
#define LLU long long unsigned int
#define FOR(i,n) for(int i=0;i<n;i++)
#define TEST(t) while(t--)
#define pb push_back
#define REP(i,a,b) for(int i=a;i<=b;i++)
#define getcx getchar_unlocked
#define clr(a,b) memset(a,b,sizeof(a))
#define MAXAR 1100000
#define MOD 1000000007
#define X first
#define Y second

const int mini = numeric_limits<int>::min();
const LL minl = numeric_limits<LL>::min();
const int maxi = numeric_limits<int>::max();
const LL maxl = numeric_limits<LL>::max();

typedef pair<int, int> pii;
typedef pair<int,float> pif;
typedef vector<int>vi;

int gcd(int a,int b){
    if(b==0) return a;
    else return gcd(b,a%b);}

int main()
{
	int i,t,x,j,n,ans1,ans2;
	cin>>t;
	for(x=1;x<=t;x++)
	{
		ans1=0;
		ans2=0;
		cin>>n;
		float boy[n];
		float girl[n];
		for(i=0;i<n;i++)
			cin>>girl[i];
		for(i=0;i<n;i++)
			cin>>boy[i];
		sort(girl,girl+n);
		sort(boy,boy+n);
/*		for(i=0;i<n;i++)
			cout<<girl[i]<<" ";
		cout<<endl;
		for(i=0;i<n;i++)
			cout<<boy[i]<<" ";
		cout<<endl;*/
		i=0;
		j=0;
		while(i!=n && j!=n)
		{
			if(girl[i]>boy[j])
			{
				ans1++;
				j++;
				i++;
			}
			else
				i++;
		}
		i=0;
		j=0;
		while(i!=n && j!=n)
		{
			if(boy[i]>girl[j])
			{
				ans2++;
				j++;
				i++;
			}
			else
				i++;
		}
		cout<<"Case #"<<x<<": "<<ans1<<" "<<(n-ans2)<<endl;
	}
	return 0;
}
