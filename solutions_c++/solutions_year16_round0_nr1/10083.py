#include <bits/stdc++.h>

using namespace std;



int main (){

	  freopen("in.txt", "rt", stdin);
	  freopen("out.txt", "wt", stdout);

	int t;
	cin >> t;
	for (int k = 0; k < t; k++){
		int n;
		cin >> n;
		long long ans = 0, bla = 0;
		set <int> st;
		int i = 1;

		if (n != 0)
			while (st.size() != 10){
				bla = n*i;
				ans = bla;
				while (bla){
					st.insert(bla%10);
					bla/=10;
				}

				++i;
			}

		if (n == 0)
			cout << "Case #" << k + 1<<": INSOMNIA" << endl;
		else cout << "Case #" << k + 1 <<": " << ans << endl;


	}

}
