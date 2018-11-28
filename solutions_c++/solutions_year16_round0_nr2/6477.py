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
	    char pank[101];
	    scanf("%s", pank);
	    long long i = 0, j = i+1, counter = 0;
	    while(i <= j && j < strlen(pank))
        {
            if(pank[i] == pank[j])
            {
                i++;
                j++;
            }
            else if(pank[j] != '\n')
            {
                counter++;
                i++;
                j++;
            }
        }
        if(pank[i] == '-' && strlen(pank) == 1)
            printf("Case #%d: %d\n", t, 1);
        else if(pank[i] == '-')
            printf("Case #%d: %lld\n", t, counter+1);
        else
            printf("Case #%d: %lld\n", t, counter);
        t++;
    }

    fclose (stdin);
    fclose (stdout);
    return 0;
}
