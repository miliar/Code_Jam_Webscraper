#include <iostream>
#include <cstdio>
using namespace std;
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int N;
    cin >> N;
    for (int i = 1; i<=N; i++)
    {
        string s;
        cin >> s;
        int k ;
        cin >> k;
        int t = 0;
        printf("Case #%d: ",i);
        for (int j = 0; j<s.length();)
        {
            while (j<s.length()&&s[j]=='+') j++;
            if (j==s.length())
            {
                cout << t <<endl;
                break;
            }
            if (j+k-1>=s.length())
            {
                 cout <<"IMPOSSIBLE"<<endl;
                 break;
            }
            t++;
            for (int dd = j; dd<=j+k-1; dd++)
            {
                if (s[dd]=='+') s[dd]='-';
                else s[dd] = '+';
            }
        }
    }

}
