//ckpeteryu
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<string>
#include<cmath>
#include<vector>
#include<queue>
#include<algorithm>

using namespace std;

int main()
{
	FILE *file;
	file = fopen("pa.out", "w");
	
	int numCases;
	
	//int r;
	//int t;	
	long long int r, t;
	//long long unsigned int rollingSum;
	int cnt=1;
	int flag=1;	
	scanf("%d", &numCases);		
	
	for (int i=0; i<numCases; i++){
		//scanf("%d%d", &r, &t);		
		cnt=1;
		flag=1;
		scanf("%lld%lld", &r, &t);
		t-=(2*r+1);									
		
		while(flag){
			t-=(2*r+(cnt*2+1)+(cnt*2));
			//printf("<%lld>\n", t);
			if (t>=0){				
				cnt++;			
			}else
				flag = 0;
		}		
		//printf("Case #%d: %d\n", i+1, cnt);
		fprintf(file, "Case #%d: %d\n", i+1, cnt);
	}

	fclose(file);	
	return 0;
}


//fprintf(file, "Case #%d: ", );