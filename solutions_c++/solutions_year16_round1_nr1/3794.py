#include <iostream>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <map>
using namespace std;
 
int main()
{
    int t,i,d,in,j;
    std::ios::sync_with_stdio(false);
    cin >> t;
    for (in = 1; in <= t; ++in) 
    {
        char s[1010],ans[1010],c,tmp;
        cin >> s;
        for (i = 0; i <= strlen(s); ++i) ans[i]=s[i];
        for (i = 1; i < strlen(s); ++i)
        {
            if(s[i]>=ans[0])
            {
                //cout << s[i] << endl;
                c=ans[0];
                for (j = 1; j <= i; ++j)
                {
                    tmp=ans[j];
                    ans[j]=c;
                    c=tmp;
                }
                ans[0]=s[i];
            }
        }
        ans[i]='\0';
        cout << "Case #" << in << ": " << ans << endl;
    }
    return 0;
}