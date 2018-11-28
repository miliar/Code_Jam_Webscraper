#include <iostream>
#include <string>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    int t, a, b, c, ans, l, x;
    string s, so, r;
    cin >> t;
    for(a=0; a<t; ++a) {
            ans = 0;
            cin >> l >> x;
            cin >> so;
            s = so;
            for(b=1; b<x; ++b) {
                s += so;
            }
            r = "1";
            for(c=0; c<l*x; ++c) {
                if(r == "1")
                    r = s[c];
                else if(r == "-1") {
                    r = "-";
                    r += s[c];
                }
                else if(r == "-i" && s[c] == 'i')
                    r = "1";
                else if(r == "-i" && s[c] == 'j')
                    r = "-k";
                else if(r == "-i" && s[c] == 'k')
                    r = "j";
                else if(r == "j" && s[c] == 'i')
                    r = "-k";
                else if(r == "j" && s[c] == 'j')
                    r = "-1";
                else if(r == "j" && s[c] == 'k')
                    r = "i";
                else if(r == "k" && s[c] == 'i')
                    r = "j";
                else if(r == "k" && s[c] == 'j')
                    r = "-i";
                else if(r == "k" && s[c] == 'k')
                    r = "-1";
                else if(r == "-j" && s[c] == 'i')
                    r = "k";
                else if(r == "-j" && s[c] == 'j')
                    r = "1";
                else if(r == "-j" && s[c] == 'k')
                    r = "-i";
                else if(r == "-k" && s[c] == 'i')
                    r = "-j";
                else if(r == "-k" && s[c] == 'j')
                    r = "i";
                else if(r == "-k" && s[c] == 'k')
                    r = "1";
                else {
                    r = "1";
                    for(; c<l*x; ++c) {
                        if(r == "1")
                            r = s[c];
                        else if(r == "-1") {
                            r = "-";
                            r += s[c];
                        }
                        else if(r == "i" && s[c] == 'i')
                            r = "-1";
                        else if(r == "i" && s[c] == 'j')
                            r = "k";
                        else if(r == "i" && s[c] == 'k')
                            r = "-j";
                        else if(r == "-i" && s[c] == 'i')
                            r = "1";
                        else if(r == "-i" && s[c] == 'j')
                            r = "-k";
                        else if(r == "-i" && s[c] == 'k')
                            r = "j";
                        else if(r == "k" && s[c] == 'i')
                            r = "j";
                        else if(r == "k" && s[c] == 'j')
                            r = "-i";
                        else if(r == "k" && s[c] == 'k')
                            r = "-1";
                        else if(r == "-j" && s[c] == 'i')
                            r = "k";
                        else if(r == "-j" && s[c] == 'j')
                            r = "1";
                        else if(r == "-j" && s[c] == 'k')
                            r = "-i";
                        else if(r == "-k" && s[c] == 'i')
                            r = "-j";
                        else if(r == "-k" && s[c] == 'j')
                            r = "i";
                        else if(r == "-k" && s[c] == 'k')
                            r = "1";
                        else {
                            r = "1";
                            for(; c<l*x; ++c){
                                if(r == "1")
                                    r = s[c];
                                else if(r == "-1") {
                                    r = "-";
                                    r += s[c];
                                }
                                else if(r == "i" && s[c] == 'i')
                                    r = "-1";
                                else if(r == "i" && s[c] == 'j')
                                    r = "k";
                                else if(r == "i" && s[c] == 'k')
                                    r = "-j";
                                else if(r == "-i" && s[c] == 'i')
                                    r = "1";
                                else if(r == "-i" && s[c] == 'j')
                                    r = "-k";
                                else if(r == "-i" && s[c] == 'k')
                                    r = "j";
                                else if(r == "j" && s[c] == 'i')
                                    r = "-k";
                                else if(r == "j" && s[c] == 'j')
                                    r = "-1";
                                else if(r == "j" && s[c] == 'k')
                                    r = "i";
                                else if(r == "k" && s[c] == 'i')
                                    r = "j";
                                else if(r == "k" && s[c] == 'j')
                                    r = "-i";
                                else if(r == "k" && s[c] == 'k')
                                    r = "-1";
                                else if(r == "-j" && s[c] == 'i')
                                    r = "k";
                                else if(r == "-j" && s[c] == 'j')
                                    r = "1";
                                else if(r == "-j" && s[c] == 'k')
                                    r = "-i";
                                else if(r == "-k" && s[c] == 'i')
                                    r = "-j";
                                else if(r == "-k" && s[c] == 'j')
                                    r = "i";
                                else if(r == "-k" && s[c] == 'k')
                                    r = "1";
                            }
                            if(r == "k") {
                                ans = 1;
                            }
                        }
                    }
                }
            }
            if (ans == 1) {
                cout << "Case #" << a+1 << ": YES" << '\n';
            }
            else {
                cout << "Case #" << a+1 << ": NO" << '\n';
            }
    }
    return 0;
}
