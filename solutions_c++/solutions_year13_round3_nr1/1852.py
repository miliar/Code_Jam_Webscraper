#include <iostream>
#include <fstream>
#include <string>
using namespace std;

bool v(char c) {
    if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u')
        return true;
    else
        return false;
}

int main() {
    clock_t start = clock();
    
    ifstream fin("/Users/usamaelnily/Desktop/in.txt");
    ofstream fout("/Users/usamaelnily/Desktop/out.txt");
    int T, c = 1, n;
    string str;
    fin >> T;
    while(T--) {
        int ans = 0, flag = 0, vowels = 1;
        fin >> str >> n;
        
        for(int i = 0; i < str.length(); i++) {
            flag = 0;
            vowels = 1;
            
            for(int j = i; j < str.length(); j++) {
                if(flag > 0 && v(str[j]) && flag < n)
                    flag = 0;
                if(!v(str[j]) && vowels) {
                    flag++;
                }
                if(flag >= n)
                    ans++;
            }
        }
        
        fout <<"Case #" << c << ": " << ans << endl;
        c++;
    }
    clock_t end = clock();
    
    cout <<"Time: " << ((double)(end-start)/CLOCKS_PER_SEC) / 60 <<" minutes" <<endl;
    return 0;
}