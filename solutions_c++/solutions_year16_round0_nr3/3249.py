#include <bits/stdc++.h>
using namespace std;
vector<int> number;
int jamcoins=0;
const int N=14;
const int J=50;
vector<int> primes;
int mark[10000010];
inline void sieve(int B)
{
    if (B > 1) primes.push_back(2);
    for (int i=3;i<=B;i+=2)
    {
        if (!mark[i])
        {
            primes.push_back(i);
            if (i<=sqrt(B)+1)  for (int j=i*i;j<=B;j+=i) mark[j]=i;
        }
    }
}
long long findSmallestFactor(long long x)
{
    for(long long i=2;i*i<=x;i++) if(x%i==0) return i;
    return -1;
}
vector<long long> isJamcoin()
{
    long long Number=0;
    vector<long long> ret;
    for(int base=2;base<=10;base++){
        Number++;
        long long exp=base;
        for(int i=N-1;i>=0;i--) {
            Number+=number[i]*exp;
            exp*=base;
        }
        Number+=exp;
        long long fac;
        if(Number<10000000) {fac=mark[Number];
        if(fac==0) fac=-1;} else
        fac=findSmallestFactor(Number);
        /*cout << Number << endl;
        cout << fac << endl;*/
        if(fac==-1)
        {
            vector<long long> dummy;
            dummy.push_back(-1);
            return dummy;
        }
        ret.push_back(fac);
    }
    return ret;
}
int outputd=1;
void output(vector<long long> ret)
{
    cout << 1;
    for(int i=0;i<number.size();i++) cout << number[i];
    cout << 1;
    for(int i=0;i<ret.size();i++) cout << " " << ret[i];
    cout << endl;
    if(outputd==J) exit(0);
    outputd++;
}
void gen(int len)
{
    if(len==N)
    {
        vector<long long> num=isJamcoin();
        if(num[0]==-1) return;
        output(num);
        return;
    }
    number.push_back(0);
    gen(len+1);
    number.pop_back();
    number.push_back(1);
    gen(len+1);
    number.pop_back();
}

int main()
{
    freopen("out.txt","w",stdout);
    sieve(10000000);
    /*number.push_back(0);
        number.push_back(0);

    number.push_back(0);

    number.push_back(0);

    number.push_back(0);
    number.push_back(0);
    number.push_back(0);
    number.push_back(0);
    number.push_back(0);
    number.push_back(0);
    number.push_back(0);

    number.push_back(0);
    number.push_back(1);
    number.push_back(0);
    vector<long long> xyz=isJamcoin();
    //for(int i=0;i<xyz.size();i++) cout << xyz[i] << endl;*/
    cout << "Case #1:" << endl;
    gen(0);
    return 0;
}
