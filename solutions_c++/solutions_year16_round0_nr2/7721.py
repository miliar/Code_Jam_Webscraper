#include<bits/stdc++.h>

using namespace std;

int main(){
    ifstream fin("input.txt");
    ofstream fout("output.txt");
    long long n;
    fin >> n;
    for(int i = 0; i < n; ++i){
        string s;
        fin >> s;
        int k = s.size();
        for(int j = s.size() - 1; j >= 0; --j){
            if(s[j] == '+'){
                k = j;
            }
            else{
                break;
            }
        }
        int ans = 0;
        //cout << i << ' ' << k << ' ' << s << endl;
        while(k != 0){
            //cout << k << ' ' << s << ' ';
            if(s[0] == '+'){
                ++ans;
                int z = 0;
                while(s[z] == '+'){
                    s[z] = '-';
                    ++z;
                }
            }
            ++ans;
            for(int j = 0; j * 2 < k; ++j){
                swap(s[j], s[k - j - 1]);
            }
            for(int j = 0; j < k; ++j){
                if(s[j] == '+'){
                    s[j] = '-';
                }
                else{
                    s[j] = '+';
                }
            }
            for(int j = k - 1; s[j] == '+'; --j){
                k = j;
            }
        }
        fout << "Case #" << i + 1<< ": " << ans << endl;
    }
}
