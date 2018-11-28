#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int main(){
	int n,f1,f2,t;
	int a1[10][10],a2[10][10];

	
	cin>>t;
	
	for(int i=1;i<=t;++i){
		bool freq[20];
		int cnt=0;
		int op;
		memset(freq,0,sizeof freq);
		cin>>f1;
		for(int j=0;j<4;++j)
			for(int k=0;k<4;++k){
				cin>>a1[j][k];
				
				if(j==f1-1)
					freq[a1[j][k]] = true;
			}

		cin>>f2;
		for(int j=0;j<4;++j)
			for(int k=0;k<4;++k){
				cin>>a2[j][k];
				if(j==f2-1 && freq[a2[j][k]])
					cnt++,op = a2[j][k];
			}
		
		if(cnt==0)
			printf("Case #%d: Volunteer cheated!\n",i);
		else if(cnt==1)
			printf("Case #%d: %d\n",i,op);
		else
			printf("Case #%d: Bad magician!\n",i);
	}
		
	return 0;
}
