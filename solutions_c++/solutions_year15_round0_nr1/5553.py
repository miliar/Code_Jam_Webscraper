#include <iostream>

using namespace std;

int main()
{
    int n,Si,r=0,levantados=0;
    char s[1001];
    cin >> n;
    for(int i=0;i<n;i++)
    {
        cin >> Si >> s;
        levantados=s[0]-'0';
        for(int a=1;a<=Si;a++)
        {
                if(a>levantados && s[a]!='0')
                {
                    r=r+(a-levantados);
                    levantados+=(a-levantados);
                }
                levantados+=(s[a]-'0');
        }
        cout << "Case #"<< i+1 << ": " << r << endl;
        r=0;

    }
    return 0;
}
