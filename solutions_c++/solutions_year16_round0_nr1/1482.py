#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <set>

using namespace std;

void put(int n, set<int> &s)
{
	while(n>0){
		s.insert(n%10);
		n/=10;
	}
}

int main()
{
	int T;
	scanf("%d",&T);
	for(int tnum=1; tnum<=T; ++tnum)
	{
		set<int> st;
		int N;     
		scanf("%d",&N);
		printf("Case #%d: ",tnum);
		if(N==0)
			printf("INSOMNIA\n");
		else{
			put(N,st);
			int N1=N;
			while(st.size()<10){
				N1+=N;
				put(N1,st);
			}             
			printf("%d\n",N1);
		}
	}
}