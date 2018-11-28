#include <stdio.h>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <cstring>
#include <string>
#include <cmath>
#include <cassert>
#include <ctime>
#include <algorithm>
#include <sstream>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <cstdlib>
#include <cstdio>
#include <iterator>
#include <functional>
#include <bitset>


#define TASK   "D-small"

using namespace std;

void solve(){

	double temp;
	vector<double> Naomi,Ken;
	vector<double> NaomiDW,KenDW;
	
	int war=0;
	int deceitfulWar=0;
	
	int N;

	scanf("%d",&N);
	
	for(int i=0; i<N; i++){
		scanf("%lf",&temp);		Naomi.push_back(temp);
	}

	for(int i=0; i<N; i++){
		scanf("%lf",&temp);		Ken.push_back(temp);
	}
	
		sort(Naomi.begin(), Naomi.end());
		sort(Ken.begin(), Ken.end());
		
		NaomiDW.assign(Naomi.begin(), Naomi.end());
		KenDW.assign(Ken.begin(), Ken.end());

	
	for(int i=1;i<=N;i++){
		if(NaomiDW.front() < KenDW.front())
		{
			NaomiDW.erase(NaomiDW.begin());
			KenDW.pop_back();
			
		}
		else{
			deceitfulWar = deceitfulWar + 1;
			NaomiDW.erase(NaomiDW.begin());
			KenDW.erase(KenDW.begin());		
		}		
	}
	
	for(int i=1;i<=N;i++){
		if(Naomi.back() > Ken.back())
		{
			war = war + 1;
			Naomi.pop_back();
			Ken.erase(Ken.begin());
			
		}else{
			Naomi.pop_back();
			Ken.pop_back();
		}
	}
	
		printf("%d %d\n",deceitfulWar,war);	
	
}



int main(int argc, char **argv)
{
	freopen(TASK".in","r",stdin);
	freopen(TASK".out","w",stdout);
		
	char buf[1000];
	int testNum;
	gets(buf);
	sscanf(buf,"%d",&testNum);

	for (int testId = 1; testId <= testNum; testId++){
		
		printf("Case #%d: ",testId);
		solve();
		
	}	
	
	return 0;
}
