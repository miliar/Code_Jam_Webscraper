#include <iostream>
#include <fstream>
using namespace std;

struct Quaternion {
    bool positive;
    enum Char {
        I = 0, J = 1, K = 2, ONE = 3
    } value;
    static Char get(char c) {
        if(c == 'i') return I;
        if(c == 'j') return J;
        if(c == 'k') return K;
    }
    Quaternion() = default;
    Quaternion(bool positive, Char value) : positive(positive), value(value) {}
    Quaternion operator *(const Quaternion &other) const {
        Quaternion result;
        result.positive = !(positive ^ other.positive);
        if(value == ONE) result.value = other.value;
        else if(other.value == ONE) result.value = value;
        else if(value == other.value) {
            result.positive = !result.positive;
            result.value = ONE;
        } else {
            result.value = static_cast<Char>(3 - value - other.value);
            if(other.value != (value + 1) % 3) result.positive = !result.positive;
        }
        return result;
    }
    bool operator ==(const Quaternion &other) const {
        return positive == other.positive && value == other.value;
    }
};
int main() {
    ifstream inf("C-small-attempt0.in");
    ofstream ouf("output.txt");
    int T; inf >> T;
    for(int t = 1; t <= T; ++t) {
        int L, X; inf >> L >> X;
        string pattern; inf >> pattern;
        string s;
        for(int x = 0; x < X; ++x) {
            s += pattern;
        }
        Quaternion current = Quaternion(true, Quaternion::Char::ONE);
        Quaternion i = Quaternion(true, Quaternion::Char::I);
        Quaternion k = Quaternion(true, Quaternion::Char::K);
        Quaternion fin = Quaternion(false, Quaternion::Char::ONE);
        bool met_i = false, met_k = false;
        for(int l = 0; l < s.length(); ++l) {
            current = current * Quaternion(true, Quaternion::get(s[l]));
            if(current == i) met_i = true;
            else if(current == k && met_i) met_k = true;
        }
        bool answer;
        if(met_i && met_k && current == fin) answer = true;
        else answer = false;
        ouf << "Case #" << t << ": " << (answer ? "YES" : "NO") << endl;
    }
    return 0;
}