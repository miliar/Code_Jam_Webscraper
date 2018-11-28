//
// Created by Michal Stobierski on 2016-04-16.
//

#include<iostream>
#include<deque>
using namespace std;

deque<char> D;

int main()
{
    ios_base::sync_with_stdio(0);
    int T;
    cin >> T;
    for(int asd=1; asd<=T; ++asd)
    {

        string S, res="";
        cin >> S;
        D.push_back(S[0]);
        for(int i=1; i<S.size(); ++i)
        {
            if(S[i]>=D.front())
            {
                D.push_front(S[i]);
            }
            else D.push_back(S[i]);
        }
        while(!D.empty())
        {
            res+=D.front();
            D.pop_front();
        }
        cout << "Case #" << asd << ": " << res << endl;
    }
    return 0;
}