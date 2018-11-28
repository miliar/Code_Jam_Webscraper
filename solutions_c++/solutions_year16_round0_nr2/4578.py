#include <iostream>
#include <string>

using namespace std;

int main(){
int		T, i, j, ans;
string	in;
		cin >> T;
		for(i = 0 ; i < T ; i++){
			cin >> in;
			ans = 0;
		int	l = in.length();
			for(j = 0 ; j < l - 1 ; j++){
				if(in[j] != in[j + 1])ans++;
			}
			if(in[l - 1] == '-')ans++;
			cout << "Case #" << i + 1 << ": " << ans;
			if(i != T - 1)cout << endl;
		}
		return 0;
}
