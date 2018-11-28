#include "iostream"
#include "string"
using namespace std;

int pancake(string pattern) {
    if (pattern.size() == 0) return 0;
    if (pattern.size() == 1) {
        if (pattern[0] == '+') return 0;
        else return 1;
    }

    char cur = pattern[0];
    char searchChar = (pattern[0] == '+')?'-':'+';
    int num = 1; 
    auto pos = pattern.find_first_of(searchChar, 0);
    while (pattern.find_first_of(searchChar, pos) != std::string::npos) {
        pos = pattern.find_first_of(searchChar, pos);
        num++;
        char temp = cur;
        cur = searchChar;
        searchChar = temp;
    }
    if (searchChar == '-')
        num--;
    return num;
}

int main()
{
    int T, id = 1;
    string pattern;
    cin >> T;
    while (T--) {
        cout << "Case #" << id << ": ";
        cin >> pattern;
        id++;
        cout << pancake(pattern) << endl;
    }
    
    return 0;
}