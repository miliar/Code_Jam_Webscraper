#include<bits/stdc++>
using namespace std;
int bitmask;
int menor[100000];
int main()
{
    int T;
    for(int l = 1; l <= T; l++)
    {
        string s;
        scanf("%d", &s);
        int bitmask = 0;
        memset(menor, 0, sizeof(memset));

        int t = s.size();
        for(int i = 0; i < n; i++)
            if(s[i] == '+')
                bitmask += 1 << i;

    }
}
