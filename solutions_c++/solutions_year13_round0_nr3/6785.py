#include<cstdio>
#include<math.h>
#include<vector>
#include<set>
#include<algorithm>
using namespace std;
int T,r,t[100];
int A, B;
vector<int> v;
int main(void){
	scanf("%d",&T);
	for(int i=1;i<=32;i++){
		int l=0, n=i,f=1;
		while(n>0){
			t[l++]=n%10; n/=10;
		}
		for(int j=0;j<l/2;j++){
			if(t[j]!=t[l-j-1]){f=0;break;}
		}
		if(f) v.push_back(i*i);
	}
	for(int Z=1;Z<=T;Z++){ r=0;
		scanf("%d %d",&A,&B);
		for(int i=0;i<v.size();i++){
			if(v[i]<A) continue;
			if(v[i]>B) break;
			int l=0, n=v[i],f=1;
//			printf("n:%d\n",n);
			while(n>0){
				t[l++]=n%10; n/=10;
			}
			for(int j=0;j<l/2;j++){
				if(t[j]!=t[l-j-1]){f=0; break;}
			}
			if(f){ r++;}
		}		
		printf("Case #%d: %d\n",Z,r);
	}
	return 0;
}
