
//main includes
#include<iostream>
#include<cstdio>
#include<cstring>
#include<ctime>
#include<cmath>


//other includes
#include<algorithm>
#include<climits>
#include<vector>
#include<queue>
#include<stack>
#include<bitset>
#include<set>
#include<deque>
#include<cstdlib>
#include<map>
#include <utility>

#define re



using namespace std;

#define FOR(a,b)        for(__typeof(b) i=(a);i<(b);i++)
#define ll long long 

int n,t;
string s;
void preprocess()
{
}

bool isConsonant(char ch)
{
	if(ch == 'a'|| ch == 'e' | ch == 'i' || ch == 'o' || ch=='u')
		return false;
	return true;
}

ll solve()
{
	int l = s.length();
	int prev = -1;
	ll count = 0;
	ll found = 0;
	int temp = 0;
	for(int i=0;i<n-1;i++)
	{
		if(isConsonant(s.at(i)))
		{
			temp++;
		}
		else
		{
			temp = 0;
		}
	}
	for(int i=n-1;i<l;i++)
	{
		if(isConsonant(s.at(i)))
		{
			temp++;
			if(temp == n)
			{
				count += (i-n-prev+1)*(l-i);
				temp--;

				prev = i-n+1;
			}
			
		}
		else
				temp = 0;
	}
	return count;
}


int main(){
#ifdef re
freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);
freopen("log.txt","w",stderr);
#endif

cin>>t;
for(int i=1;i<=t;i++)
{
	cin>>s>>n;
	cout<<"Case #"<<i<<": "<<solve()<<endl;
}

#ifdef re
//printf("\n  Time Taken  %.31f sec\n",(double)clock()/(CLOCKS_PER_SEC));

#endif
return 0;
}

