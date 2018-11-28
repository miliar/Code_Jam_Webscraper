#include <iostream>

using namespace std;

char neg(char a) {
    switch (a) {
    case '1': return '-';
    case 'i': return 'I';
    case 'j': return 'J';
    case 'k': return 'K';
    case '-': return '1';
    case 'I': return 'i';
    case 'J': return 'j';
    case 'K': return 'k';
    }
    return 0;
}

bool isneg(char a) {
    switch (a) {
    case '-':
    case 'I':
    case 'J':
    case 'K':
        return true;
    }
    return false;
}

char matrixmul(char a, char b) {
    char c = b;
    
    bool nega = isneg(a);
    bool negb = isneg(b);
    if (nega) a = neg(a);
    if (negb) b = neg(b);
    
    switch (a) {
    case 'i':
        switch (b) {
            case '1': c = 'i'; break;
            case 'i': c = '-'; break;
            case 'j': c = 'k'; break;
            case 'k': c = 'J'; break;
        } break;
    case 'j':
        switch (b) {
            case '1': c = 'j'; break;
            case 'i': c = 'K'; break;
            case 'j': c = '-'; break;
            case 'k': c = 'i'; break;
        } break;
    case 'k':
        switch (b) {
            case '1': c = 'k'; break;
            case 'i': c = 'j'; break;
            case 'j': c = 'I'; break;
            case 'k': c = '-'; break;
        } break;
   }
   
   return (nega != negb) ? neg(c) : c;
}

string reduce(string s) {
    for (;;) {
        int l = s.size();
        if (l < 2) break;
        char a = s[l - 2], b = s[l - 1];
        char c = matrixmul(a, b);
        s[l - 2] = c;
        s.resize(l - 1);
    }
    return s;
}

void solve(int count) {
    int d, x; // d = num chars, x = num reps
    cin >> d >> x;
    string s;
    cin >> s;
    
    string str;
    for (int i = 0; i < x; ++i) str += s;
    
    bool possible = false;
    
    const int l = str.size();
    if (l >= 3) {
        int i, k;
        // first try to get a i at the beginning
        for (i = 1; i <= l - 2 && !possible; ++i) {
            string a = reduce(str.substr(0, i));
            if (a == "i") {
                //cout << "Found i from " << str.substr(0, i) << endl;
                
                // now search a k from the end
                for (k = l - 1; k >= 2; --k) {
                    string c = reduce(str.substr(k, l - k));
                    if (c == "k") {
                  //      cout << "Found k from " << str.substr(k, l - k) << endl;
                        
                        // now check middle for j
                        string b = reduce(str.substr(i, k - i));
                        if (b == "j") {
                    //        cout << "Found j from " << str.substr(i, k - i) << endl;
                            possible = true;
                            break;
                        }
                    }
                }
                if (k < 2) break; // no k found.. abort
            }
        }
    }
    
    cout << "Case #" << count << ": ";
    cout << (possible ? "YES" : "NO");
    cout << endl;
}

int main(int argc, const char * argv[]) {
	int numCases = 0;
    cin >> numCases;
    
  //  cout << reduce("jij") << endl;
  //  cout << reduce("iji") << endl;
  //  cout << reduce("jijiji") << endl;
    
    for (int count = 1; count <= numCases; ++count) {
        solve(count);
    }
    return 0;
}

