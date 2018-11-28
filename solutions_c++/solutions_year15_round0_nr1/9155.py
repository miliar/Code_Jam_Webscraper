#include <iostream>
#include <string>
#include <cstdio>

using namespace std;

int chiffre(char c)
{
    if(c == '0')
    {
        return 0;
    }
    else if(c == '1')
    {
        return 1;
    }
    else if(c == '2')
    {
        return 2;
    }
    else if(c == '3')
    {
        return 3;
    }
    else if(c == '4')
    {
        return 4;
    }
    else if(c == '5')
    {
        return 5;
    }
    else if(c == '6')
    {
        return 6;
    }
    else if(c == '7')
    {
        return 7;
    }
    else if(c == '8')
    {
        return 8;
    }
    else
    {
        return 9;
    }
    return -1000000;
}

int main()
{
    string ch;
    int need,disp,n,temp;
    int t,t_max;

    freopen("A-large.in","rt",stdin);
    freopen("outL.out","wt",stdout);

    cin >> t;
    t_max = t;
    while(t--)
    {
        cin >> temp;
        cin >> ch;
        need = 0;
        disp = 0;
        for(unsigned int i(0);i<ch.length();i++)
        {
            n = chiffre(ch[i]);
            if((n == 0) && (disp < i+1))
            {
                need++;
                disp++;
            }

            disp += n;
        }

        cout << "Case #" << t_max - t << ": " << need << endl;
    }
    return 0;
}
