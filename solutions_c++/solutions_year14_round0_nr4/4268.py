#include <iostream>
#include <stdlib.h>
#include <math.h>
#include <cstdio>
#include <algorithm>

using namespace std;

int main() {
	int t,nn,w,dw,minn,mink,maxn,maxk;
	long double n[1000]={0},k[1000]={0},b;
	freopen ("D-large.in", "r", stdin);
	freopen ("d.out", "w", stdout);
	cin >> t;
	for (int h=1;h<t+1;h++) {
		cin >> nn;
		w=0;
		dw=0;
		if (nn==1) {
			cin >> n[0];
			cin >> k[0];
			if (n[0]>k[0]) cout << "Case #" << h << ": " << 1 << " " << 1 << endl;
			else cout << "Case #" << h << ": " << 0 << " " << 0 << endl;
		}
		else
		{
			for (int i=0;i<nn;i++) cin >> n[i];
			for (int i=0;i<nn;i++) cin >> k[i];
			//sort n
			for (int i=0;i<nn;i++) {
				for (int j=0;j<nn-1;j++) {
					if (n[j]>n[j+1]) {b=n[j];n[j]=n[j+1];n[j+1]=b;}
				}
			}
			//sort k
			for (int i=0;i<nn;i++) {
				for (int j=0;j<nn-1;j++) {
					if (k[j]>k[j+1]) {b=k[j];k[j]=k[j+1];k[j+1]=b;}
				}
			}
			//dw state
			minn=0;
			mink=0;
			maxn=nn-1;
			maxk=nn-1;
			for (int i=0;i<nn;i++) {
				if (n[minn]<k[mink]) {
					minn++;
					maxk--;
				}
				else
				{
					minn++;
					mink++;
					dw++;
				}
			}
			//w state
			minn=0;
			mink=0;
			maxn=nn-1;
			maxk=nn-1;
			for (int i=0;i<nn;i++) {
				if(n[maxn]>k[maxk]) {
					w++;
					maxn--;
					mink++;
				}
				else
				{
					maxn--;
					maxk--;
				}
			}
			//out
			cout << "Case #" << h << ": " << dw << " " << w << endl;
		}
		


	}
	//end of tests


	fclose(stdout);
	return 0;
}