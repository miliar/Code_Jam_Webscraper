#include <bits/stdc++.h>
using namespace std;

#define MAX 1200

int ans[MAX];

bool validate(int g[], string& aux){
	vector<int> z(3, 0);
	for (int i = 0; i < aux.length(); i++){
		if (aux[i] == 'P') z[0]++;
		else if (aux[i] == 'R') z[1]++;
		else z[2]++;
	}
	for (int i = 0; i < 3; i++){
		if (g[i] != z[i])
			return false;
	}
	return true;
}

string solve(int a, int b, int type){
	if (a == b){
		if (type == 0) return "P";
		else if (type == 1) return "R";
		else return "S";
	}
	int w = (type+1)%3;
	//cout << "type: " << type << " w: " << w << " a: " << a << " b: " << b << endl;
	string actual = "";
		string tryside1 = solve(a, (a+b)/2, type);
		string tryside2 = solve((a+b)/2+1, b, w);
		
		if (tryside1.length() > 0 && tryside2.length() > 0){
			actual = tryside1+tryside2;
		}

		string try2side1 = solve(a, (a+b)/2, w);
		string try2side2 = solve((a+b)/2+1, b, type);

		if (try2side1.length() > 0 && try2side2.length() > 0){
			string tmp = try2side1+try2side2;
			if (tmp < actual || actual.length() == 0) actual = tmp;
		}
	return actual;
}

int main(){
    int t, cases = 1;
    cin >> t;
    while (t--){
        int n, g[3];
        cin >> n >> g[1] >> g[0] >> g[2];

        string ans = "";
        for (int i = 0; i < 3; i++){
        	//cout << "g: " << g[0] << " " << g[1] << " " << g[2] << endl;
        	g[i]--;
        	string aux = "";
        	if (g[i] >= 0)
        		aux = solve(0, (1<<n)-1, i);
        	g[i]++;
        	if (ans.length() == 0 || (aux < ans && aux.length() > 0)){
        		if (validate(g, aux))
        			ans = aux;
        	}
        }

        cout << "Case #" << cases++ << ": ";

        if (ans.length() > 0){
        	cout << ans << endl;
        }
        else cout << "IMPOSSIBLE" << endl;
    }
    return 0;
}
