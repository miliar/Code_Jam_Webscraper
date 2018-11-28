#include<iostream>
#include<bits/stdc++.h>
#include<map>
#include<string>
#include<sstream>

using namespace std;

int main()
{
    freopen("in.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        long long n;
        cin>>n;
        cout << "Case #" << i << ": ";
        if(n == 0)
        {
            cout << "INSOMNIA" << endl;
            continue;
        }
        map<int, bool> d;
        long long number = n;
        while(true)
        {
            stringstream ss;
            ss << number;
            string str = ss.str();
            for(char dig : str)
            {
                d[dig-'0'] = true;
            }
            if(d.size() == 10)
            {
                cout << number << endl;
                break;
            }
            number += n;
        }
    }
    return 0;
}
