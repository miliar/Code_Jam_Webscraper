#include <bits/stdc++.h>
//#define DEBUG
using namespace std;
typedef long long ll;

int main()
{
    string table[4][4] = {
                        {"1","i","j","k"},
                        {"i","-1","k","-j"},
                        {"j","-k","-1","i"},
                        {"k","j","-i","-1"},
    };
    map<char,int> mp;
    mp['1'] = 0;
    mp['i'] = 1;
    mp['j'] = 2;
    mp['k'] = 3;

    #ifndef DEBUG

    ifstream in("qc_s.in");
    cin.rdbuf(in.rdbuf());
    ofstream out("qc_s.out");
    cout.rdbuf(out.rdbuf());

    #endif
    int T;
    cin>>T;
    for(int A = 1;A <= T; A++)
    {
        ll L,X;
        cin>>L>>X;
        string s;
        cin>>s;
        bool valid = false;
        int iend = -1, kstrt = L*X;

        int sign = 1;
        int curr = 0;
        for(int i = 0; i < L*X; i++)
        {
            int val = mp[s[i%L]];
            string tmp = table[curr][val];
            if(tmp[0] == '-')
            {
                sign = -sign;
                curr = mp[tmp[1]];
            }
            else    curr = mp[tmp[0]];
            //cout<<"Tmp :"<<tmp<<endl;
            if(sign == 1 && curr == 1)
            {
                iend = i;
                break;
            }

        }
        //cout<<endl;
        sign = 1;
        curr = 0;
        for(int i = L*X-1; i > iend; i--)
        {
            int val = mp[s[i%L]];
            string tmp = table[val][curr];
            if(tmp[0] == '-')
            {
                sign = -sign;
                curr = mp[tmp[1]];
            }
            else    curr = mp[tmp[0]];
            //cout<<"Tmp :"<<tmp<<endl;
            if(sign == 1 && curr == 3)
            {
                kstrt = i;
                break;
            }


        }
        //cout<<endl;
        if(iend > -1 && kstrt < L*X)
        {
            sign = 1;
            curr = 0;
            for(int i = iend+1; i < kstrt; i++)
            {
                int val = mp[s[i%L]];
                string tmp = table[curr][val];
                if(tmp[0] == '-')
                {
                    sign = -sign;
                    curr = mp[tmp[1]];
                }
                else    curr = mp[tmp[0]];
                //cout<<"Tmp :"<<tmp<<endl;
            }
            if(sign == 1 && curr == 2)
                valid = true;
        }

     if(valid)
        cout<<"Case #"<<A<<": "<<"YES"<<endl;
    else
        cout<<"Case #"<<A<<": "<<"NO"<<endl;
    }


    return 0;
}
