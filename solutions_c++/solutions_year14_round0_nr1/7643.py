#include <bits/stdc++.h>
using namespace std;
#define oo (1<<30)
#define sz(v) (int)v.size()

int main(){
#ifndef ONLINE_JUDGE
	freopen("A-small-attempt0.in", "rt", stdin);
	freopen("test1.in","wt",stdout);
#endif
	int N;
	cin>>N;
	for(int n=0;n<N;n++){
		int ar[17]={0};

		for(int i=0;i<2;i++){
			int B;
			cin>>B;

			for(int i1=0;i1<4;i1++){
				for(int i2=0;i2<4;i2++){
					int X;
					cin>>X;
					if(i1+1==B)
						ar[X]++;
				}
			}
		}


		int W=0;
		int ans;
		for(int i=1;i<=16;i++)
			if(ar[i]==2)
				W++,ans=i;
		if(W==0)
			printf("Case #%d: Volunteer cheated!\n",n+1);

		else if(W==1)
			printf("Case #%d: %d\n",n+1,ans);
		else
			printf("Case #%d: Bad magician!\n",n+1);
	}

	return 0;
};
