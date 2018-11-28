#include <iostream>
#include<string>

using namespace std;

int T;
long long N;

void prob1()
{

    long long tmp1, tmp2;
    int curN;
    cin >> T;
    int cnt = 0;


    for (int c=1; c<=T; c++)
    {
        cin >> N;
        cout << "Case #" << c << ": ";
        if (N ==0) {
            cout << "INSOMNIA\n";
            continue;
        }

        cnt = 0;
        tmp1 = N;
        long long multip = 1;
        bool arr [10] ={0};

        while ( cnt < 10)
        {
            tmp1 =tmp2= N*multip;
            multip++;

            while (tmp2 > 0)
            {
                curN = tmp2%10;
                tmp2 /= 10;

                if (!arr[curN])
                {
                    cnt++;
                    arr[curN] = true;
                }
            }

        }

        cout << tmp1 << endl;

    }

}

void prob2()
{
    cin >> T;
    string s;
    long long res;
    int sz;
    for (int c=1; c<=T; c++)
    {

        cin >> s;
        res = 0;
        cout << "Case #" << c << ": ";
        sz = s.size();

        for (int i=1; i<sz; i++)
        {
            if (s[i] != s[i-1])
                res++;

        }

        if (s[sz-1] == '-')
            res++;
        cout << res << endl;
    }

}

int main() {
   // cout << "Hello, World!" << endl;
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    //prob1();
    prob2();

    return 0;
}