//UESTC_L3

#include <stdexcept>
#include <cstdarg>
#include <iostream>
#include <fstream>
#include <exception>
#include <memory>
#include <locale>
#include <sstream>
#include <set>
#include <list>
#include <bitset>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <string>
#include <utility>
#include <cctype>
#include <climits>
#include <cassert>
#include <cstdio>
#include <cstring>
#include <map>
#include <cmath>
#include <algorithm>
#include <ctime>
#include <vector>
#include <queue>
#include <deque>
#include <cstdlib>
#include <stack>
#include <iterator>
#include <functional>
#include <complex>
#include <valarray>
using namespace std;

int n;
int f[110][110];
char str[110][110];

int main(){
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A.out","w",stdout);
	
	int test;
	scanf("%d",&test);
	
	int ct=0;
	while(test--){
		memset(f,0,sizeof(f));
		scanf("%d",&n);
		string final[110];
		
		int now;
		for(int i=0;i<n;i++){
			scanf("%s",str[i]);
			int len=strlen(str[i]);
			now=0;
			for(int j=0;j<len;j++){
				if(j==0)final[i].push_back(str[i][j]);
				else{
					if(str[i][j]==final[i][now])f[i][now]++;
					else{
						final[i].push_back(str[i][j]);
						now++;
					}
				}
			}
		}
		bool judge=true;
		for(int i=1;i<n;i++){
			if(final[i]!=final[i-1]){
				judge=false;
			}
		}
		
		int ret=0;
		if(judge){
			
			for(int i=0;i<=now;i++){
			int ma=0,mi=1000;
			for(int j=0;j<n;j++){
				ma=max(ma,f[j][i]);
				mi=min(mi,f[j][i]);
			}
			ret+=ma-mi;
		}
		}
		printf("Case #%d: ",++ct);
		if(judge){
			printf("%d\n",ret);
		}
		else{
			printf("Fegla Won\n");
		}
	}
	return 0;
}