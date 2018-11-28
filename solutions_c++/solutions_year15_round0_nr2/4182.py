#include <iostream>
#include <fstream>
#include <sstream>
#include <ctime>
#include <cmath>
#include <vector>
#include <algorithm>
#include <queue>
#include <string.h>
#include <time.h>
//#include <unistd.h>
using namespace std;


char line[10000];
	

struct entry {	
	int num;
	int rate;
	
		
	int newtime() {
		if (num%(rate+1)==0)
			return (num/(rate+1));
		else
			return 1+(num/(rate+1));
	}
	
	
	int time() {
		if (num%rate==0)
			return (num/rate);
		else
			return 1+(num/rate);
	}
};

int pickmax(vector<entry>& P) {
	int xtime=0;
	int choice=-1;
	
	for (int i=0;i<P.size();i++) {
		int cur_time=P[i].time();
		if (cur_time>xtime) {
			xtime=cur_time;
			choice=i;
		}
	}
	
	return choice;
}


void debug(vector<int>& P,int id) {
	for (int i=0;i<P.size();i++) printf("%d ",P[i]);
	printf("@[%d]\n",id);
}

	
int main(int argc,char*argv[]) {
	int T;
	scanf("%d\n",&T);
	
	
	int D,v;
	char win;
	
	
	vector<entry> P;
	
	
	// greedy?
	
	
	for (int iter=1;iter<=T;iter++) 
	{
		scanf("%d\n",&D);
		
		P.clear();
		for (int i=0;i<D;i++) {
			scanf("%d",&v);
			
			entry e;
			e.num=v;
			e.rate=1;
			
			P.push_back(e);
		}
		scanf("\n");
		
		//for (int i=0;i<D;i++) printf("%d ",P[i]);
		
		
		int total=0; // time used

		while (P.size()>0) {			

			int best=pickmax(P);
			
			
			int bound=P[best].newtime();
			
			int budget=P[best].time()-bound-1; 
			
			
			// make decision
			for (int j=P.size()-1;j>=0;j--)
				if (j!=best)
			{
				if (P[j].time()>bound)
					budget--;
			}
			
			// action
			total++;
			if (budget<=0) { // simulate
				int oldlast=P.size()-1;
				for (int j=oldlast;j>=0;j--) {
					P[j].num-=P[j].rate;
					if (P[j].num<=0) {
						P[j]=P.back();
						P.pop_back();
					}
				}
			} else {
				P[best].rate++;
			}
			
			//debug(P,total);
		}
		
		printf("Case #%d: %d\n",iter,total);
		//printf("@@%d, %d %d %d %d %d\n",D,P[0],P[1],P[2],P[3],P[4]);
	}
	
	return 0;

	
	
/*

9/1=9
1+9/2=6
2+9/3=5
3+9/4=5


*/	
	
}