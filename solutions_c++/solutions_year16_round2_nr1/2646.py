#include <iostream>
#include <algorithm>

#define BUFFER 2048

int emptyarray(int nums[26]) 
{
    for (int i = 0; i < 26; i++) {
        if (nums[i]) {
            return 0;
        }
    }

    return 1;
}

int removenumber(int lettercount[26], const char *s)
{
    while (*s != '\0') {
        lettercount[*s-'A'] -= 1;
        s++;
    }

    if (lettercount[*s - 'A'] <  0) {
        std::cout << "oops remove number below 0\n";
        exit(1);
    }

    return 0;
}

int findnumber(char *s) 
{
    int lettercount[26];
    char numberstring[2000];
    int index = 0;
    memset(lettercount, 0, sizeof(int) * 26);

    while (*s != '\0') {
        lettercount[*s - 'A'] += 1;
        s++;
    }

    while (emptyarray(lettercount) == 0) {
        if (lettercount['Z' - 'A']) {
            numberstring[index++] = '0'; 
            removenumber(lettercount, "ZERO");
        } else if (lettercount['W' - 'A']) {
            numberstring[index++] = '2'; 
            removenumber(lettercount, "TWO");
        } else if (lettercount['U' - 'A']) {
            numberstring[index++] = '4'; 
            removenumber(lettercount, "FOUR");
        } else if (lettercount['X'- 'A']) {
            numberstring[index++] = '6'; 
            removenumber(lettercount, "SIX");
        } else if (lettercount['G'- 'A']) {
            numberstring[index++] = '8'; 
            removenumber(lettercount, "EIGHT");
        } else if (lettercount['O'- 'A']) {
            numberstring[index++] = '1'; 
            removenumber(lettercount, "ONE");
        } else if (lettercount['H'- 'A']) {
            numberstring[index++] = '3'; 
            removenumber(lettercount, "THREE");
        } else if (lettercount['S'- 'A']) {
            numberstring[index++] = '7'; 
            removenumber(lettercount, "SEVEN");
        } else if (lettercount['V'- 'A']) {
            numberstring[index++] = '5'; 
            removenumber(lettercount, "FIVE");
        } else if (lettercount['N'- 'A']) {
            numberstring[index++] = '9'; 
            removenumber(lettercount, "NINE");
        } else {
            std::cout << "Something wrong here!\n";
            exit(1);
        }
        
    }

    
    numberstring[index] = '\0';

    std::string mystring = std::string(numberstring);
    std::sort(std::begin(mystring), std::end(mystring));
    std::cout << mystring << std::endl;

    return 0;
}

int main(int argc, char *argv[])
{
    int testcases;
    char s[BUFFER];

    scanf("%d", &testcases);
    
    for (int i = 0; i < testcases; i++) {
        scanf("%s", s);
        std::cout << "Case #" << i + 1 << ": ";
        findnumber(s);
    }

    return 0;
}
