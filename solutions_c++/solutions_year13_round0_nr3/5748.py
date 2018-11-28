#include <iostream>
#include <fstream>
#include <string>
#include <cmath>

using namespace std;

bool isPalindrome(double i)
{
    int n = i;
    int temp=n;
    int r = 0;
    //cout << temp << " ";
    while(n>0)
    {
        r=r*10+n%10;
        n=n/10;
    }
    if(temp==r)
    {
        return true;
    }
    else
    {
        return false;
    }
}
int fairNums(long a, long b)
{
    long count = 0;
    for(long i = a; i <= b; i++)
    {
        if(isPalindrome(i))
        {
            double root = sqrt(i);
            if(root == (int)root)
        {
            if(isPalindrome(root))
            {
      //          cout << "sqrt is palindrome\n";
                count++;
            }
        }
        }
    }

    return count;
}

int main()
{
    fstream in("C-small-attempt0.in", ios::in);
    fstream out("output.txt", ios::out);
    int t;
    long a, b;

    in >> t;
    for(int i = 0; i < t; i++)
    {
        in >> a >> b;

        long result = fairNums(a,b);

        out << "Case #" << i+1 <<": " << result << endl;
    }

    in.close();
    out.close();
    return 0;
}
