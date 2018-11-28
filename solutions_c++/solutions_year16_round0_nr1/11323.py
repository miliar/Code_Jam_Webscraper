/*************************************************************************
	> File Name: PA.cpp
	> Author: Gavin Lee
	> School: National Chiao Tung University
	> Team: NCTU_Ragnorok
	> Mail: sz110010@gmail.com
	> Created Time: 西元2016年04月09日 (週六) 19時53分11秒
 ************************************************************************/

#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    scanf("%d", &t);
    for(int i = 1; i <= t; ++i)
    {
        int n;
        scanf("%d", &n);
        if(n == 0)
        {
            printf("Case #%d: INSOMNIA\n", i);
            continue;
        }
        bool c[100] = {0};
        int ans = n;
        while(true)
        {
            bool che = false;
            stringstream ss;
            string str;
            ss << ans;
            ss >> str;
            int l = str.length();
            for(int j = 0; j < l; ++j)
                c[str[j]] = true;
            for(int j = '0'; j <= '9'; ++j)
            {
                if(c[j] == 0)
                {
                    ans += n;
                    che = true;
                    break;
                }
            }
            if(che)
                continue;
            printf("Case #%d: %d\n", i, ans);
            break;
        }
    }
    return 0;
}
