//Common headers
#include<iostream>
#include<vector>
#include<utility>
#include<algorithm>
#include<string>
#include<cstdio>

using namespace std;


#define traverse(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define rtraverse(container, it) for(typeof(container.rbegin()) it = container.rbegin(); it != container.rend(); it++)
#define efor(i,a,b)               for(int i=a;i<b;i++)

#define TOLERANCE 10e-5
#define MOD 1000000007

typedef unsigned long long ull;
typedef std::pair< int, int > ipair;


int main(){
	ios_base::sync_with_stdio(false);
	int testCases= 0;
	cin>>testCases;
	char c;
	int smax;
	for(int tc=1;tc<=testCases;tc++){
		cin >> smax;
		smax++;
		int S[smax];
		
		
		efor(i,0,smax){
			cin>> c;
			S[i] = c-'0';
		}
		
		int cs=0;//so far
		int added = 0;
		efor(i,0,smax){
			if(i>cs){
				added+=i-cs;
				cs+= i-cs;
			}
			cs+= S[i];
		}
		
		printf("Case #%d: %d\n",tc, added);
	}
	
	return 0;
}