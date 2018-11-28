#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t;
    cin >> t;
    int n, J;
    cin >> n >> J;
    ofstream fout("res.txt");
    fout << "Case #1:" << endl;
    int stepen = 1;
    int cnt = 0;
    vector<int> v;

    while(cnt < J)
    {

        for(int i=0; i<(1 << (stepen-1)); i++) // reshenie
        {
            v.clear();
            v.push_back(1);
            for(int j = 0; j < stepen - 1; j++)
            {
                if( (i & (1 << j)) == 0)
                    v.push_back(0);
                else
                    v.push_back(1);
            }
            v.push_back(1);
//            cout << stepen << " ";
//            for(int j = 0; j < v.size(); j++)
//                cout << v[j] << " ";
//            cout << endl;
            string s = "";
            for(int j=0; j<n; j++)
                s+="0";
            for(int j = 0; j < v.size(); j++)
            {
                if(v[j] == 1)
                {
                    s[j] = '1';
                    s[n-1-stepen+j] = '1';
                }
            }
            cout << s << " ";
            fout << s << " ";
            reverse(v.begin(), v.end());
            for(int x = 2; x <= 10; x++)
            {
                long long res = 0;
                long long st = 1;

                for(int k = 0; k < v.size(); k++)
                {
                    res += st * v[k];
                    st *= x;
                }
                fout << res << " ";
                cout << res << " ";
            }
            fout << endl;
            cout << endl;

            cnt ++;
            if(cnt == J)
                break;
        }
        stepen ++;


    }

    return 0;
}
