#include<iostream>
#include<vector>
#include<algorithm>
#include<cstdio>
using namespace std;
int main()
{

    int n, tc;
    cin>>tc;
    for(int t=1; t<=tc; t++)
    {
        vector<double>a1, a2, a3, a4;
        int counterDec = 0;
        int counterWar = 0;
        double temp;
        cin>>n;

        for(int i=0; i<n ; i++)
        {
            cin>>temp;
            a1.push_back(temp);

        }
        for(int i=0; i<n ; i++)
        {
            cin>>temp;
            a2.push_back(temp);

        }
        sort(a1.rbegin(), a1.rend());
        sort(a2.rbegin(), a2.rend());
        a3 = a1;
        a4 = a2;
        while(!a1.empty())
        {
            if(*a1.begin()>*a2.begin())
            {
                counterWar++;
                a1.erase(a1.begin());
                a2.pop_back();
            }
            else
            {
                a1.erase(a1.begin());
                a2.erase(a2.begin());
            }
        }
        a1 = a4;
        a2 = a3;
        while(!a1.empty())
        {
            if(*a1.begin()>*a2.begin())
            {
                counterDec++;
                a1.erase(a1.begin());
                a2.pop_back();
            }
            else
            {
                a1.erase(a1.begin());
                a2.erase(a2.begin());
            }
        }
        cout<<"Case #"<<t<<": "<<(n-counterDec)<<" "<<counterWar<<endl;
    }

}
