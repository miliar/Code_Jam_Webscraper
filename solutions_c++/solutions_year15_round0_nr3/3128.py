#include <iostream>
#include <fstream>
#include <string>

using namespace std;


ifstream fin("input.txt");
ofstream fout("output.txt");

enum class Value {
   one, i, j, k
};
struct MValue {
    MValue() : sign(1), v(Value::one) {}
    MValue(int sign, Value v) : sign(sign), v(v) {}
    MValue(char ch) {
        sign = 1;
        switch(ch) {
            case '1' : v = Value::one;break;
            case 'i' : v = Value::i;break;
            case 'j' : v = Value::j;break;
            case 'k' : v = Value::k;break;
        }
    }
    bool operator==(const MValue& b) const {
       return sign == b.sign && v == b.v;
    }
    bool operator!=(const MValue& b) {
       return !((*this) == b);
    }
    int sign;
    Value v;
};

MValue compute_seg(const string& str, int len, int second_len);

MValue operator*(MValue a, MValue b) {
    MValue result;
    if(a.v == Value::one) result.v = b.v;
    if(b.v == Value::one) result.v = a.v;
    if(a.v == Value::i && b.v == Value::i) { result.v = Value::one; result.sign *= -1; }
    if(a.v == Value::i && b.v == Value::j) { result.v = Value::k; }
    if(a.v == Value::i && b.v == Value::k) { result.v = Value::j; result.sign *= -1; }
    if(a.v == Value::j && b.v == Value::i) { result.v = Value::k; result.sign *= -1; }
    if(a.v == Value::j && b.v == Value::j) { result.v = Value::one; result.sign *= -1; }
    if(a.v == Value::j && b.v == Value::k) { result.v = Value::i; }
    if(a.v == Value::k && b.v == Value::i) { result.v = Value::j; }
    if(a.v == Value::k && b.v == Value::j) { result.v = Value::i; result.sign *= -1; }
    if(a.v == Value::k && b.v == Value::k) { result.v = Value::one; result.sign *= -1; }
    result.sign *= a.sign;
    result.sign *= b.sign;
    return result;
}

MValue divide(MValue a, MValue b) {
    MValue result;
    result.sign = a.sign / b.sign;
    if(b.v == Value::one) result.v = a.v;
    if(a.v == Value::one) { result.v = b.v; result.sign *= -1;}
    if(a.v == Value::i && b.v == Value::i) result.v = Value::one;
    if(a.v == Value::i && b.v == Value::j) result.v = Value::k;
    if(a.v == Value::i && b.v == Value::k) {result.v = Value::j;result.sign *= -1;}
    if(a.v == Value::j && b.v == Value::i) {result.v = Value::k;result.sign *= -1;}
    if(a.v == Value::j && b.v == Value::j) result.v = Value::one;
    if(a.v == Value::j && b.v == Value::k) result.v = Value::i;
    if(a.v == Value::k && b.v == Value::i) result.v = Value::j;
    if(a.v == Value::k && b.v == Value::j) {result.v = Value::i;result.sign *= -1;}
    if(a.v == Value::k && b.v == Value::k) result.v = Value::one;
    return result;
}

MValue remove_first(MValue a, MValue b) {
    MValue result;
}

std::string solve(int l, int x, const std::string& input) {
    string str;
    MValue value_i { 1, Value::i};
    MValue value_j { 1, Value::j};
    MValue value_k { 1, Value::k};
    for(int i=0;i<x;++i) { str.append(input); }
    MValue first_seg { 1, Value::one};
    for(int first_len = 1;first_len < str.size() - 1; ++first_len) {
        first_seg = first_seg * MValue(str[first_len-1]);
        if(first_seg != value_i) continue;
        auto second_seg = MValue();
        auto third_seg = compute_seg(str, first_len, str.size() - first_len);
        for(int second_len = 1;second_len < str.size() - first_len; ++second_len) {
            second_seg = second_seg * MValue(str[first_len + second_len - 1]);
            third_seg = divide(third_seg, MValue(str[first_len + second_len - 1]));
//            std::cerr << "first_len = " << second_len;
//            std::cerr << "second_len = " << second_len;
//            std::cerr << "third_len = " << str.size() - first_len - second_len;
//            std::cerr << "\n";
            if(second_seg == value_j && third_seg == value_k) return "YES";
        }
    }
    return "NO";
}

MValue compute_seg(const string& str, int start, int len) {
    MValue result;
    for(int i = start; i != start + len; ++i) {
        result = result * MValue(str[i]);
    }
    return result;
}

int main() {
    int num_case;
    fin >> num_case;
    for(int i=0;i<num_case;++i) {
        int l, x;
        string input;
        fin >> l >> x;
        fin >> input;
        fout << "Case #" << i + 1 << ": " << solve(l, x, input) << "\n";
//        std::cerr << "Case #" << i + 1 << ": " << solve(l, x, input) << "\n";
    }

    return 0;
}