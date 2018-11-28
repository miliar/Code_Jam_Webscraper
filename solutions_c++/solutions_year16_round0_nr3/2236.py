#include <iostream>
#include <vector>
using namespace std;


vector<int> solve(string s, int debug = 0){
    vector<int> V;
    for(int i = 2; i <= 10; ++i){
        for(int j = 2; j <= 100; ++j){
            int m = 0; 
            long long d = 0;
            for(int l = 0; l < s.size(); ++l){
                m = (m * i + s[l] - '0') % j;
                // if(debug)d = d*i + s[l] - '0';
            }
            if(m == 0){
                // if(debug)cout << d << endl;
                V.push_back(j);
                break;
            }
        }
        if(V.size() != i-1){
            return vector<int>();
        }
    }
    return V;
}

int main() {
	int TC;
	cin >> TC;
	for(int tc = 1 ; tc<=TC; ++tc){
	    int N , J;
	    cin >> N >> J;
	    cout << "Case #" << tc << ":" << endl;
	    for(int i = 0; i < (1<<(N-2)) ; ++i){
	        string s = "1";
	        for(int l = N-3; l >= 0; --l){
	            s += ((i >> l) & 1) + '0';
	        }
	        s += "1";
	        vector<int> V = solve(s);
	        if(V.size()){
	            cout << s << " ";
	            for(int j = 0; j < V.size(); ++j){
	                cout << V[j] << " ";
	            }
	            cout << endl;
	           // solve(s,1);
	            J--;
	        }
	        if(J == 0)break;
	    }
	}
}
