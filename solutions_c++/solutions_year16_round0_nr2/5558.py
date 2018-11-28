#include<bits/stdc++.h>
using namespace std;
int last_sad(int len, int hp[])
{
    for (int i=len-1;i>=0;i--)
        if (hp[i] == false) return i;
    return -1;
}

int main()
{
    int T;
    scanf ("%d",&T);
    for (int c=1;c<=T;c++)
    {
        string input;
        cin >> input;
        int len = input.length();
        int hp[len],ans=0;
        for (int i=0;i<len;i++)
        {
            if (input.at(i) == '+')
                hp[i] = true;
            else
                hp[i] = false;
        }
        while (last_sad(len,hp) != -1)
        {
            for (int i=0;i<=last_sad(len,hp);i++)
                hp[i] = !hp[i];
            ans++;
        }
        cout << "Case #" << c << ": " << ans << endl;

    }
}
