#include <iostream>

using namespace std;

double a[1001],b[1001];
int nTest,n;
double tmp;
void sort(){
	for (int i=1; i<=n-1; i++)
		for (int j=i+1; j<=n; j++){
			if (a[i]>a[j]) {
				tmp = a[j];
				a[j] = a[i];
				a[i] = tmp;
			}
		}
	for (int i=1; i<=n-1; i++)
		for (int j=i+1; j<=n; j++){
			if (b[i]>b[j]) {
				tmp = b[j];
				b[j] = b[i];
				b[i] = tmp;
			}
		}
}
int getDecWar(){
	int score = 0;
	int naomi = n,ken =n;
	while (naomi > 0 && ken > 0) {
		while (b[ken] >= a[naomi]) {
			ken--;
			if (ken < 1) return score;
		}
		score++;
		naomi--;
		ken--;
	}
	return score;
}
int getWar(){
	int score = n;
	int naomi = 1,ken =1;
	while (naomi <= n && ken <=n) {
		while (b[ken] <= a[naomi]) {
			ken++;
			if (ken > n) return score;
		}
//		cout << "Ken : " <<naomi << " "<< ken << endl;
		score--;
		naomi++;
		ken++;
	}
	return score;
}
int main(){
	cin >> nTest;
	for (int t=1; t<=nTest; t++){
		cin >> n;
		for (int i=1;i<=n; i++) cin >> a[i];
		for (int i=1;i<=n; i++) cin >> b[i];
		sort();
//		for (int i=1;i<=n; i++) cout << a[i] << " " ;
//		cout << endl;
//		for (int i=1;i<=n; i++) cout << b[i] << " ";
//		cout << endl;
		cout << "Case #" << t << ": " << getDecWar() << " " << getWar() << endl;
	}
	
}
