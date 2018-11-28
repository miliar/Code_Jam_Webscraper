using namespace std;

#include <iostream>
#include <string>
#include <cstdlib>
#include <cctype>
#include <fstream>
#include <cmath>
#include <sstream>

bool isPalindrome(string s)
{
    if (s == string(s.rbegin(), s.rend())) {
        return true;
    }
    return false;
}

bool isSquare(int x)
{
    double d_sqrt = sqrt(x);
    int i_sqrt = d_sqrt;
    if(d_sqrt == i_sqrt)
        return true;

    return false;
}

string ConvertIntToStr(int y)
{
   stringstream ss;
   ss << y;
   return ss.str();
}

int main()
{
    ifstream in;
    in.open ("C-small-attempt0.in");
    ofstream out;
    out.open ("C-small-attempt0.out");
    int n, A, B, j, count;
    in >> n;

    for(int i = 0; i < n; i++)
    {
        in >> A;
        in >> B;
        count = 0;

        for(j = A; j <= B; j++)
            if(isPalindrome(ConvertIntToStr(j)) && isSquare(j) && isPalindrome(ConvertIntToStr((int) sqrt(j))))
                count++;

        out << "Case #" << i+1 << ": " << count << endl;
    }

    in.close();
    out.close();

    return 0;
}
