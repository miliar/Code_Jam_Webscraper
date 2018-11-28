#include<fstream>
#include<iomanip>
#include<list>
#include<algorithm>
using namespace std;

int deceitfulWar(list<double> lstNaomi, list<double> lstKen) {
	int ret = 0;
	while (lstNaomi.size() > 0) {
		if (lstNaomi.front() < lstKen.front()) {
			lstNaomi.pop_front();
			lstKen.pop_back();
		}
		else {
			lstNaomi.pop_front();
			lstKen.pop_front();
			ret++;
		}
	}
	return ret;
}

int war(list<double>* pLstNaomi, list<double>* pLstKen) {
	int ret = 0;
	while (pLstKen->size() > 0) {
		if (pLstNaomi->front() > pLstKen->front()) {
			pLstKen->pop_front();
			pLstNaomi->pop_back();
			ret++;
		}
		else {
			pLstKen->pop_front();
			pLstNaomi->pop_front();
		}
	}
	return ret;
}

int main() {
	list<double> lstNaomi;
	list<double> lstKen;
	ifstream cin("D-large.in", fstream::in);
	ofstream cout("D-large.out", fstream::out);

	int n, t;
	double tmp;

	if (!cin) return 1;
	cin >> t;
	for (int i = 0; i < t; i++) {
		lstNaomi.clear();
		lstKen.clear();
		cin >> n;
		for (int j = 0; j < n; j++) {
			cin >> tmp;
			lstNaomi.push_back(tmp);
		}
		for (int j = 0; j < n; j++){
			cin >> tmp;
			lstKen.push_back(tmp);
		}

		lstNaomi.sort();
		lstKen.sort();

		int iRetDeceitfulWar = deceitfulWar(lstNaomi, lstKen);
		int iRetWar = war(&lstNaomi, &lstKen);
		
		cout << "Case #" << i + 1 << ": " << iRetDeceitfulWar << " " << iRetWar << endl;
	}

	return 0;
}