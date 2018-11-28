#include <iostream>
#include <fstream>
#include <cstring>

using namespace std;

class HighPrecision {
    
public:
    int Number[200];
    
    HighPrecision(char *num);
    bool IsFair();
};

bool HighPrecision::IsFair()
{
    int i;
    for (i = 199; i >=0; i--) {
        if (Number[i] != 0) {
            break;
        }
    }
    
    for (int j = i; j >= 0; j--) {
        if (Number[j] != Number[i - j]) {
            return false;
        }
        if (j == i - j + 1 || j == i - j) {
            break;
        }
    }
    return true;
}

HighPrecision::HighPrecision(char *num)
{
    int len = strlen(num);
    for (int i = 0; i < 200; i++) {
        if (i < len) {
            Number[i] = num[len - 1 - i] - '0';
        }
        else {
            Number[i] = 0;
        }
    }
}

HighPrecision operator+(HighPrecision precision1, HighPrecision precision2)
{
    HighPrecision result("0");
    int pre = 0;
    for (int i = 0; i < 200; i++) {
        result.Number[i] = precision1.Number[i] + precision2.Number[i] + pre;
        pre = result.Number[i] / 10;
        result.Number[i] = result.Number[i] % 10;
    }
    return result;
}

HighPrecision operator*(HighPrecision precision1, HighPrecision precision2)
{
    int num[400];
    memset(num, 0, sizeof(num));
    HighPrecision result("0");
    for (int i = 0; i < 200; i++) {
        for (int j = 0; j < 200; j++) {
            num[i + j] += precision2.Number[i] * precision1.Number[j];
        }
    }
    int pre = 0;
    for (int i = 0; i < 200; i++) {
        result.Number[i] = num[i] + pre;
        pre = result.Number[i] / 10;
        result.Number[i] = result.Number[i] % 10;
    }
    return result;
}

bool operator<=(HighPrecision precision1, HighPrecision precision2)
{
    for (int i = 199; i >= 0; i--) {
        if (precision1.Number[i] < precision2.Number[i]) {
            return true;
        }
        else if (precision1.Number[i] > precision2.Number[i]) {
            return false;
        }
    }
    return true;
}

bool operator>=(HighPrecision precision1, HighPrecision precision2)
{
    for (int i = 199; i >= 0; i--) {
        if (precision1.Number[i] < precision2.Number[i]) {
            return false;
        }
        else if (precision1.Number[i] > precision2.Number[i]) {
            return true;
        }
    }
    return true;
}

bool operator>(HighPrecision precision1, HighPrecision precision2)
{
    for (int i = 199; i >= 0; i--) {
        if (precision1.Number[i] < precision2.Number[i]) {
            return false;
        }
        else if (precision1.Number[i] > precision2.Number[i]) {
            return true;
        }
    }
    return false;
}

int main(void)
{
    ifstream fin("/Users/chengwayne/Downloads/C-small-attempt0.in.txt");
    ofstream fout("/Users/chengwayne/Downloads/out.txt");
    
    int t;
//    cin >>t;
    fin >>t;
    for (int i = 1; i <= t; i++) {
        char a[100], b[100];
//        cin >>a >>b;
        fin >>a >>b;

        HighPrecision ha(a), hb(b);
        int len = strlen(a);
        if (len % 2 == 0) {
            len = len / 2 - 1;
        }
        else {
            len = len / 2;
        }
        
        char s[100] = "1";
        for (int j = 0; j < len; j++) {
            strcat(s, "0");
        }
        
        int count = 0;
        
        HighPrecision p(s);
        do {
            HighPrecision result = p * p;
            if (result > hb) {
                break;
            }
            if (!p.IsFair()) {
                HighPrecision one("1");
                p = p + one;
                continue;
            }
            if (result.IsFair()) {
                if (result >= ha && result <= hb) {
                    count++;
                }
            }
            HighPrecision one("1");
            p = p + one;
        } while (true);
        
//        cout <<"Case #" <<i <<": " <<count <<endl;
        fout <<"Case #" <<i <<": " <<count <<endl;
    }
    
    return 0;
}

