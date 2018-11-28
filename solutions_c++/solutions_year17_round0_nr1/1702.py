#include <iostream>

using namespace std;

int main()
{
    freopen("a","r",stdin);
    freopen("b","w",stdout);
    int t;
    cin >> t;
    for (int c34=1;c34<=t;c34++)
    {
        cout << "Case #" << c34 << ": ";
        string s;
        cin >> s;
        int k;
        cin >> k;
        int res=0;
        for (int i=0;i<s.length()-k+1;i++)
        {
            if (s[i]=='-')
            {
                res++;
                for (int j=i;j<i+k;j++)
                {
                    s[j]='+'+'-'-s[j];
                }
            }
        }
        for (int i=0;i<s.length();i++)
        {
            if (s[i]=='-'){res=-1;break;}
        }
        if (res==-1){cout << "IMPOSSIBLE" << endl;}else{cout << res << endl;}
    }
    return 0;
}
