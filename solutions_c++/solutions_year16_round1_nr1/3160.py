#include<bits/stdc++.h>

using namespace std;

int main() {
	ifstream in("A-large.in");
    int s;
    in >> s;
    for(int t =0; t < s; t++){
        string input;
        in >> input;
        string s = "";
        s += input[0];
        for(int i = 1; i < input.length();i++){
            if(input[i] >= s[0])
                s = input[i] + s;
            else 
                s = s + input[i];
        }
        cout << "Case #" <<  t+1 << ": " << s << endl;
    }

	return 0;
}
