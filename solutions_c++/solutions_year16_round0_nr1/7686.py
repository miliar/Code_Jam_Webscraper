#include <iostream>
#include <vector>
using namespace std;

bool isGood(vector<bool> &v)
{
    for(int i=0;i<v.size();i++)
    {
        if(!v[i])
            return false;
    }
    return true;
}

long long solution(long long n)
{
    vector<bool> seen(10, false);
    long long next  = n;
    while(true) 
    {
        long long nn = next;
        while(nn)
        {
            seen[nn%10] = true;
            nn /= 10;
        }
        if (isGood(seen))
            return next;
        next = next + n;
    }
}

int main()
{
    int T;
    cin>>T;
    for(int i=0;i<T;++i)
    {
        long long t;
        cin>>t;
        cout<<"Case #"<<i+1<<": ";
        if(!t)
            cout<<"INSOMNIA"<<endl;
        else
            cout<<solution(t)<<endl;
    }
    return 0;
}
