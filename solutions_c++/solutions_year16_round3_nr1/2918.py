#include<iostream>
#include<stdio.h>
#include<cstring>
#include<cstdio>
#include<stdlib.h>
#include<sstream>
#include<list>
#include<math.h>
#include<map>
#include<set>
#include<cstdlib>
#include<cctype>
#include<cmath>
#include<fstream>
#include<vector>
#include<algorithm>
#include <queue>
#include<string>
#include<cstring>
#include <deque>
#include<stack>
#include <array>
using namespace std;


#define ALL(a) a.begin(),a.end()
#define CLR(a) memset(a,0,sizeof(a))
#define PB push_back
#define PI acos(-1.0)
#define SET(a) memset(a,-1,sizeof(a))
#define ALL_BITS ((1 << 31) - 1)
#define NEG_BITS(mask) (mask ^= ALL_BITS)
#define TEST_BIT(mask, i) (mask & (1 << i))
#define ON_BIT(mask, i) (mask |= (1 << i))
#define OFF_BIT(mask, i) (mask &= NEG_BITS(1 << i))
#define max3(a,b,c) max(a,max(b,c))
#define min3(a,b,c) min(a,min(b,c))
long long GCDFast(long long a,long long b){   while(b)b^=a^=b^=a%=b;  return a;   }
#define MOD 1000000007
#define MX 100010
#define pii pair<int,int>
#define LL long long
// UP, RIGHT, DOWN, LEFT, UPPER-RIGHT, LOWER-RIGHT, LOWER-LEFT, UPPER-LEFT
int dx[8] = {-1, 0, 1, 0, -1, 1,  1, -1};
int dy[8] = { 0, 1, 0,-1,  1, 1, -1, -1};

/*
#define N 200000002
bool prime_number[N];
long long prime_num[11078937];
int size;
void prime()
{
int i = 0 ,limit = (int)sqrt((double)N), x = 0,j = 0,y;
memset(prime_number,true,sizeof(prime_number));
for(x = 2 ; x <= limit; x++)
{
if(prime_number[x] == true)
{
y = N/x;
for(i = 2 ; i <= y ;i++)
prime_number[i*x] = false;
}
}
for(x = 2,i = 0 ; x <= N; x++)
if (prime_number[x])
{
prime_num[i] = x;
i++;	
}
size = i;
}
*/

int main()
{
	long long flag = 0,n,i=0,j,x,y,m,input,ans,testcase;
	int T=0,index,k;
	long long sum = 0,temp;
	freopen ("d:/Codejam/A-small-attempt1.in","r",stdin);
	freopen ("d:/Codejam/A-small-attempt1.out","w",stdout);

	string str;
	long long number=0;
	int a[30];
	cin>>testcase;
	while(testcase--){
		cin>>n;

		pair<int,char>P[30];

		for(i=0;i<n;i++){
			cin>>P[i].first;
			P[i].second = i+'A';
		}

		
		set<int>X;
		set<int>::iterator it;

		printf("Case #%d: ",++T);
		flag =1;
		sort(P,P+n);
		while(flag){
			flag  = 0;
			i=n-1;
			{
				if(P[i].first>1 && P[i-1].first >1){
					flag =1;
					P[i].first--;
					P[i-1].first--;
					cout<<P[i].second<<P[i-1].second<<" ";
				}
				else if(P[i].first==1){
					;//X.insert(i);
					//P[i].first--;
				}
			}
			sort(P,P+n);
		}

		for(i=0;i<n;i++)
			if(P[i].first){
				if(P[i].first %2 ==0){
					while(P[i].first){
					cout<<P[i].second<<P[i].second<<" ";
					P[i].first-=2;
					}
				}
				else
					X.insert(i);
			}

		if(X.size()%2 != 0){
			it = X.begin();
			x = *it;
			cout<<P[x].second<<" ";
			X.erase (it);
		}

		for(it = X.begin();it!=X.end();){
			x = *it;
			it++;
			y = *it;
			it++;
			cout<<P[x].second<<P[y].second<<" ";
		}
		cout<<"\n";
	}

	return 0;
}
