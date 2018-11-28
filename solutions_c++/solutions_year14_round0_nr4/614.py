#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int main(int argc, char *argv[])
{
    ifstream in(argv[1]);
    int n;
    in >> n;

//    cout << n << endl;
    for (int nc = 1; nc <= n; nc++) {
	int size;
	in >> size;
//	cout << size << endl;
	vector<double> n, k;

	for (int i = 0; i < size; ++i) {
	    double t;
	    in >> t;
	    n.push_back(t);
	}

	sort(n.begin(), n.end());

	for (int i = 0; i < size; ++i) {
	    double t;
	    in >> t;
	    k.push_back(t);
	}

	sort(k.begin(), k.end());

/*	for (int i = 0; i < n.size(); ++i) {
	    cout << n[i] << " ";
	}
	cout << endl;

	for (int i = 0; i < k.size(); ++i) {
	    cout << k[i] << " ";
	}
	cout << endl;*/

	int i = 0;
	int j = 0;
	
	int w = 0;
	
	while ((i < n.size()) && (j < k.size())) {
	    if (n[i] < k[j]) {
		i++;
	    } else {
		w++;
		i++;
		j++;
	    }
	}

	int dw = 0;
	i = 0;
	j = 0;

	while ((i < n.size()) && (j < k.size())) {
	    if (k[j] > n[i]) {
		i++;
		j++;
	    } else {
		j++;
		dw++;
	    }
	}

	cout << "Case #" << nc << ": " << w << " " << dw << endl;
    }

    return 0;
}
