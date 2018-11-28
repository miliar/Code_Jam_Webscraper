#include <iostream>
#include <string>
using namespace std;

const int MAXN = 1000 * 1000 + 5;

int i, longest[MAXN], last[MAXN], m, t, t_case;

bool is_vowel(char c) {
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}

int main() {
    
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    
    cin >> t;

    for(t_case = 1; t_case <= t; ++t_case) {
        string Text;        
        cin >> Text;
        cin >> m;
        
        long long ans = 0;

        int n = Text.size();
        
        for(i = 0; i < n; ++i) {
            last[i] = -1;
            longest[i] = 0;
        }

        for(i = 0; i < n; ++i)
            if(is_vowel(Text[i])) {
                longest[i] = 0;
                if(i != 0)
                    last[i] = last[i - 1];
            }

            else {
                if(i == 0)
                    longest[i] = 1;
                else
                    longest[i] = longest[i - 1] + 1;

                if(longest[i] >= m)
                    last[i] = i;
                else {
                    if(i != 0)
                        last[i] = last[i - 1];
                }
            }
        
        for(i = 0; i < n; ++i) {
            //cerr << i << " " << last[i] << " " << longest[i] << "\n";
            if(last[i] != -1)
                ans += last[i] - m + 2; 
        }

        cout << "Case #" << t_case <<": " << ans << "\n";
    }

    return 0;
}
