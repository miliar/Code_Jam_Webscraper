#include<iostream>
#include<string>
#include<cstdlib>
#include<sstream>

using namespace std;

bool isp(unsigned long long x)
{
    stringstream ss;
    ss << x;
    string s(ss.str());

    int len = s.length();
    for(int i=0,j=len-1;i<j;i++,j--)
    {
        if(s[i]!=s[j])
            return false;
    }

    return true;
}

bool issq(unsigned long long num)
{
    unsigned long long i,t;

    for(i=0,t=0;t<=num;i++,t=i*i)
    {
        if(t == num)
            return isp(i);
    }

    return 0;
}


int main()
{
    int T,tt;
    unsigned long long a,b,i,ans;
    cin >> T;

    for(tt=1;tt<=T;tt++)
    {

        cin >> a >> b;
        for(i=a,ans=0;i<=b;i++)
        {
            if(isp(i))
                if(issq(i))
                    ans++;
        }

        cout << "Case #" << tt << ": " << ans << endl;

    }
    return 0;
}
