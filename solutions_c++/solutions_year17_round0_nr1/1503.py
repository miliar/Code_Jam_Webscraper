#include<cstdio>
#include<iostream>
#include<cstring>
using namespace std;
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    string str;
    int n, k;
    cin >> n;
    for(int i=1; i<=n; i++)
    {
        cin >> str >> k;
        int count = 0;
        for(int j=0; j+k<=str.size(); j++)
        {
            if(str[j]=='+') continue;
            for(int a=0; a<k; a++)
            {
                if(str[j+a]=='+')
                    str[j+a]='-';
                else str[j+a]='+';
            }
            count ++;
        }
        bool isPossible = true;
        for(int j=str.size()-k; j<str.size(); j++)
            if(str[j]=='-'){
                isPossible = false;
                break;
            }
        if(isPossible)
            cout << "Case #" << i << ": " << count << endl;
        else
            cout << "Case #" << i << ": IMPOSSIBLE" << endl;
    }
    return 0;
}
