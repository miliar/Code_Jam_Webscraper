// =====================================================================================
//       Filename:  C_tweak.cpp
//    Description:  
//        Created:  04/14/2013 12:30:48 AM
//         Author:  BrOkEN@!
// =====================================================================================

#include<fstream>
#include<iostream>
#include<sstream>
#include<bitset>
#include<deque>
#include<list>
#include<map>
#include<queue>
#include<set>
#include<stack>
#include<vector>
#include<algorithm>
#include<iterator>
#include<string>
#include<cassert>
#include<cctype>
#include<climits>
#include<cmath>
#include<cstddef>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<ctime>

#define TIMER 1
#define FOR(i,a,b) for(typeof((a)) i=(a); i <= (b) ; ++i)       
#define FOREACH(it,x) for(typeof((x).begin()) it=(x).begin(); it != (x).end() ; ++it)   
#define MAX 101


using namespace std;

typedef pair<int,int> PI;
typedef vector<PI> VI;
typedef unsigned long long int __int64;

__int64 A=0ULL,B=0ULL;

__int64 tab[40]={0,1, 2, 3, 11, 22,101, 111, 121, 202, 212,1001, 1111, 2002, 10001, 10101,10201, 11011, 11111, 11211, 20002, 20102, 100001, 101101, 110011, 111111,200002, 1000001, 1001001, 1002001, 1010101,1011101, 1012101, 1100011, 1101011, 1102011, 1110111, 1111111, 2000002, 2001002};

int solve(){

	
//	printf("%llu %llu\n",a,b);
	
	int count=0;
	
	FOR(i,0,40){
		if(A<= tab[i]*tab[i] && tab[i]*tab[i]<=B){
			count++;
		}
	}
	
	return count;
}


int main(){
	int T=0;
	scanf("%d",&T);
	FOR(t,1,T){
		scanf("%llu %llu",&A,&B);
		printf("Case #%d: %d\n",t,solve());
	}


	return 0;
}

