#include <iostream>
#include <cstdio>
using namespace std;

typedef long long LL;

LL A, B;
LL pre[1 << 10];
int index;

bool isPal(LL num)
{
    int dig[1 << 4];
    int count = 0;
     
    while (num > 0)
    {
        dig[count++] = num % 10;  
        num /= 10;  
    } 
    
    for (int i = 0; i < count / 2; i++)
        if (dig[i] != dig[count - i - 1])
           return false;
    
    return true;
}

void precompute()
{
    index = 0; 
    for (LL base = 1; base <= 10000000; base++)
    {
        if (!isPal(base) || !isPal(base * base)) continue;
        
        pre[index++] = base * base;
    }
}

void readInput()
{
    cin >> A >> B;
}

void solve()
{   
    LL ans = 0;
    
    for (int i = 0; i < index; i++)
        if (pre[i] >= A && pre[i] <= B)
           ans++;
           
    cout << ans << endl;
}

int main()
{
    precompute();
    
    int T; cin >> T;
    
    for (int t = 1; t <= T; t++)
    {
        readInput();
        
        printf("Case #%d: ", t);
        solve();
    }
    
    return 0;
}
