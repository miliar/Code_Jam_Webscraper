#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int a[6][6];
	int b[6][6];
	vector <int> v;
	int x, y;
	int n;
	int k;
	cin >> n;
	int count;

    	for (int l = 0; l < n; l++) {
        	cin >> x;
	        for (int i = 0; i < 4; i++) {
            		for (int j = 0; j < 4; j++) {
		                cin >> a[i][j];
			}
            	}
	        cin >> y;
        	for (int i = 0; i < 4; i++) {
            		for (int j = 0; j < 4; j++) {
				cin >> b[i][j];
	            	}
		}
		v.clear();
		for (int i = 0; i < 4; i++) {
			v.push_back(b[y-1][i]);
		}
		count = 0;
		for (int i = 0; i < 4; i++) {
	            if (find(v.begin(), v.end(),a[x-1][i])!=v.end()) {
			count = count+1;
	               	k = a[x-1][i];

//			cout << k << " " << v[i] endl;
            	    }
			 //out << a[x-1][y] << " " << v[i] endl;
		}
	//	cout << "count : " << count << endl;
	        if (count == 1) {
                  	cout << "Case #" << l+1<< ": " << k << endl;
        	} else if (count > 1) {
	               	cout << "Case #" << l+1<< ": Bad magician!\n";
	        } else if (count == 0) {
        	       cout << "Case #" << l+1 <<  ": Volunteer cheated!\n";
		}     

	}
        return 0;
}
