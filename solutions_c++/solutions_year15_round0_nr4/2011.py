// D. Ominous Omino
#include <iostream>
#include <cmath>
#include <vector>

#define pb push_back
#define po pop_back

using namespace std;

int x, y, o;

const string gabriel = "GABRIEL";
const string richard = "RICHARD";

void solve() {
	cin>>o>>x>>y;

	if ((x * y) % o != 0) {
		cout<<richard;
		return;
	}

	// Pentru o linie
	if (x == 1 && y == 1) {
		if (o == 1)
			cout<<gabriel;
		else
			cout<<richard;
	} else if (x == 1 && y == 2) {
		if (o <= 2)
			cout<<gabriel;
		else
			cout<<richard;
	} else if (x == 1 && y == 3) {
		if (o == 1)
			cout<<gabriel;
		else
			cout<<richard;
	} else if (x == 1 && y == 4) {
		if (o <= 2)
			cout<<gabriel;
		else
			cout<<richard;
	}
	// Pentru 2 linii
	else if (x == 2 && y == 1) {
		if (o <= 2)
			cout<<gabriel;
		else
			cout<<richard;
	} else if (x == 2 && y == 2) {
		if (o <= 2)
			cout<<gabriel;
		else
			cout<<richard;
	} else if (x == 2 && y == 3) {
		if (o <= 3)
			cout<<gabriel;
		else
			cout<<richard;
	} else if (x == 2 && y == 4) {
		if (o <= 2)
			cout<<gabriel;
		else
			cout<<richard;
	} 

	// Pentru 3 linii
	else if (x == 3 && y == 1) {
		if (o == 1)
			cout<<gabriel;
		else
			cout<<richard;
	} else if (x == 3 && y == 2) {
		if (o <= 3)
			cout<<gabriel;
		else
			cout<<richard;
	} else if (x == 3 && y == 3) {
		if (o == 1 || o == 3)
			cout<<gabriel;
		else
			cout<<richard;
	} else if (x == 3 && y == 4) {
		cout<<gabriel;
	} 

	// Pentru 4 linii
	else if (x == 4 && y == 1) {
		if (o <= 2)
			cout<<gabriel;
		else
			cout<<richard;
	} else if (x == 4 && y == 2) {
		if (o <= 2)
			cout<<gabriel;
		else
			cout<<richard;
	} else if (x == 4 && y == 3) {
		cout<<gabriel;
	} else if (x == 4 && y == 4) {
		if (o != 3)
			cout<<gabriel;
		else
			cout<<richard;
	}
}

int main() {

	int t;
	cin>>t;
	for (int i=1;i<=t;i++) {
		cout<<"Case #"<<i<<": ";
		solve();
		cout<<'\n';
	}

	return 0;
}