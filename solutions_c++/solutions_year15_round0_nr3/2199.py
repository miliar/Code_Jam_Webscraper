#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cstring>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

int multiply(int a, int b)
{
    bool neg = false;
    int retVal;
    if(a < 0)
    {
        a  *= -1;
        neg = !neg;
    }
    if(b < 0)
    {
        b  *= -1;
        neg = !neg;
    }
    
    if(a == b)
    {
        if(a == 1)
            retVal = 1;
        else
            retVal = -1;
    }
    else if(a == 1)
    {
        retVal = b;
    }
    else if(b == 1)
    {
        retVal = a;
    }
    else
    {
        int val = 9 - a - b;
        if(a < b)
        {
            retVal = val * ((a + b) % 2 ? 1 : -1 );
        }
        else
        {
            retVal = val * ((a + b) % 2 ? -1 : 1 );
        }
    }
    retVal *= (neg ? -1 : 1);
    return retVal;
}

int productSoFar[10000];
int productOfInterval(int i, int j)
{
    int leftOut = (i > 0 ? productSoFar[i-1] : 1);
    if(leftOut == 1)
    {
        return productSoFar[j];
    }
    else if(productSoFar[j] == -1)
    {
        return leftOut;
    }
    else if(productSoFar[j] == leftOut)
    {
        return 1;
    }
    else if(leftOut == 2)
    {
        return productSoFar[j] == 4 ? 3 : 4;
    }
    else if(leftOut == 3)
    {
        return productSoFar[j] == -4 ? 2 : 4;
    }

    return productSoFar[j] == 3 ? 2 : 3;
}


int main()
{
    long long T,x,l;
    cin >> T;

    for(long long t=1LL; t <= T; ++t)
    {
        string s, S;
        cin >> l >> x >> s;
        for(int i=0; i < x; ++i)
        {
            S.append(s);
        }
        int curVal = 1;
        productSoFar[0] = (S[0] == '1' ? 1 : S[0] - 'i' + 2);
        for(int i=1; i < S.size(); ++i)
            productSoFar[i] = multiply(productSoFar[i-1], (S[i] == '1' ? 1 : S[i] - 'i' + 2));

        bool found = false;
        for(int i=0; i < S.size(); ++i)
        {
            if(productSoFar[i] == 2)
            {
                for(int k=i+1; k < S.size(); ++k)
                {
                    if(productOfInterval(i+1, k) == 3)
                    {
                        if(productOfInterval(k+1, S.size()-1) == 4)
                        {
                            found = true;
                            break;
                        }
                    }
                }
                if(found)
                    break;
            }
        }

        cout << "Case #" << t << ": " << (found ? "YES" : "NO") << endl;
    }

    return 0;
}
