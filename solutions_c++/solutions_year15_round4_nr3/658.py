#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
#include <vector>
using namespace std;
int word[1500];
int oldword[1500];

map<string,int>mp;
int cnt;
int tt,n;
vector<string> a[30];
int aa[30][12];
const int EN = 1;
const int FR = 2;
vector<string> ddd(string str)
{
    string tgt = " ";
    char tmp[20];
    vector<string> res;
    res.clear();
    while(str.find(tgt) != str.npos)
    {
        int pos = str.find(tgt);
        memset(tmp,0,sizeof tmp);
        str.copy(tmp,pos,0);
        string s = string(tmp);
        res.push_back(s);
        str.erase(0,pos+1);
    }
    res.push_back(str);
//    for (int i = 0; i < res.size(); i++)
//    cout<<res[i]<<endl;
    return res;
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>tt;
    getchar();
    for (int ii = 1; ii <= tt; ii++)
    {
        cin>>n;
        string s;
        getchar();
        vector<string> en,fr;
        en.clear();
        fr.clear();
        getline(cin,s);
        en = ddd(s);
        getline(cin,s);
        fr = ddd(s);

        cnt = 0;
        mp.clear();
        memset(word,0,sizeof word);
        memset(oldword,0,sizeof oldword);
        int id;
        for (int i = 0; i < en.size(); i++)
        {
            if (mp.find(en[i]) == mp.end())
            {
                mp[en[i]] = ++cnt;
                id = cnt;
            }
            else
            {
                id = mp[en[i]];
            }
            word[id] |= EN;
        }

        for (int i = 0; i < fr.size(); i++)
        {
            if (mp.find(fr[i]) == mp.end())
            {
                mp[fr[i]] = ++cnt;
                id = cnt;
            }
            else
            {
                id = mp[fr[i]];
            }
            word[id] |= FR;
        }

        for (int i = 0; i <= cnt; i++) oldword[i] = word[i];

        for (int i = 0; i <= 22; i++) a[i].clear();
        for (int i = 0; i < n-2; i++)
        {
            getline(cin,s);
            a[i] = ddd(s);
            for (int j = 0; j < a[i].size(); j++)
            {
                if (mp.find(a[i][j]) == mp.end())
                {
                    mp[a[i][j]] = ++cnt;
                }
            }
        }
        for (int i = 0; i < n-2; i++)
        {
            for (int j = 0; j < a[i].size(); j++)
            {
                id = mp[a[i][j]];
                aa[i][j] = id;
            }
        }
        int tot = n-2;
        int ans = 99999999;
        //cout << cnt << endl;
        for (int sta = 0; sta < (1<<tot); sta++)
        {

            memcpy(word,oldword,sizeof word);
            for (int i = 0; i < tot; i++)
            {
                int lang;
                if ((1<<i)&sta)
                {
                    lang = EN;
                }
                else
                {
                    lang = FR;
                }

                for (int j = 0; j < a[i].size(); j++)
                {

                    id = aa[i][j];
                    word[id] |= lang;
                }
            }
            int sum = 0;
            for (int i = 1; i <= cnt; i++)
            {
                if (word[i] == 3) sum++;
            }
            ans = min(sum,ans);

        }
        printf("Case #%d: %d\n",ii,ans);

    }
    return 0;
}
