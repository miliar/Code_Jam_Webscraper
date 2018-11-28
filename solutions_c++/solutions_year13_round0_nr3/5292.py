#include<algorithm>
#include<functional>
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<string>
#include<sstream>
#include<iostream>
#include<iomanip>
#include<vector>
#include<list>
#include<stack>
#include<queue>
#include<map>
#include<set>
#include<bitset>
#include<climits>

#define all(c) (c).begin(), (c).end()
#define rep(i,n) for(int i=0;i<(n);i++)
#define pb(e) push_back(e)
#define mp(a, b) make_pair(a, b)
#define fr first
#define sc second

typedef unsigned long long ull;
typedef long long ll;

const int INF=100000000;
int dx[4]={1,0,-1,0};
int dy[4]={0,1,0,-1};

using namespace std;

typedef pair<int ,int > P;

bool check(int a)
{
	ostringstream os;
	os<<a;
	string str=os.str(),str1,str2;

	int b=str.size();
	str1=str.substr(0,b/2);
	str2=str.substr(b/2+b%2,b);
	reverse(all(str2));

	return (str1==str2);

}
int small_solve()
{
	vector<int> vec;
	rep(i,34) vec.pb(i*i);
	bool f[1030];
	fill(f,f+1030,false);
	rep(i,vec.size())
		f[vec[i]]=(check(i)&&check(vec[i]));

	int a,b;
	cin>>a>>b;

	int ans=0;
	for(int i=a;i<=b;i++)
	{
		if(f[i])
		{
			ans++;
		}
	}
	return ans;

}

int main()
{
	int t;
	cin>>t;

	FILE*fp=fopen("C:/Users/odan/Documents/app/vim/GCJ/ans3.txt","w");
	
	rep(i,t)
		fprintf(fp,"Case #%d: %d\n",i+1,small_solve());

	fclose(fp);

	return 0;
}


