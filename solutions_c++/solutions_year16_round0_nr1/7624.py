#include <iostream>

using namespace std;

long asleep_func(int n)
{
    if(n==0) return 0;
    int flg[10];
    int sum = 0;
    int ret = 1;
    for(int i=0;i<10;i++) flg[i]=0;
    for(int i=1;sum!=10;i++)
    {
        sum = 0;
        int N = n * i;
        int m = N;
        while(N)
        {
            flg[N%10] = 1;
            N /= 10;
        }
        for(int i=0;i<10;i++) sum += flg[i];
        ret = m;
    }
    return ret;
}

int main()
{
    int t;
    int n;

    cin >> t;
    for(int i=1;i<=t;i++)
    {
        cin >> n ;
        if(asleep_func(n)) cout << "Case #" << i << ": " << asleep_func(n) << endl;
        else cout << "Case #" << i << ": " << "INSOMNIA" << endl;
    }
    return 0;
}

