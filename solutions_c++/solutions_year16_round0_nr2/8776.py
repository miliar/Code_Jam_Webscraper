/**** krishna keshav && peace && PES College of Engineering, mandya *******/

#include<iostream>
#include<vector>

#define ll unsigned long long

using namespace std;

bool checkPlus(string s)
{
    ll len = s.length();
    for(ll i = 0; i < len ; i++)
        if(s[i] != '+')
            return false;
    return true;
}

bool checkMinus(string s)
{
    ll len = s.length();
    for(ll i = 0; i < len ; i++)
    {
        if(s[i] != '-')
            return false;
    }
    return true;
}

string reverse(string s , ll pos)
{
    for(ll j = 0 ; j <= pos ; j++)
    {
        char temp = s[j];
        s[j] = s[pos - j];
        s[pos - j] = temp;
    }
    return s;
}

int main()
{
    ll t;
    cin >> t;
    ll test = t;
    while(t--)
    {
        ll flips = 0 , counter = 0;
        string S;
        cin >> S;//cout << S;
        while(1)
        {
            if(checkMinus(S))
            {
                flips++;//cout << "ho";
                break;
                //S = reverse(S , counter);
            }
            if(checkPlus(S))
            {
                //cout << "lo";
                break;
            }
            for(ll i = counter ; i < S.length() - 1; i++)
            {
                if((S[i] == '+' && S[i + 1] == '-') || (S[i] == '-' && S[i + 1] == '+'))
                {
                    counter = i;
                    //cout << "cho";
                    S = reverse(S , i);//cout << S;
                    for(ll k = 0 ; k <= i ; k++)
                    {
                        if(S[k] == '-') S[k] = '+';
                        else S[k] = '-';
                    }//cout << S;
                    flips++;
                    break;
                }
                //cout << "cho1";
            }
            counter++;//cout << "cho1";
        }
        cout << "Case #" << test - t << ": " << flips << endl;
    }
    return 0;
}
