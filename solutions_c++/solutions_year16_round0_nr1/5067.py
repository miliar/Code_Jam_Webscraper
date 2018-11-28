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

//small testcase
int main()
{
	long long flag = 0,n,i=0,j,x,y,m,input,ans,testcase;
	int T=0;
	long long sum = 0,currentNumber,temp;
	freopen ("d:/Codejam/A-large.in","r",stdin);
	freopen ("d:/Codejam/A-large.out","w",stdout);
	cin>>testcase;
	int digit[11];
	while(testcase--){
		
		cin>>input;

		if(input == 0){
		printf("Case #%d: ",++T);
		cout<<"INSOMNIA\n";
		continue;
		}

		currentNumber = input;
		memset(digit,0,sizeof digit);
		i=1; sum = 0;
		while(true){
			temp = currentNumber;
			while(currentNumber){
				x = currentNumber%10;
				if(!digit[x]){
				digit[x]=1;
				sum++;
				}
				currentNumber/=10;
			}
			if(sum == 10){
				currentNumber = temp;
				break;
			}
			i++;
			currentNumber= input*i;

		}

		printf("Case #%d: ",++T);
		cout<<currentNumber<<"\n";
	}
	
	return 0;
}
