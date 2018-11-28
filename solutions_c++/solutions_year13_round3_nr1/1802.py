#include<cstdio>
#include<vector>
#include<map>
#include<set>
#include<iostream>
#include<iomanip>
#include<time.h>
#include<sstream>
#include<fstream>
#include<string>
#include<string.h>
#include<algorithm>

#define nl printf("\n")

using namespace std;

bool is_vowel(char ch)
{
    return (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u');
}

int main()
{
    ios_base::sync_with_stdio(false);

    int T;
    cin >> T;

    for (int t; t < T; t++) {
        string word;
        int n;
        cin >> word >> n;

        vector<int> q(word.size(),0);

        if (!is_vowel(word[0])) {
            q[0] = 1;
        }
        for (int i = 1; i < q.size(); i++) {
            if (!is_vowel(word[i])) {
                q[i] = q[i-1] + 1;
            } else {
                q[i] = 0;
            }

        }

        //for (int i = 0; i < q.size(); i++) {
            //cout << q[i] << " ";
        //}


        int sum = 0;
        int minule = 0;

        //cout << endl << "minule: ";
        for (int i = 0; i < q.size(); i++) {
            if (q[i] >= n) {
                minule = i+1-n+1;
            } else {
                //minule = minule;
            }
            //cout << minule << " ";
            sum += minule;
        }
        //cout << endl;

        cout << "Case #" << t+1 << ": " << sum << endl;
    }
}
