#include <bits\stdc++.h>

std::string solve(std::string str); 

using namespace std;

int main(){
    int t;
    cin >> t;
    for (int i = 0; i < t; i++){
        string str;
        cin >> str;
        string ret = solve(str);
        
        cout << "Case #" << i + 1 << ": " << ret << endl;
    }
}

string solve(string str){
    map <char, int> counts;
    for (int i = 0; i < str.size(); i++){
        counts[str[i]]++;
    }
    
    string ret;
    while(counts['Z'] > 0){
        ret.push_back('0');
        counts['Z']--;
        counts['E']--;
        counts['R']--;
        counts['O']--;
    }
    
    int twos = 0;
    while(counts['W'] > 0){
        twos++;
        counts['T']--;
        counts['W']--;
        counts['O']--;
    }
    
    int fours = 0;
    while(counts['U'] > 0){
        fours++;
        counts['F']--;
        counts['O']--;
        counts['U']--;
        counts['R']--;
    }
    
    int sixs = 0;
    while(counts['X'] > 0){
        sixs++;
        counts['S']--;
        counts['I']--;
        counts['X']--;
    }
    
    int eights = 0;
    while(counts['G'] > 0){
        eights++;
        counts['E']--;
        counts['I']--;
        counts['G']--;
        counts['H']--;
        counts['T']--;
    }
    
    int threes = 0;
    while(counts['H'] > 0){
        threes++;
        counts['T']--;
        counts['H']--;
        counts['R']--;
        counts['E']--;
        counts['E']--;
    }
    
    int fives = 0;
    while(counts['F'] > 0){
        fives++;
        counts['F']--;
        counts['I']--;
        counts['V']--;
        counts['E']--;
    }
    
    int ones = 0;
    while(counts['O'] > 0){
        ones++;
        counts['O']--;
        counts['N']--;
        counts['E']--;
    }
    
    int sevens = 0;
    while(counts['V'] > 0){
        sevens++;
        counts['S']--;
        counts['E']--;
        counts['V']--;
        counts['E']--;
        counts['N']--;        
    }
    
    int nines = 0;
    while(counts['N'] > 0){
        nines++;
        counts['N']--;
        counts['I']--;
        counts['N']--;
        counts['E']--;
    }
    
    for (int i = 0; i < ones; i++){
        ret.push_back('1');
    }
    for (int i = 0; i < twos; i++){
        ret.push_back('2');
    }
    for (int i = 0; i < threes; i++){
        ret.push_back('3');
    }
    for (int i = 0; i < fours; i++){
        ret.push_back('4');
    }
    for (int i = 0; i < fives; i++){
        ret.push_back('5');
    }
    for (int i = 0; i < sixs; i++){
        ret.push_back('6');
    }
    for (int i = 0; i < sevens; i++){
        ret.push_back('7');
    }
    for (int i = 0; i < eights; i++){
        ret.push_back('8');
    }
    for (int i = 0; i < nines; i++){
        ret.push_back('9');
    }
    
    return ret;
}