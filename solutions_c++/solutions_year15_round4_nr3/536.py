#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <set>
#include <algorithm>

using namespace std;

template <class T>ostream &operator<<(ostream &o,const vector<T>&v)
{o<<"{";for(int i=0;i<(int)v.size();i++)o<<(i>0?", ":"")<<v[i];o<<"}";return o;}

int main()
{
    int T;
    cin>>T;
    for (int t=1; t<=T; t++)
    {
        int N;
        cin>>N;
        string tmp;
        getline(cin, tmp);
        vector<vector<string>> S(N);
        set<string> D;

        for (int i=0; i<N; i++)
        {
            string s;
            getline(cin, s);
            stringstream ss(s);
            string a;
            while (ss>>a)
            {
                S[i].push_back(a);
                D.insert(a);
            }
        }

        vector<vector<int>> A;
        int base = 0;

        for (string s: D)
        {
            vector<int> T;
            for (int i=0; i<N; i++)
                for (string a: S[i])
                    if (a==s)
                    {
                        T.push_back(i);
                        break;
                    }
            if (T.size()>=2 && T[0]==0 && T[1]==1)
            {
                base++;
            }
            else if (T.back() >= 2)
                A.push_back(T);
        }

        int ans = 99999999;

        for (int b=0; b<(1<<N); b++)
        if ((b&3)==1)
        {
            int c = 0;
            for (vector<int> &a: A)
            {
                int f = 0;
                for (int x: a)
                    f |= 1<<(b>>x&1);
                if (f==3)
                    c++;
            }
            ans = min(ans, c+base);
        }

        cout << "Case #" << t << ": " << ans << endl;
    }
}
    
