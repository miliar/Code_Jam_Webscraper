#include <iostream>
#include <algorithm>
using namespace std;
const int maxn = 10000;
double a[maxn], b[maxn];
int n;
int win(int deta){
	for (int i = 0; i<n-deta; i++){
		if (a[i] < b[i+deta]) return -1;
	}
	return n-deta;
}
int main(){
	int T, cas = 0;
	for (cin>>T; T--;){
		cas++;
		cout<<"Case #"<<cas<<": ";
		cin>>n;
		for (int i = 0; i<n; i++){
			cin>>a[i];
		}
		for (int j = 0; j<n; j++){
			cin>>b[j];
		}
		sort(a, a+n);
		sort(b, b+n);
		for (int i = 0; i+i<n; i++){
			swap(a[i], a[n-i-1]);
			swap(b[i], b[n-i-1]);
		}
		int pnt = 0;
		for (int i = 0; i<n; i++){
			pnt = max(pnt, win(i));
		}
		int q = 0;
		for (int i = 0; i<n; i++){
			bool fd = false;
			for (int j = 0; j<n; j++) if (b[j] > a[i]){
				b[j] = -1;
				fd = true;
				break;
			}
			if (!fd){
				for (int j = n-1; j>=0; j--) if (b[j] >=0){
					b[j] = -1;
					break;
				}
				q++;
			}
		}
		cout<<pnt<<' '<<q<<endl;
	}
	return 0;
}

