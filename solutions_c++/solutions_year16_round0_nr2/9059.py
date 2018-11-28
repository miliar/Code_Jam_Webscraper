#include <bits/stdc++.h>
using namespace std;

long long readLI()
{
    register char c;
    for(c=getchar(); !(c>='0' && c<='9'); c=getchar());
    register long long a=c-'0';
    for(c=getchar(); c>='0' && c<='9'; c=getchar())
        a=(a<<3)+(a<<1)+c-'0';
    return a;
}

int main()
{
    int t=readLI(), n, ans, i;
    char a[100];
    for(int tc=1; tc<=t; tc++)
    {
        n = ans = i = 0;
        for(char c=getchar(); c=='-' || c=='+'; c=getchar())
            a[n++] = c;
        while(i<n && a[i]=='-')
            i++;
        if(i)
            ans++;
        while(i<n)
        {
            while(i<n && a[i]=='+')
                i++;
            if(i == n)
                break;
            ans++;
            while(i<n && a[i]=='-')
                i++;
            ans++;
        }
	    cout << "Case #" << tc << ": " << ans << endl;
    }
	return 0;
}
