#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#define rep(i, j, k) for(int i = j; i <= k; i++)

using namespace std;

int n, x, time = 0, sum, times = 0, len;

int main()
{
	//freopen ("1.out", "w", stdout);
    cin >> n;
	rep (i, 0, n - 1)
	{
        cin >> x;
        int visit[10];
        memset(visit, 0, sizeof(visit));
        sum = x;
		int fuck = 1;
        while (fuck > 0) 
		{
            times += fuck;;
            if (times > 1000000) 
				break;
            char s[1000];
            sprintf(s, "%d", sum);
            len = strlen(s);
			rep (j, 0, len)
                if (!visit[s[j] - '0']) 
					visit[s[j] - '0'] = 1, time++;
            if (time == 10)
				break;
            else
				sum += x;
        }
        if (times > 1000000) 
			cout << "Case #" << i + 1 << ": INSOMNIA" << endl;
        else 
			cout << "Case #" << i + 1 << ": " << sum << endl;
    }
    return 0;
}
