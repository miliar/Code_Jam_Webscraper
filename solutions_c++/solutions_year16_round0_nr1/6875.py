#include <cstdio>
#include <iostream>
#include <algorithm>

#define SZ 1000000
using namespace std;

int Ans[SZ+7];

int AddMask(int no) {

	int mask = 0;
	while(no!=0) {
		mask = ( (mask) | (1<<(no%10)) );
		no /= 10;
	}
	return mask;
}

void Init()
{
	int mx = 0;
	for(int i=1;i<=SZ;i++) {
		int mask = 0;
		int no = i;
		int iter = 0;
		while(mask != ( (1<<10)-1) ) {
			iter++;
			no = i*iter;
			mask = (mask | AddMask(no) );
			//cout<<no<<" ," <<mask<<endl;
		}
		//mx = max(mx,iter);
		Ans[i] = no;
		//cout<<i<<" "<<no<<" "<<iter<<endl;

	}
	//cout<<mx<<endl;
}


int main()
{
	Init();
	freopen("A2.txt","rt",stdin);
	freopen("Aout2.txt","wt",stdout);
	int tst,n,cas=0;
	scanf("%d",&tst);
	while(tst--) {
		cas++;
		scanf("%d",&n);
		if(n!=0) printf("Case #%d: %d\n",cas,Ans[n]);
		else printf("Case #%d: INSOMNIA\n",cas);
	}


	return 0;
}