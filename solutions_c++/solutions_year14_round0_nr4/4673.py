#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool gt(const double &a, const double &b) {
	if( (a - b) > 10e-9) {
		return true;
	}
	return false;
}

int main() {
    int T;
    cin >> T;

    for(int i = 1; i < T+1; ++i) {
	    int num;
	    int war = 0;
	    int dwar = 0;
	    vector<double> a,b;

	    cin >> num;
	    for( int j = 0; j < num; ++j ) {
		    double in;
		    cin >> in;
		    a.push_back(in);
	    }
	    for( int j = 0; j < num; ++j ) {
		    double in;
		    cin >> in;
		    b.push_back(in);
	    }
	    sort(a.begin(), a.end());
	    sort(b.begin(), b.end());

	    size_t large = a.size() - 1;
	    size_t small = 0;
	    for( size_t j = a.size(); j > 0; --j ) {
		    //cout << a[j-1] << ' ' << b[small] << ' ' << b[large] << '\n';
		    if( gt(a[j-1], b[large]) ) {
			    if( gt(a[j-1], b[small]) ) {
				    war++;
			    }
			    small++;
		    } else {
			    large--;
		    }
	    }
	    //cout << '\n';
	    large = a.size() - 1;
	    small = 0;
	    for( size_t j = 0; j < a.size(); ++j ) {
		    //cout << a[j] << ' ' << b[small] << ' ' << b[large] << '\n';
		    if( a[j] > b[large] ) {
			    if( a[j] > b[small] ) {
				    dwar++;
			    }
			    small++;
		    } else {
			    if( a[j] > b[small] ) {
				    dwar++;
				    small++;
			    } else {
				    large--;
			    }
		    }
	    }

	    cout << "Case #" << i << ": " << dwar << ' ' << war << '\n';
    }

    return 0;
}
