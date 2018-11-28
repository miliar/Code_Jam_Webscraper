#include<cstdio>
#include<cstring>
#include<map>
#include<vector>
using namespace std;

int main(){
    int T, C=1, m;
    map<char, int> counts;
    vector<int> digits;
    scanf("%d", &T);
    while(T--){
        char s[1<<11];
        counts.clear(); digits.clear(); digits.resize(10, 0);
        scanf("%s", s);
        for(int i = 0; i < strlen(s); ++i){
            if(counts.count(s[i])) ++counts[s[i]];
            else counts[s[i]] = 1;
        }
        if(counts.count('Z')){
            m = counts['Z'];
            digits[0] = m;
            counts['Z'] -= m;
            counts['E'] -= m;
            counts['R'] -= m;
            counts['O'] -= m;
        }
        if(counts.count('W')){
            m = counts['W'];
            digits[2] = m;
            counts['T'] -= m;
            counts['W'] -= m;
            counts['O'] -= m;
        }
        if(counts.count('U') && counts['U']){
            m = counts['U'];
            digits[4] = m;
            counts['F'] -= m;
            counts['O'] -= m;
            counts['U'] -= m;
            counts['R'] -= m;
        }
        if(counts.count('X') && counts['X']){
            m = counts['X'];
            digits[6] = m;
            counts['S'] -= m;
            counts['I'] -= m;
            counts['X'] -= m;
        }
        if(counts.count('G') && counts['G']){
            m = counts['G'];
            digits[8] = m;
            counts['E'] -= m;
            counts['I'] -= m;
            counts['G'] -= m;
            counts['H'] -= m;
            counts['T'] -= m;
        }
        if(counts.count('O') && counts['O']){
            m = counts['O'];
            digits[1] = m;
            counts['O'] -= m;
            counts['N'] -= m;
            counts['E'] -= m;
        }
        if(counts.count('T') && counts['T']){
            m = counts['T'];
            digits[3] = m;
            counts['T'] -= m;
            counts['H'] -= m;
            counts['R'] -= m;
            counts['E'] -= m;
            counts['E'] -= m;
        }
        if(counts.count('F') && counts['F']){
            m = counts['F'];
            digits[5] = m;
            counts['F'] -= m;
            counts['I'] -= m;
            counts['V'] -= m;
            counts['E'] -= m;
        }
        if(counts.count('S') && counts['S']){
            m = counts['S'];
            digits[7] = m;
            counts['S'] -= m;
            counts['E'] -= m;
            counts['V'] -= m;
            counts['E'] -= m;
            counts['N'] -= m;
        }
        if(counts.count('I') && counts['I']){
            m = counts['I'];
            digits[9] = m;
        }
        printf("Case #%d: ", C++);
        for(int i = 0; i < 10; ++i){
            for(int j = 0; j < digits[i]; ++j)
                printf("%d", i);
        }
        printf("\n");
    }
}
