#include <bits/stdc++.h>

using namespace std;

int main(int argc,char *argv[])
{
    int T;
    cin >> T;
    for (int t=0;t<T;t++)
    {
        int N;
        cin >> N;
        int seen = 0;
        long long v = N;
        int cnt = 0;
        for (;;)
        {
            cnt++;
            stringstream ss;
            ss << v;
            for (int i=0;i<ss.str().length();i++)
                seen |= 1<<(ss.str()[i]-'0');
            if (seen==1023)
            {
                cout << "Case #" << t+1 << ": " << v << endl;
                break;
            }
            v += N;
            if (cnt>1000000)
            {
                cout << "Case #" << t+1 << ": INSOMNIA" << endl;
                break;
            }
        }
    }
    return 0;
}
