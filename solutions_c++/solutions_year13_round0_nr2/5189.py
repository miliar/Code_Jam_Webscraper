#include <iostream>
using namespace std;
int main()
{
	int t,n,m,ans,check;
	int a[100][100];
	cin >> t;
	for (int i=1; i<=t; ++i) {
		cin >> n >> m;
		for (int j=0; j!=n; ++j) {
			for (int k=0; k!=m; ++k) {
				cin >> a[j][k];
			}
		}
		ans=1;
		for (int j=0; j!=n; ++j) {
			for (int k=0; k!=m; ++k) {
				check=1;
				for (int l=0; l!=n; ++l) {
					if (a[l][k]>a[j][k]) {
						check=0;
						break;
					}
				}
				if (check==0) {
					check=1;
					for (int l=0; l!=m; ++l) {
						if (a[j][l]>a[j][k]) {
							check=0;
							break;
						}
					}
					if (check==0) {
						ans=0;
						break;
					}
				}
			}
		}
		if (ans==1) {
			cout << "Case #" << i << ": YES" << endl;
		} else {
			cout << "Case #" << i << ": NO" << endl;
		}
	}
	return 0;
}
