/*
                ================================
                Author : Adnaan 'Zohran' Ahmed
                Handle: adnaan1703
                Heritage Institute of Technology
                ================================
*/

#include <bits/stdc++.h>

#define MOD 1000000007
#define PI 3.1415926535897932384626433832795
#define INF LONG_MAX
#define X first
#define Y second
#define pb push_back

using namespace std;

typedef vector<int> vint;
typedef vector<long long int> vlint;
typedef vector<vector<int> > vvint;
typedef vector<vector<long long int> > vvlint;
typedef long long int lint;

void solve(int);

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

	
	
    	freopen("inp2.in", "r", stdin);
    	freopen("out2.txt", "w", stdout);
	
	

    int t = 1;
    cin>>t;
    for(int i=1; i<=t; i++)
    	solve(i);
	return 0;
}

void solve(int test)
{
	int n;
	cin>>n;
	string str;
	cin>>str;

	int sum = 0;
	int counter = 0;
	int tmp;
	for(int i=0; i<n; i++)
	{
		tmp = (int)(str.at(i) - '0');
		sum+=tmp;
		tmp = i+1 - sum;
		if(tmp > 0)
		{
			sum+=tmp;
			counter+=tmp;
		}
	}
	cout<<"Case #"<<test<<": "<<counter<<endl;
}