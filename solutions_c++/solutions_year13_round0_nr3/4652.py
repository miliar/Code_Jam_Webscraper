#include <cassert>
#include <cmath>
#include <cstdlib>

#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;


template <typename To, typename From>
To lexical_cast(const From& from);

bool isPalindrome(const string& s);
string truncate(const string& s);

class BigInteger {
    public:
        BigInteger();
        explicit BigInteger(const char* str);
        explicit BigInteger(const string& str);
        explicit BigInteger(const int x);
        BigInteger(const BigInteger& rhs);

        const BigInteger& operator=(const BigInteger& rhs);

        BigInteger operator*(const BigInteger& rhs) const;
        BigInteger operator+(const BigInteger& rhs) const;
        bool operator==(const BigInteger& rhs) const;
        bool operator!=(const BigInteger& rhs) const;

        const string& toString() const;

        friend ostream& operator<<(ostream& out, const BigInteger& rhs);

    private:
        string digits_;
};


int main() {
    int cases;
    cin >> cases;
    for (int i = 0; i < cases; ++i) {
        cout << "Case #" << i + 1 << ": ";

        double a, b;
        cin >> a >> b;

        int fairAndSquareCount = 0;

        BigInteger end(truncate(lexical_cast<string>(sqrt(b))));
        BigInteger j(truncate(lexical_cast<string>(sqrt(lexical_cast<double>(a)))));

        // Off by one errors :(
        if (lexical_cast<double>(j * j) < a) {
            j = j + BigInteger(1);
        }

        for(
            ;
            lexical_cast<double>(j) <= lexical_cast<double>(end);
            j = j + BigInteger(1)
        ) {
            if (!isPalindrome(j.toString())) {
                continue;
            }
            const BigInteger square = j * j;
            if (lexical_cast<double>(square) < a) {
                continue;
            }
            if (isPalindrome(j.toString()) && isPalindrome(square.toString())) {
                //cout << j << ':' << square << " is fair and square" << endl;
                ++fairAndSquareCount;
            }
        }
        cout << fairAndSquareCount << endl;
    }
    exit(EXIT_SUCCESS);
}


template <typename To, typename From>
To lexical_cast(const From& from) {
    stringstream s;
    s << from;
    To to;
    s >> to;
    return to;
}


BigInteger::BigInteger()
    : digits_("0")
{
}


BigInteger::BigInteger(const char* str)
    : digits_(str)
{
    while (digits_.size() > 0 && '0' == digits_.at(0)) {
        digits_ = digits_.substr(1);
    }
}


BigInteger::BigInteger(const string& str)
    : digits_(str)
{
    while (digits_.size() > 0 && '0' == digits_.at(0)) {
        digits_ = digits_.substr(1);
    }
}


BigInteger::BigInteger(const int x)
    : digits_(lexical_cast<string>(x))
{
}


const BigInteger& BigInteger::operator=(const BigInteger& rhs) {
    digits_ = rhs.digits_;
    return *this;
}


BigInteger::BigInteger(const BigInteger& rhs)
    : digits_(rhs.digits_)
{
}


const string& BigInteger::toString() const
{
    return digits_;
}


BigInteger BigInteger::operator*(const BigInteger& rhs) const {
    vector<BigInteger> partials;

    const string::const_iterator begin1(rhs.digits_.begin());
    for (string::const_iterator i(rhs.digits_.end() - 1); i >= begin1; --i) {
        string partial("0", partials.size());
        const int value1 = *i - '0';
        const string::const_iterator begin2(digits_.begin());
        int carry = 0;
        for (string::const_iterator j(digits_.end() - 1); j >= begin2; --j) {
            const int value2 = *j - '0';
            const int tens = (value1 * value2) / 10;
            const int ones = (value1 * value2) % 10 + carry;
            carry = tens;
            //cout << "value1 " << value1 << " value2 " << value2 << " tens " << tens << " ones " << ones << endl;

            partial = static_cast<char>(ones + '0') + partial;
        }

        if (0 != carry) {
            partial = static_cast<char>(carry + '0') + partial;
        }
        //cout << partial << endl;
        partials.push_back(BigInteger(partial));
    }

    const vector<BigInteger>::const_iterator end(partials.end());
    BigInteger sum(0);
    for (vector<BigInteger>::const_iterator i(partials.begin()); i != end; ++i) {
        sum = sum + *i;
    }

    return sum;
}


BigInteger BigInteger::operator+(const BigInteger& rhs) const {
    string partial;
    const size_t biggerSize = max(digits_.size(), rhs.digits_.size());
    int carry = 0;
    string::const_iterator lhsIter(digits_.end() - 1);
    string::const_iterator rhsIter(rhs.digits_.end() - 1);
    for (size_t i = 0; i < biggerSize; ++i) {
        const int value1 = lhsIter >= digits_.begin() ? *lhsIter - '0' : 0;
        const int value2 = rhsIter >= rhs.digits_.begin() ? *rhsIter - '0' : 0;
        --lhsIter;
        --rhsIter;
        const int tens = (value1 + value2) / 10;
        const int ones = (value1 + value2) % 10 + carry;
        carry = tens;
        //cout << "value1 " << value1 << " value2 " << value2 << " tens " << tens << " ones " << ones << endl;

        partial = static_cast<char>(ones + '0') + partial;
    }
    if (0 != carry) {
        partial = static_cast<char>(carry + '0') + partial;
    }
    return BigInteger(partial);
}


bool BigInteger::operator==(const BigInteger& rhs) const {
    return digits_ == rhs.digits_;
}


bool BigInteger::operator!=(const BigInteger& rhs) const {
    return !operator==(rhs);
}


ostream& operator<<(ostream& out, const BigInteger& rhs) {
    out << rhs.digits_;
    return out;
}


bool isPalindrome(const string& s) {
    string::const_iterator front(s.begin());
    string::const_iterator back(s.end() - 1);
    while (front < back) {
        if (*front != *back) {
            return false;
        }
        ++front;
        --back;
    }
    return true;
}


string truncate(const string& s) {
    string truncatedValue;
    const string::const_iterator end(s.end());
    for (string::const_iterator i(s.begin()); i != end; ++i) {
        if ('.' == *i) {
            return truncatedValue;
        }
        truncatedValue += *i;
    }
    return truncatedValue;
}
