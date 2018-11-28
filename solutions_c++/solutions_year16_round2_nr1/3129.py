#include <iostream>
#include "string"

using namespace std;

bool comp(char c1, char c2)
{
    return tolower(c1) < tolower(c2);
}

int main() {
    
    int t, j, cnt;
    string s;
    string res;
    
    cin >> t;
    
    for (int i = 1; i <= t; ++i) {
        
        s.clear();
        res.clear();
        
        cin >> s;

        // zero
        
        while (s.find('Z')!=std::string::npos & s.find('E')!=std::string::npos & s.find('R')!=std::string::npos & s.find('O')!=std::string::npos) {
            res += '0';
            s.erase(s.find('Z'), 1);
            s.erase(s.find('E'), 1);
            s.erase(s.find('R'), 1);
            s.erase(s.find('O'), 1);
        }
        
        while (s.find('T')!=std::string::npos & s.find('W')!=std::string::npos & s.find('O')!=std::string::npos) {
            res += '2';
            s.erase(s.find('T'), 1);
            s.erase(s.find('W'), 1);
            s.erase(s.find('O'), 1);
        }
        
        while (s.find('F')!=std::string::npos & s.find('O')!=std::string::npos & s.find('U')!=std::string::npos & s.find('R')!=std::string::npos) {
            res += '4';
            s.erase(s.find('F'), 1);
            s.erase(s.find('O'), 1);
            s.erase(s.find('U'), 1);
            s.erase(s.find('R'), 1);
        }
        
        while (s.find('S')!=std::string::npos & s.find('I')!=std::string::npos & s.find('X')!=std::string::npos) {
            res += '6';
            s.erase(s.find('S'), 1);
            s.erase(s.find('I'), 1);
            s.erase(s.find('X'), 1);
        }
        
        while (s.find('E')!=std::string::npos & s.find('I')!=std::string::npos & s.find('G')!=std::string::npos & s.find('H')!=std::string::npos & s.find('T')!=std::string::npos) {
            res += '8';
            s.erase(s.find('E'), 1);
            s.erase(s.find('I'), 1);
            s.erase(s.find('G'), 1);
            s.erase(s.find('H'), 1);
            s.erase(s.find('T'), 1);
        }
        
        
        
        while (s.find('O')!=std::string::npos & s.find('N')!=std::string::npos & s.find('E')!=std::string::npos) {
            res += '1';
            s.erase(s.find('O'), 1);
            s.erase(s.find('N'), 1);
            s.erase(s.find('E'), 1);
        }
        

        
        
        while (s.find('T')!=std::string::npos & s.find('H')!=std::string::npos & s.find('R')!=std::string::npos & s.find('E')!=std::string::npos & s.find('E')!= s.rfind('E')) {
            res += '3';
            s.erase(s.find('T'), 1);
            s.erase(s.find('H'), 1);
            s.erase(s.find('R'), 1);
            s.erase(s.find('E'), 1);
            s.erase(s.find('E'), 1);
        }
        

        
        while (s.find('F')!=std::string::npos & s.find('I')!=std::string::npos & s.find('V')!=std::string::npos & s.find('E')!=std::string::npos) {
            res += '5';
            s.erase(s.find('F'), 1);
            s.erase(s.find('I'), 1);
            s.erase(s.find('V'), 1);
            s.erase(s.find('E'), 1);
        }
        

        
        while (s.find('S')!=std::string::npos & s.find('E')!=std::string::npos & s.find('V')!=std::string::npos & s.find('N')!=std::string::npos) {
            res += '7';
            s.erase(s.find('S'), 1);
            s.erase(s.find('E'), 1);
            s.erase(s.find('V'), 1);
            s.erase(s.find('E'), 1);
            s.erase(s.find('N'), 1);
        }
        

        
        while (s.find('N')!=std::string::npos & s.find('I')!=std::string::npos & s.find('N')!=std::string::npos & s.find('E')!=std::string::npos) {
            res += '9';
            s.erase(s.find('N'), 1);
            s.erase(s.find('I'), 1);
            s.erase(s.find('N'), 1);
            s.erase(s.find('E'), 1);
        }
        
        sort(res.begin(), res.end(), comp);
        
        cout << "Case #" << i << ": " << res << endl;
        
        
    }
}