#include <string>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


string solve()
{
    int N, R, P, S;
    cin>>N>>R>>P>>S;

    string ans = "";

    for (char e: "RPS")
    {
        string a(1, e);

        for (int i=0;i <N; i++)
        {
            string b = a;
            a = "";

            for (int j=0; j<(int)b.size(); j++)
            switch (b[j])
            {
            case 'R': a += "RS"; break;
            case 'P': a += "PR"; break;
            case 'S': a += "SP"; break;
            }
        }

        if (count(a.begin(), a.end(), 'R')==R &&
            count(a.begin(), a.end(), 'P')==P)
        {
            for (int i=0; i<N; i++)
            {
                for (int j=0; j<(int)a.size(); j+=(1<<i)*2)
                {
                    if (a.substr(j, 1<<i) > a.substr(j+(1<<i), 1<<i))
                    {
                        for (int k=0; k<(1<<i); k++)
                            swap(a[j+k], a[j+(1<<i)+k]);
                    }
                }
            }
            if (ans=="")
                ans = a;
            else
                ans = min(ans, a);
        }
    }

    if (ans=="")
        return "IMPOSSIBLE";
    else
        return ans;
}

int main()
{
    int T;
    cin>>T;
    for (int i=1; i<=T; i++)
        cout<<"Case #"<<i<<": "<<solve()<<endl;
}
