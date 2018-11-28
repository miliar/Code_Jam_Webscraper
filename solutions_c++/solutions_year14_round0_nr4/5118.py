#include <iostream>
#include <algorithm>

using namespace std;

	int p,k,l,wl;
	float ko[1200],mn[1200];

int main() {

	cin>>p;
	for (int j=1; j<=p; j++) {
		l =0; 
		wl= 0;
		cin>>k;
		for (int i=0; i<k; i++)
		cin>>ko[i];
		for (int i=0; i<k; i++)
		cin>>mn[i];
		sort(ko, ko + k);
		sort(mn, mn + k);
		for (int i=0,h=0; i<k; i++) {
			if (ko[i] > mn[h]) {
				h++;
				wl++;
			}
		}
		for (int i=0,j=0; i<k; i++) {
			if (ko[j] < mn[i])
			j++;
			else
			l++;
		}
		cout<<"Case #"<<j<<": "<<wl<<" "<<l<<"\n";
	}

	return 0;
}