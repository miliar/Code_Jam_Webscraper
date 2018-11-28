#include <iostream>
#include <cstdio>
#include <string>
using namespace std;

string intercambia(string s, int i, int j){
    for(; i < j; i++, j--){
        char c = s[i];
        s[i] = s[j] == '-' ? '+' : '-';
        s[j] = c == '-' ? '+' : '-';
    }
    if(i == j)
        s[i] = s[i] == '-' ? '+' : '-';
    return s;
}

int solve(string s){
    int cont = 0;
//    cout << s << endl;
	for(int i = s.size()-1; i > 0; i--){
        if(s[i] == '-'){
            s[i] = '+';
            if(s[0] == '+'){
                for(int j = 1; j < i && s[j] == '+'; j++){
                    s[j] = '-';
                }
                cont += 2;
            }
            else{
                s[0] = '+';
                cont++;
            }
            s = intercambia(s, 1, i-1);
//            cout << s << endl;
        }
	}
	return cont+(s[0] == '-');
}

int main(){
	int n, casos;
	string s;
	cin >> casos;
	for(int i = 1; i <= casos; i++){
		cin >> s;
        printf("Case #%d: %d\n", i, solve(s));
	}
	return 0;
}
