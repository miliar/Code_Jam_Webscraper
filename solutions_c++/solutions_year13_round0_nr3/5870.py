#include <iostream>
#include <sstream>
#include <string>
#include <cmath>

using namespace std;

template<class T>
std::string ConvertToString(T);

template <class T>
std::string ConvertToString(T value)
{
    std::stringstream ss;
    ss << value;
    return ss.str();
}

bool is_palindrome(string& str)
{
    string::iterator it;
    string::reverse_iterator rit;
    for (it = str.begin(), rit = str.rbegin(); it != str.end() && rit != str.rend(); ++it, ++rit) {
        if (*it != *rit)
            return false;
    }
    return true;
}

int T, A, B;
int ans;
int cnt[1001];
bool tbl[1001];

void cal()
{
    for (int i = 0; i <= 1000; ++i) {
        cnt[i] = 0;
        tbl[i] = false;
    }

    for (int i = 1; i <= 1000; ++i) {
        int ii = i*i;
        if (ii <= 1000) {
            string s1 = ConvertToString(i);
            string s2 = ConvertToString(ii);
            if (is_palindrome(s1) && is_palindrome(s2)) {
                cnt[ii] = 1;
                tbl[ii] = true;
            }
        }
    }
    
    for (int i = 1; i <= 1000; ++i)
        cnt[i] += cnt[i-1];
}

int main()
{

    cal();
    scanf("%d\n", &T);
    for (int i = 1; i <= T; ++i) {
        scanf("%d %d\n", &A, &B);
        printf("Case #%d: %d\n", i, cnt[B]-cnt[A-1]);

    }
    return 0;
}

