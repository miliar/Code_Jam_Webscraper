#include <cstdio>
#include <vector>

using namespace std;

int main(){
	int t;
	scanf("%d",&t);
	for(int tc=1;tc<=t;tc++){
		int d;
		scanf("%d",&d);
		vector<int>diners;
		int max_pan=0;
		for(int i=0;i<d;i++){
			int a;
			scanf("%d",&a);
			diners.push_back(a);
			if(a>max_pan){max_pan=a;}
		}
		int best=1e9;
		for(int k=1;k<=max_pan;k++){
			//k is the target number of pancakes at maximum
			int sum=k;
			for(int i=0;i<d;i++){
				sum+=(diners[i]+k-1)/k-1;
			}
			fprintf(stderr,"%d %d\n",k,sum);
			if(sum<best){best=sum;}
		}
		printf("Case #%d: %d\n",tc,best);
	}
}
