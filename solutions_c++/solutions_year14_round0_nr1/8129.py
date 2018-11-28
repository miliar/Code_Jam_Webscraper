#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <memory.h>
#include <time.h>
#include <algorithm>
#include <memory.h>
#include <string>
#include <sstream>
#include <vector>
#define N 111111
#define LL long long



using namespace std;


int a[100],x,y,T;


int main(){        
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin >> T;
	int v = 0;

	while (T--){
		v++;
		memset(a,0,sizeof(a));
		cin >> x;
		for (int i=1;i<5;i++) for (int j=1;j<5;j++){
			cin >> y;
			if (i==x) a[y]++;
		}
		cin >> x;
		for (int i=1;i<5;i++) for (int j=1;j<5;j++){
			cin >> y;
			if (i==x) a[y]++;
		}

		int kol = 0,ans = 0;
		for (int i=1;i<=16;i++) if (a[i]==2){
			kol++;
			ans = i;
		}

		if (kol >1) cout << "Case #"<< v <<": Bad magician!"<<endl;else
		if (kol==1) cout << "Case #"<< v <<": "<<ans<<endl;else
		if (kol==0) cout << "Case #"<< v <<": Volunteer cheated!"<<endl;
	}

	return 0;
}