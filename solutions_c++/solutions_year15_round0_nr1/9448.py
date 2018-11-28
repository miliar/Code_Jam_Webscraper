#include<iostream>
#include<fstream>

using namespace std;

int main() {
    ifstream fin("/Users/usamaelnily/Desktop/a.in");
    ofstream fout("/Users/usamaelnily/Desktop/a.out");
    
    int t, cases;
    fin >> t;
    cases = t;
    while(t--) {
        int smax, standing = 0, ans = 0;
        string s;
        fin >> smax >> s;
        for(int i = 0; i < s.length(); i++) {
            if(standing >= i)
                standing += (s[i] - '0');
            else if((s[i] - '0') > 0){
                ans += (i - standing);
                standing += (i - standing);
                standing += (s[i] - '0');
            }
        }
        fout << "Case #" << cases - t << ": " << ans << endl;
    }
    
    return 0;
}