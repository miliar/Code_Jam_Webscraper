#include <iostream>
#include <cstring>
#include <cctype>
#include <cmath>
#include <math.h>
#include <algorithm>
#include <vector>
#include <sstream>
#include <cstdio>


using namespace std;


struct srt {
    bool operator()(const std::pair<int,int> &left, const std::pair<int,int> &right) {
        return left.first > right.first;
    }
};


int main()
{
    freopen("A-large.in","r",stdin);
    freopen("inp.out","w",stdout);

    int n;
    cin >> n;
    //cout << 1 << endl;
    for (int i=0;i<n;i++)
    {

        vector<pair<int,char > > a;
        int num;
        cin >> num;
        //cout << 2 << endl;
        for (int j=0;j<num;j++)
        {
            int x;
            cin >> x;
            a.push_back(make_pair(x,'A'+j));
        }
        a.push_back(make_pair(0,'A'+num));

        cout << "Case #" << i+1 << ":";
        sort(a.begin(),a.end(),srt());
        while (a[0].first!=0)
        {

            if (a[0].first-a[1].first>=2)
            {
                cout << " " << a[0].second << a[0].second;
                a[0].first-=2;
            }
            else if (a[1].first==0)
            {
                cout << " " << a[0].second;
                a[0].first-=1;
            }
            else if (a[1].first==1 && a[2].first==1 && a[0].first==1)
            {
                cout << " " <<a[0].second;
                a[0].first--;
            }
            else
            {
                cout << " " << a[0].second << a[1].second;
                a[0].first-=1;
                a[1].first-=1;
            }
            sort(a.begin(),a.end(),srt());
        }
        cout << endl;




    }
}
