#include <iostream>
#include <vector>

using namespace std;

bool check ( vector < vector <int > > v )
{
	vector <int> max_x;
	vector <int> max_y;

	for ( int i = 0; i < v.size(); i++ ) {
		int max = v[i][0];
		for ( int j = 0; j < v[0].size(); j++ ) {
			if ( v[i][j] > max )
				max = v[i][j];
		}
		
		max_x.push_back(max);
	}

        for ( int i = 0; i < v[0].size(); i++ ) {
	        int max = v[0][i];
                for ( int j = 0; j < v.size(); j++ ) {
                        if ( v[j][i] > max ) 
                                max = v[j][i];
                }
                max_y.push_back(max);
        }
	
	int f = 1;

        for ( int i = 0; i < v.size(); i++ ) {
                for ( int j = 0; j < v[0].size(); j++ ) {
                        if ( v[i][j] < max_x[i] && v[i][j] < max_y[j] ) {
                              	f = 0;
				break;
			}
                }
        }

	return f;
}

int main()
{
	int t;
	cin >> t;
	vector <int> v;
	vector <vector <int> > vov;

	for ( int i = 0; i < t; i++ ) {
		int m,n,x;
		cin >> m >> n;
		for ( int j = 0; j < m; j++ ) {
			for ( int k = 0; k < n; k++ ) {
				cin >> x;
				v.push_back(x);
			}
			vov.push_back(v);
			v.clear();
		}
		cout << "Case #" << i + 1 << ": ";
		if ( check(vov) )
			cout << "YES\n";
		else
			cout << "NO\n";
		vov.clear();
	}

	return 0;
}
