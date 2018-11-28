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
	int i,x,t,a,j,b,n;
	int A[4][4];
	int B[4][4];
	int hash1[17];
	int hash2[17];
	cin>>t;
	for(x=1;x<=t;x++)
	{
		int ans=0;
		memset(hash1,0,sizeof(hash1));
		memset(hash2,0,sizeof(hash2));
		cin>>a;
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				cin>>A[i][j];
		cin>>b;
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				cin>>B[i][j];
		for(j=0;j<4;j++)
		{
			hash1[A[a-1][j]]++;
			hash2[B[b-1][j]]++;
		}
		int pos=0;
		for(i=0;i<=16;i++)
		{
			if(hash1[i]!=0 && (hash1[i]==hash2[i]))
			{
				ans++;
				pos=i;
			}
		}
	//	cout<<ans<<endl;
		if(ans==1)
			cout<<"Case #"<<x<<": "<<pos<<endl;
		else if(ans==0)
			cout<<"Case #"<<x<<": Volunteer cheated!"<<endl;
		else if(ans>1)
			cout<<"Case #"<<x<<": Bad magician!"<<endl;
	}
	return 0;
}
