#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cmath>
using namespace std;

long power(long x)
{
    int s = 1;
    for (int i=1;i<=x;i++)
        s*=10;
    return s;
}

bool palindrome(long test)
{
    char buf[100]; long len;
    sprintf(buf, "%ld", test);
    len = strlen(buf);
    for (int i=0;i<len;i++)
        if (buf[i] != buf[len-1-i])
            return false;
    return true;
}

long concat(long i, long flag)
{
    char buf[100];
    sprintf(buf, "%ld", i);
    int len = strlen(buf);
    int st = len-flag;
    for (int i = 0; i<len;i++)
        buf[st+i]=buf[st-i-(1-flag)];
    buf[len*2-flag]=0;
    return atol(buf);

}

long Produce(long len, long cap1, long cap2)
{
    long count = 0;
    long half = (len+1)/2;
    long st = power(half-1), en=power(half)-1;
    for (int i=st; i<=en;i++)
    {
        long result = concat(i, len%2);
        if (result>=cap1 && result<=cap2)
            if (palindrome(result*result))
                count++;
    }
    return count;
}

void real_main()
{
    long A, B;
    cin>>A>>B;
    long A0 = (long) ceil(sqrt(A));
    long B0 = (long) floor(sqrt(B));

    char buffer[100];
    sprintf(buffer, "%ld", A0);
    long Al = strlen(buffer);
    
    sprintf(buffer, "%ld", B0);
    long Bl = strlen(buffer);

    long S = 0;

    for (int i=Al; i<=Bl; i++)
        S+=Produce(i, A0, B0);
    cout<<S<<endl;

}

int main()
{
    int T; cin>>T;
    for (int i=0; i<T;i++)
    {
        cout<<"Case #"<<i+1<<": ";
        real_main();
    }
    return 0;
}
