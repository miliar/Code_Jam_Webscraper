#include <bits/stdc++.h>
using namespace std;

int a[5],b[5];

int main(){
	//freopen("test.inp","r" ,stdin);
	//freopen("A-small-attempt0.out","w",stdout);

	int TC;
	cin >> TC;
	for (int t=1;t<=TC;t++){
		int f,l;
		cin >> f;

		int aa;

		for (int i=1;i<=4;i++)
			for (int j=0;j<4;j++){
				cin >> aa;
				if (i==f)
					a[j] = aa;
			}

		cin >> l;

		for (int i=1;i<=4;i++)
			for (int j=0;j<4;j++){
				cin >> aa;
				if (i==l)
					b[j] = aa;
			}

		int ct = 0;
		int ans = 0;

		for (int i=0;i<4;i++)
			for (int j=0;j<4;j++)
				if (a[i]==b[j])
					ct ++ , ans = a[i];

		printf("Case #%d: ",t );
		if (ct==0)
			cout << "Volunteer cheated!" << endl;
		else if (ct==1)
			cout << ans << endl;
		else
			cout << "Bad magician!" << endl;

	}

}