#include <iostream>
#include <limits>

using namespace std;

struct Quaternion {
    bool positive;
    char value;
};

bool equal(Quaternion a, char b) {
    return a.positive && a.value == b;
}

void multiply(Quaternion& a, char b) {
    //cout << (a.positive ? "" : "-") << a.value << " * " << b;
    switch(a.value) {
        case '1':
            a.value = b;
            break;
        case 'i':
            switch(b) {
                case '1':
                    a.value = 'i';
                    break;
                case 'i':
                    a.value = '1';
                    a.positive = !a.positive;
                    break;
                case 'j':
                    a.value = 'k';
                    break;
                case 'k':
                    a.value = 'j';
                    a.positive = !a.positive;
                    break;
            }
            break;
        case 'j':
            switch(b) {
                case '1':
                    a.value = 'j';
                    break;
                case 'i':
                    a.value = 'k';
                    a.positive = !a.positive;
                    break;
                case 'j':
                    a.value = '1';
                    a.positive = !a.positive;
                    break;
                case 'k':
                    a.value = 'i';
                    break;
            }
            break;
        case 'k':
            switch(b) {
                case '1':
                    a.value = 'k';
                    break;
                case 'i':
                    a.value = 'j';
                    break;
                case 'j':
                    a.value = 'i';
                    a.positive = !a.positive;
                    break;
                case 'k':
                    a.value = '1';
                    a.positive = !a.positive;
                    break;
            }
            break;
    }
    //cout << " = " << (a.positive ? "" : "-") << a.value << endl;
    return;
}


bool reducesToIJK(int x, string w) {
    string goal = "ijk";
    int g = 0;
    char subgoal = goal[g];
    Quaternion buf;
    buf.positive = true;
    buf.value = '1';
    for(int i = 0; i < x; i++) {
        for(string::iterator it = w.begin(); it != w.end(); ++it) {
            multiply(buf, *it);
            if(g < goal.length() && equal(buf, goal[g])) {
                //cout << "found " << goal[g] << endl;
                g++;
                buf.positive = true;
                buf.value = '1';
            }
        }
    }
    return g == goal.length() && equal(buf, '1');
}

int main() {
    int t;
    cin >> t;
    
    for(int i = 1; i <= t; i++) {
        int l,x;
        cin >> l >> x;

        cin.ignore (numeric_limits<streamsize>::max(), '\n'); 
        
        string word;
        getline (cin, word);

        cout << "Case #" << i << ": ";
        cout << (reducesToIJK(x, word) ? "YES" : "NO");
        cout << endl;
    }

    return 0;
}

