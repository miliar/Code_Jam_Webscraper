#include <iostream>
#include <string>
#include <sstream>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int findDigit(long long N)
{
    int digit = 0;
    while (N > 0)
    {
        digit++;
        N = N/10;
    }
    return digit;
}
int revs(long long cur)
{
    long long r=0;
    int b=0;
    while(cur > 0)
    {
        b = cur % 10;
        cur = cur / 10;
        r = r*10 +b;
    }

    return r;
}

int getComp(int d)
{
    long long r=1;
    d--;
    while(d>0)
    {
        r *= 10;
        d--;
    }
    return r;
}
int main()
{
    freopen("D:\\GoogleCodeJam\\in.txt","r",stdin);
    freopen("D:\\GoogleCodeJam\\out.txt","w",stdout);

    int TestNum = 0;
    cin >> TestNum;
    for (int testCase = 0;testCase < TestNum;testCase++)
	{
	    long long N;
	    cin >> N;
	    int digit = findDigit(N);

        long long result = 0;
        long long cur = 0;
        if (N <=19) {result = N;cur=N;}
        else
        {
            result = 10;
            cur = 10;
            for (int d=3;d<=digit;d++)
            {
                int da = d-1;
                int half = da/2;
                long long halfNum=0;
                while(half>0)
                {
                    halfNum *= 10;
                    halfNum += 9;
                    half--;
                }
                result += halfNum;
                cur += halfNum;
                cur = revs(cur);
                result ++;
                long long target = getComp(d);
                result += target - cur;
                cur = target;
            }


            if (N > cur)
            {
                long long temCur = cur;
                long long gap = 0;
                long long fly = 0, reFly=0;

                while(temCur < N)
                {
                    temCur++;
                    long long re = revs(temCur);
                    long long temGap = re -temCur;
                    if (re <= N && gap < temGap)
                    {
                        gap=temGap;
                        fly=temCur;
                        reFly=re;
                    }
                }

                if (gap > 0)
                {
                    result += (fly-cur)+1+(N-reFly);
                }else{
                    result += (N-cur);
                }
            }
        }

        if (testCase != 0) cout << endl;
        cout << "Case #" << (testCase + 1) << ": " << result;
	}
    return 0;
}
