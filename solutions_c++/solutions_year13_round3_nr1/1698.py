#include<iostream>
#include<string>

using namespace std;

int main () {
    int T; cin >> T;
    for (int step=1; step<=T; step++) {    
        string line; cin >> line;
        int n; cin >> n;
        int answer = 0;
        for (int i=0; i<line.length(); i++)
            for (int j=i; j<line.length(); j++) {
                int consonant = 0;
                for (int k=i; k<=j; k++) {
                    if (line[k] != 'a' && line[k] != 'e' && 
                       line[k] != 'i' && line[k] != 'o' && line[k] != 'u')
                    consonant++;   
                    else consonant = 0;
                    if (consonant >= n) {
                       answer++;
                       break;
                    }
                }
            }
        cout << "Case #" << step << ": " << answer << endl;    
    }    
    return 0;
}
