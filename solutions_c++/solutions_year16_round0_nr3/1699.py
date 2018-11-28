#include <cstdio>
#include <vector>
#include <iostream>
using namespace std;

typedef long long ll;

int val[32];
vector<int> res;

bool check(int base, int r)
{
    int sum = 0;
    int now = 1;
    for (int i = 0; i < 32; ++i)
    {
        if (val[i] == 1)
        {
            sum += now;
        }
        now = now * base % r;
    }
    
    sum = sum % r;
    return sum == 0;
}

bool mychecker(ll N)
{
    int betweenCount = 0;
    for (int i = 0; i < 32; ++i)
    {
        if (N & (1ll << i))
        {
            val[i] = 1;
        }
        else
        {
            val[i] = 0;
        }
        if (i > 0 && i < 31)	betweenCount += val[i];
    }

    if (betweenCount % 2 != 0)	return false;
    
    res.clear();
    
    if (check(2, 3))
    {
        res.push_back(3);
        res.push_back(2);
    }
    else
    {
        return false;
    }
    
    if (check(4, 3))
    {
        res.push_back(3);
    }
    else if (check(4, 5))
    {
        res.push_back(5);
    }
    else
    {
        return false;
    }
    res.push_back(2);
    
    if (check(6, 7))
    {
        res.push_back(7);
    }
    else
    {
        return false;
    }
    res.push_back(2);
    
    if (check(8, 3))
    {
        res.push_back(3);
    }
    else
    {
        return false;
    }
    res.push_back(2);
    
    if (check(10, 3))
    {
        res.push_back(3);
        return true;
    }
    
    if (check(10, 7))
    {
        res.push_back(7);
        return true;
    }
    
    if (check(10, 11))
    {
        res.push_back(11);
        return true;
    }
    
    return false;
}


int main()
{
    printf("Case #1:\n");
    ll Min = (1ll << 31) + 1;
    ll Max = (1ll << 32);
    //printf("%lld %lld\n", Min, Max);
    int count = 0;
    for (ll i = Min; i < Max; i += 2)
    {
        if (mychecker(i))
        {
            count ++;
            for (int j = 31; j >=0; --j)	printf("%d", val[j]);
            for (int j = 0; j < 9; ++j)	printf(" %d", res[j]);
            printf("\n");
        }
        if (count == 500)	break;
    }
    return	0;
}
