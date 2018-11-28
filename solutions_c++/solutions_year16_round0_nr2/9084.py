#include<bits/stdc++.h>

using namespace std;

int main()
{
    int t;
    string s;
    char tab[101];
    scanf("%d",&t);
    for(int i=1; i<=t; i++)
    {
        cin >> s;
        int wyn=1;
        for(int a=1; a<s.size(); a++)
        {
            if(s[a]!=s[a-1])
                wyn++;
        }
        if(s[s.size()-1]=='+')
            wyn--;
        cout << "Case #" << i << ": " << wyn << endl;
    }
}
