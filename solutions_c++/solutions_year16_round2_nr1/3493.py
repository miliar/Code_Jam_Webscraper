#include <stdio.h>
#include <string>
#include <string.h>
#include <iostream>

using namespace std;

void sub(char *ch, const string& str, int times)
{
    for(int i = 0; i < str.length(); i++)
        ch[str[i]-'A'] -= times;
}

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("aout.txt","w",stdout);

    int T;
    scanf("%d",&T);

    for(int cases = 1; cases <= T; cases++)
    {
        string inp;
        cin >> inp;

        int digit[10];
        char ch[27];

        memset(digit,0,sizeof(digit));
        memset(ch,0,sizeof(ch));

        for(int i = 0; i < inp.length(); i++)
            ch[ inp[i]-'A' ]++;

        digit[0] = ch['Z'-'A'];
        sub(ch,string("ZERO"),digit[0]);

        digit[2] = ch['W'-'A'];
        sub(ch,string("TWO"),digit[2]);

        digit[4] = ch['U'-'A'];
        sub(ch,string("FOUR"),digit[4]);

        digit[1] = ch['O'-'A'];
        sub(ch,string("ONE"),digit[1]);

        digit[3] = ch['R'-'A'];
        sub(ch,string("THREE"),digit[3]);

        digit[5] = ch['F'-'A'];
        sub(ch,string("FIVE"),digit[5]);

        digit[6] = ch['X'-'A'];
        sub(ch,string("SIX"),digit[6]);

        digit[7] = ch['S'-'A'];
        sub(ch,string("SEVEN"),digit[7]);

        digit[8] = ch['G'-'A'];
        sub(ch,string("EIGHT"),digit[8]);

        digit[9] = ch['I'-'A'];
        sub(ch,string("NINE"),digit[9]);

        cout << "Case #" << cases << ": ";
        for(int i = 0; i < 10; i++)
            for(int j = 0; j < digit[i]; j++)
                cout << i;
        cout << endl;
    }

    return 0;
}
