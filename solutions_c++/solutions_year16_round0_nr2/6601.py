#include<bits/stdc++.h>

using namespace std;

int countPlus(string & s){
    int ret = 0;
    for(int i = 0; i < s.length(); i++) {
        if(s[i] == '+')
            ret++;
    }
    return ret;
}

void flip(string & s) {
    for(int i = 0; i < s.length();i++) {
        if(s[i] == '+')
            s[i] = '-';
        else 
            s[i] = '+';

    }
}

int main() {
	ifstream in("B-large.in");
    int t;
    in >> t;
    for(int m = 0; m < t; m++) {
        int count = 0;
        string s;
        in >> s;
        int numplus = countPlus(s);
        /*
        if(numplus * 2 < s.length()){
            flip(s);
            count++;
        }*/
        bool neg = false;
        for(int i = 0; i < s.length(); i++) {
            if(!neg && s[i] == '-') {
                neg = true;
                count += 2;
            }
            if(s[i] == '+')
                neg = false;
        }
        if(s[0] == '-'){
            count -= 1;
        }
        cout << "Case #" << (m+1) << ": " << count << endl;

    }

	return 0;
}
