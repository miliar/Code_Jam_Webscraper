#include <bits/stdc++.h>

using namespace std;

main ()
{
    freopen("input2.in","r",stdin);
    freopen("output2.in", "w",stdout);

    int T, t = 1;
	scanf("%d", &T);
	while(t <= T)
	{
	    long long N, i = 0, digit, temp;
	    int digits[10] = {0};

	    scanf("%lld", &N);
	    if(N == 0)
        {
            printf("Case #%d: ", t);
            printf("INSOMNIA\n");
            t++;
            continue;
        }
	    char flag = true;
        while(flag)
        {
            i++;
            temp = i * N;
            while(temp != 0)
            {
                digit = temp%10;
                temp = temp/10;
                digits[digit] = 1;
            }
            if(digits[0] == 1 && digits[1] == 1 && digits[2] == 1 && digits[3] == 1 && digits[4] == 1 && digits[5] == 1 && digits[6] == 1 && digits[7] == 1 && digits[8] == 1 && digits[9] == 1)
                flag = false;
        }
        if(flag == false)
            printf("Case #%d: %lld\n", t, i*N);

        t++;
    }

    fclose (stdin);
    fclose (stdout);
    return 0;
}
