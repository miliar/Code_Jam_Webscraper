#include<iostream>
#include<string>

using namespace std;

void solve(int _case){
	int smax;
	string str;

	cin >> smax;
	cin >> str;
	
	int stand = 0;
	int invite = 0;
	for (int i=0; i<smax; i++) {
		int snext = str[i+1] - '0';
		stand += str[i] - '0';
		if (snext > 0 && stand < i+1) {
			int inv = i + 1 - stand;
			invite += inv;
			stand += inv;
		}
	}
	cout << "Case #" << _case << ": " << invite << endl;
}

int main(){
    freopen("large.in","r",stdin);
    freopen("large.out","w",stdout);
    int t;
    cin >> t;
    for(int i = 1 ; i <= t ; ++ i )
        solve(i);
}
