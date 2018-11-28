#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>

using namespace std;
const char* fi = "C-small-attempt1.in";
const char* fo = "output.txt";
const double eps = 1E-9;

unsigned long long A,B;

bool IsPalind(unsigned long long x);
int Count(unsigned long long L, unsigned long long R, short k);
int Reverse(int x);

int main()
{
    freopen(fi,"r",stdin);
    freopen(fo,"w",stdout);
    int nTest;
    cin >> nTest;
    for (int test=1; test<=nTest; test++)
    {
        cin >> A >> B;
        cout << "Case #" << test << ": ";
        unsigned long long result = 0;
        int L = max((int)(log10(sqrt(A))+1+eps),1);
        int R = max((int)(log10(sqrt(B))+1+eps),1);
        for (int i=L; i<=R; i++)
            result = result + Count(A,B,i);
        cout << result << endl;
    }

    //Count(1000,10000,4);
    return 0;
}

int Reverse(int x)
{
    int result = 0;
    while (x>0)
    {
        result = result*10 + x%10;
        x /=10;
    }
    return result;
}

bool IsPalind(unsigned long long x)
{
    string s = "";
    while (x>0)
    {
        s = char(x%10+48) + s;
        x/=10;
    }
    for (unsigned int i=0; i<s.length()/2; i++)
        if (s[i]!=s[s.length()-i-1]) return false;
    return true;
}

int Count(unsigned long long L, unsigned long long R, short k)
{
    unsigned long long result = 0;
    if (k==1)
    {
        if (L<=1 && R>=1) result++;
        if (L<=4 && R>=4) result++;
        if (L<=9 && R>=9) result++;
        return result;
    }
    if (k%2==0)
    {
        for (int i=(int)(pow(10,k/2-1)+eps); i<=(int)(pow(10,k/2)+eps)-1; i++)
        {
            int tmp = i*(int)(pow(10,k/2)+eps)+Reverse(i);
            unsigned long long sqrTmp = tmp*tmp;
            if (IsPalind(sqrTmp) && sqrTmp>=L && sqrTmp<=R) result++;
        }
    }
    else
    {
        for (int j=0; j<=9; j++)
            for (int i=(int)(pow(10,k/2-1)+eps); i<=(int)(pow(10,k/2)+eps)-1; i++)
            {
               // int b = i*(int)pow(10,k/2+1);
                int tmp = i*(int)(pow(10,k/2+1)+eps)+j*(int)(pow(10,k/2)+eps)+Reverse(i);
                unsigned long long sqrTmp = tmp*tmp;
                if (IsPalind(sqrTmp) && sqrTmp>=L && sqrTmp<=R) result++;
            }
    }
    return result;
}
