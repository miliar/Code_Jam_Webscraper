#include <bits/stdc++.h>

using namespace std;

int main()
{

    ofstream out;
    ifstream in("B-large.in");
    out.open("output.txt");

    int t;
    in >> t;
    for(int tn = 1; tn <= t; tn++){
        string s;
        in >> s;
        int cnt = 0;
        for(int i = 0; i < s.size()-1; i++){
            if(s[i] != s[i+1]){
                cnt++;
            }
        }
        if(s[s.size()-1] == '-'){
            cnt++;
        }
        out << "Case #" << tn << ": " << cnt << endl;

    }

    out.close();
    in.close();

    return 0;
}
