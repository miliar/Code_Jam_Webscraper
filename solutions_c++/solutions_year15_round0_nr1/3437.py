//Rejection is a part of any man’s life.
//If you can’t accept and move past rejection, or at least use it as writing material - you’re not a real man
#include <bits/stdc++.h>

using namespace std;

int main()
{
    cin.sync_with_stdio(false);
    freopen("A-large.in", "r", stdin);
    freopen("outputl.txt", "w", stdout);
    int test;
    cin>>test;
    int counter = 0;
    while(test--)
    {
        counter++;
        long long int x,answer,curr;
        string s;
        answer = curr =  0;
        cin>>x>>s;
        for(int i = 0; i < s.size(); i++)
        {
            if(curr < i) {
                answer = answer + (i-curr);
                curr= curr + ( i - curr);
            }
            curr = curr + (s[i] - '0');
        }

        cout<<"Case #"<<counter<<":"<<" "<<answer<<endl;

    }
    return 0;
}

