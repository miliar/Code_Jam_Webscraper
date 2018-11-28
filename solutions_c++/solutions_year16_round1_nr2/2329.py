#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {

	int t;

	cin >> t;

	for(int ti = 1; ti <= t; ti++){

	    int n;

	    cin >> n;

	    vector<vector<int> > lists (2*n, vector<int> (n));
	    vector<int> found (2501);

	    vector<vector<int> > rows;
	    vector< vector<int> > cols;

	    for(int i = 0; i < 2*n - 1; i++){
            for(int j = 0; j < n; j++){

            cin >> lists[i][j];
            found[lists[i][j]]++;
            }
	    }

        cout << "Case #" << ti <<": ";

	    for(int i = 0; i < found.size(); i++){
            if(found[i] & 2){
                cout << i << " ";
            }
	    }
	    cout << '\n';


	}

	return 0;
}
