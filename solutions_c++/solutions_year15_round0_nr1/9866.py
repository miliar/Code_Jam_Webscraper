#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("input.in","r", stdin);
    freopen("output.out","w", stdout);
    int cases ,x,claped,counter;
    cin >> cases ;
    string s ;
    for (int d=0;d<cases;d++)
    {
        claped=0 ;
        counter=0;
        cin >>x>> s ;
        for (int i=0;i<s.size();i++)
        {
            if (s[i]=='0')
            {
                continue;
            }
            if (i<=claped)
            {
                claped += (s[i]-'0');
            }
            else
            {
                counter += (i-claped);
                claped +=(s[i]-'0')+(i-claped);
            }
        }
        cout << "Case #"<<d+1<<": " << counter << endl;
    }
    return 0;
}
