// =====================================================================================
//       Filename:  A.cpp
//    Description:  
//        Created:  05/12/2013 02:30:43 PM
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

#define FOR(i,a,b) for(typeof((a)) i=(a); i <= (b) ; ++i)       
#define FOREACH(it,x) for(typeof((x).begin()) it=(x).begin(); it != (x).end() ; ++it)   
#define LMAX 101


using namespace std;

typedef pair<int,int> PI;
typedef vector<PI> VI;

char str[LMAX];

int n=0;

int solve(){
//	printf("%s %d\n",str,n);

	int len=strlen(str),c=0,ans=0;

	FOR(i,0,len-1){
		FOR(j,i+n,len){
			c=0;
			
			FOR(k,i,j-1){
				if(
					str[k]=='a' ||
					str[k]=='e' ||
					str[k]=='i' ||
					str[k]=='o' ||
					str[k]=='u' 
				){
					c=0;
				}else{
					c++;
				}

				if(c>=n){
					ans++;
					break;
				}
			}
		
			
		}
	}


	return ans;
}


int main(){
	int T=0;
	scanf("%d",&T);
	FOR(t,1,T){
		scanf("%s",str);
		scanf("%d",&n);
		printf("Case #%d: %d\n",t,solve());
	}

	return 0;
}

