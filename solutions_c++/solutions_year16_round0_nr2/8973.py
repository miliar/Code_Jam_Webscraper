#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <algorithm>
#include <string>
#include <string.h>

using namespace std;  // since cin and cout are both in namespace std, this saves some text
long flipPancakes(string s);
string flip(string s, long index);
long findLast(string s, char c);

int main() {
    int t;
    string s;
    cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
    for (int i = 1; i <= t; ++i) {
        cin >> s;
        cout << "Case #" << i << ": " << flipPancakes(s) << endl;
    }
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
}

long flipPancakes(string s){
    string ideal;
    long count = 0;
    char firstChar;
    long lastIndex;
    for(long i=0; i<s.size(); i++){
        ideal.append("+");
    }
    while(s!=ideal){
        firstChar = s[0];
        lastIndex= findLast(s,firstChar);
        s = flip(s,lastIndex);
        count++;
    }
    return count;
}

string flip(string s, long index){
    char c = s[0];
    if(c=='-'){
        c='+';
    } else{
        c='-';
    }
    for(long i=0; i<index+1; i++){
        s[i] = c;
    }
    return s;
}

long findLast(string s, char c){
    long index = 0;
    while(s[index] == c){
        index++;
    }
    return index-1;
}