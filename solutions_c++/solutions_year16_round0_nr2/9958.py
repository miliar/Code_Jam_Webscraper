#include <bits/stdc++.h>
#define debug(a, b) copy(a.begin(), a.end(), ostream_iterator<b> (cout, " ")); cout<<endl
#define debugm(m) for(const auto &i: m) cout<<i.first<<' '<<i.second<<endl;

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
int main(int argc, char const *argv[])
{
    int t=Read();
    for(int tt=1;tt<=t;tt++)
    {
        int ans=0;
        string s;
        cin>>s;
        int i=0;
        while(1)
        {
            i=s.find("-");
            if(i==string::npos)
                break;
            while(s[i]=='-' && i<s.length())
                i++;
            i--;
            ans++;
            for(;i>=0;i--)
                if(s[i]=='+')
                    s[i]='-';
                else
                    s[i]='+';
        }
        
        printf("Case #%d: %d\n", tt, ans);
    }
    return 0;
}