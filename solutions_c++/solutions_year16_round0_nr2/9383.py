#include <bits/stdc++.h>
using namespace std;


int main()
{
    int n; cin >> n;
    for(int EVENJETFUELCANTMELTGOOGLESMEMES = 1; EVENJETFUELCANTMELTGOOGLESMEMES <=n; EVENJETFUELCANTMELTGOOGLESMEMES++)
    {
        string pancakes;
        cin >> pancakes;
        int cur=0;
        bool flipped = false;
        for(int i = pancakes.length()-1; i >= 0; i--)
        {
            if(pancakes[i]=='+'&&!flipped)
                continue;
            else if(pancakes[i]=='-'&&flipped)
                continue;
            else
            {
                flipped=!flipped;
                cur++;
            }
        }
        printf("Case #%d: %d\n",EVENJETFUELCANTMELTGOOGLESMEMES,cur);
    }
}
