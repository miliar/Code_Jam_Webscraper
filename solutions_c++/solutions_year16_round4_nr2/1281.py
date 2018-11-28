#include <iostream>
#include <vector>
#include <algorithm>
#include <bitset>
#include <fstream>

using namespace std;

typedef long long ll;



int main() { 
	ofstream fout;
	fout.open ("ayylmao.txt");
	ifstream fin;
	fin.open ("B-small-attempt1.in");

	int t; fin>>t;
	for(int i = 1; i <= t; i++) {
		int n, k; fin >> n >> k;
		double p[n];
		for(int j = 0; j < n; j++) {
			fin >> p[j];
		}
		double maxi = 0;
		vector<bool> v(n);
    	fill(v.begin() + n - k, v.end(), true);

    	do {
    		vector<double> chosen;
    		for(int j = 0; j < n; j++) {
    			if(v[j]) {
    				chosen.push_back(p[j]);
    				//cout<<p[j]<<' ';
    			}
        	}
        	//cout<<endl;
        	double ans = 0;
        	vector<bool> vv(k);
        	fill(vv.begin() + k/2, vv.end(), true);
        	do{
        		double tmp = 1;
        		for(int j = 0; j < k; j++) {
        			//cout<<chosen[j]<<' '<<vv[j]<<endl;
        			if(vv[j]) {
        				tmp *= chosen[j];
        			}
        			else {
        				tmp *= 1 - chosen[j];
        			}
        		}
        		//cout<<tmp<<endl;
        		ans += tmp;
        	}while(next_permutation(vv.begin(), vv.end()));
        	if(maxi < ans) {
        		maxi = ans;
        	}
    	} while (next_permutation(v.begin(), v.end()));

		fout << "Case #" << i << ": " << maxi << endl;
	}
	return 0;
}