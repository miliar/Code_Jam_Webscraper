#include<fstream>
#include<iomanip>
#include<iostream>
#include<algorithm>

using namespace std;

double a[1010],b[1010];

ifstream fin("D-large.in");
ofstream fout("D-large.out");

int main(){

	cin.rdbuf(fin.rdbuf());
	cout.rdbuf(fout.rdbuf());

	int ntc,n;
	cin >> ntc;

	for (int tc=1;tc<=ntc;tc++){
		cout << "Case #" << tc << ": ";
		cin >> n;
		for (int i=0;i<n;i++) cin >> a[i];
		for (int i=0;i<n;i++) cin >> b[i];
		sort(a,a+n);
		sort(b,b+n);
		int r1 = 0,r2 = 0,k = 0;
		for (int i=0;i<n;i++){
			if (a[i]>b[k]){
				k++;
				r1++;
			}
		}

		k = -1;
		for (int i=0;i<n;i++){
			k++;
			while(k<n && a[i]>b[k]) k++;
			if (k==n){
				r2 = n-i;
				break;
			}
		}

		cout << r1 << " " << r2 << endl;


	}

	return 0;
}