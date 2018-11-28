#include <bits/stdc++.h>

using namespace std;

char winner(char a, char b)
{
    if((a=='R' && b=='P') || (a=='P'&&b=='R'))
    {
        return 'P';
    }
    else if((a=='P' && b=='S') || (a=='S' && b=='P'))
    {
        return 'S';
    }
    return 'R';
}

int main()
{
    freopen("inp.in", "r", stdin);
    freopen("outp.out", "w", stdout);
    int tc;
    scanf("%d", &tc);
    for(int kras=1; kras<=tc; kras++)
    {
        //ATTENTION! Check if the whitespace is needed or not before submitting!
        printf("Case #%d: ", kras);
        int n, r, p, s;
        scanf("%d %d %d %d", &n, &r, &p, &s);
        int total_players = (1LL<<n);

        string total="";
        for(int i=0; i<r; i++)
        {
            total += "R";
        }
        for(int j=0; j<p; j++)
        {
            total += "P";
        }
        for(int j=0; j<s; j++)
        {
            total += "S";
        }
        sort(total.begin(), total.end());
        bool found = false;
        do
        {
            bool valid = true;
            //do somethhing

            string now = total;
            for(int rounds=0; rounds<n; rounds++)
            {
                string volgend = "";
                for(int i=0; i+1<now.size(); i+=2)
                {
                    if(now[i] == now[i+1])
                    {
                        valid = false;
                        break;
                    }
                    volgend.push_back(winner(now[i], now[i+1]));
                }

                if(!valid)
                {
                    break;
                }
                now = volgend;
            }

            if(valid)
            {
                found = true;
                cout << total << endl;
                break;
            }
        }while(next_permutation(total.begin(), total.end()));
        if(!found)
        {
            cout << "IMPOSSIBLE" << endl;
        }
    }
    return 0;
}
