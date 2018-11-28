#include <iostream>
#include <fstream>
#include <string>
using namespace std;

const char PLUS = '+';
const char MINUS = '-';

#define HAPPY_FACE 0
#define BLANK_FACE 1

#define flip_char(c)                             \
    ((c == PLUS)?MINUS:PLUS)

void flip_str(string& s, int end_pos) 
{
    for(int i = 0; i < end_pos; i++) {
        s[i] = flip_char(s[i]);
    }    
}

bool all_happy(string& s, int len) 
{
    for(int i = 0; i < len; i++) {
        if(s[i] == MINUS) 
            return false;
    }
    return true;
}

int flip_count(string& test_input)
{
    int count = 0;
    size_t len = test_input.length();
    if(!len) 
        return -1;
    else if(len == 1) {
        if(test_input[0] == MINUS) {
            return 1;
        } else {
            return 0;
        }
    }
    
    const char first = test_input[0];
    size_t pos = 1;

    char next_char_to_find = flip_char(first);
    size_t find_pos = 0;

    while(pos < len) {
        if(all_happy(test_input, len)) {
            return count;
        }

        find_pos = test_input.find(next_char_to_find, 
                                   pos);
        if(find_pos == string::npos) {            
            flip_str(test_input, len);
            count++;
            break;
        }
        flip_str(test_input, find_pos);
        count++;
        next_char_to_find = flip_char(next_char_to_find);
        pos = find_pos;
    }
    return count;
}


int main()
{
    int test_cases;
    string test_input;
    ifstream infile("B-large.in");
    if(!infile) {
        cerr << " Could not read input file" << endl;
        return 0;
    }

    infile >> test_cases;
    for(int i = 1; i <= test_cases; i++) {
        infile >> test_input;
        
        int fc = flip_count(test_input);
        if(fc != -1) {
            cout << "Case #" << i << ": " << fc << endl;
        } else {
            cout << "ERROR: can't determine flip_count " << endl;
            continue;
        }
    }
    return 0;
}
