#include <bits/stdc++.h>
using namespace std;
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin >> t;
    for(int test=1;test<=t;test++)
    {
        string s;
        cin >> s;
        int n=s.length();
        deque<char> last_word;
        last_word.push_back(s[0]);
        for(int i=1;i<n;i++)
        {
            char c=s[i];
            if(c>=last_word.front()) last_word.push_front(c);
            else last_word.push_back(c);
        }
        cout << "Case #" << test << ": ";
        for(int i=0;i<n;i++) printf("%c",last_word[i]);
        printf("\n");
    }
}
