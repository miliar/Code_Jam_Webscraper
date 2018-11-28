/*
	Author:     Shreyans Doshi
	Date Time:  4/9/2016 10:54:40 AM
*/

#include <bits/stdc++.h>

using namespace std;

inline int Read()
{
	register int c=getchar();
	int x=0;
	for(;(c<48 || c>57);c=getchar());
	for(;c>47 && c<58;c=getchar())
		x=(x<<1)+(x<<3)+c-48;
	return x;
}

int main()
{
    freopen("input.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t=Read();
    for(int tt=1;tt<=t;tt++)
    {
        int ans=Read();
        if(ans==0)
        {
            printf("Case #%d: INSOMNIA\n", tt);
            continue;
        }
        set<int> a;
        int n=ans;
        while(a.size()!=10)
        {
            for(int tmp=ans;tmp;tmp/=10)
                a.insert(tmp%10);
            ans+=n;
        }
        printf("Case #%d: %d\n", tt, ans-n);
    }
    return 0;
}
