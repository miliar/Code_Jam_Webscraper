#include<fstream>
#include<iostream>
#include<cstring>
#include<algorithm>
#include<string>
#include<vector>
#include<set>
#include<unordered_map>
#define ll long long
using namespace std;

int T,cnt,sol,x,N,offset;
string S[100],str;
vector<string> sentence[100];
unordered_map<string,int> words,both, english, french;

int main()
{
    freopen("file.in","r",stdin);
    freopen("file.out","w",stdout);
    scanf("%d\n",&T);
    for(int t = 1; t <= T; t++)
    {
        scanf("%d\n",&N);
        sol = 100000000;
        offset = 0;
        words.clear();
        for(int i=0;i<N;i++)
        {
            getline(cin, S[i]);
            sentence[i].clear();
            str.clear();
            for(int j = 0; j < S[i].size(); j++)
            {
                if(S[i][j] >= 'a' && S[i][j] <= 'z')
                {
                    str.push_back(S[i][j]);
                }
                else
                {
                    if(str.size())
                    {
                        sentence[i].push_back(str);
                        if(i > 1)
                        {
                            if(words.find(str) == words.end())
                                words.insert(make_pair(str, 0));
                            else
                                words[str] = 0;
                        }
                    }
                    str.clear();
                }
            }
            if(str.size())
            {
                sentence[i].push_back(str);
                if(i > 1)
                {
                    if(words.find(str) == words.end())
                        words.insert(make_pair(str, 0));
                    else
                        words[str] = 0;
                }
            }
            str.clear();
        }
        both.clear();
        for(int i = 0; i < sentence[0].size(); i++)
            for(int j = 0; j < sentence[1].size(); j++)
            {
                if(sentence[0][i] == sentence[1][j])
                {
                    if(both.find(sentence[0][i]) == both.end())
                    {
                        both.insert(make_pair(sentence[0][i], 0));
                        offset++;
                    }
                }
            }
        english.clear();
        french.clear();
        for(int i = 0; i < sentence[0].size(); i++)
        {
            if(english.find(sentence[0][i]) == english.end())
                english.insert(make_pair(sentence[0][i], 0));
        }
        for(int i = 0; i < sentence[1].size(); i++)
        {
            if(french.find(sentence[1][i]) == french.end())
                french.insert(make_pair(sentence[1][i], 0));
        }
        N = N - 2;
        for(int state = 0; state < (1<<N); state++)
        {
            for(unordered_map<string,int>::iterator it = words.begin();it!=words.end();it++)
                it->second = 0;
            cnt = 0;
            for(int i = 2; i < N+2; i++)
            {
                if(i < 2)
                    x = i + 1;
                else
                    x = ((state & (1<<(i-2)))>0) + 1;
                for(vector<string>::iterator it = sentence[i].begin();it!=sentence[i].end();it++)
                {
                    words[*it] |= x;
                }
            }
            for(unordered_map<string,int>::iterator it = words.begin();it!=words.end();it++)
            {
                if(it->second == 3 && both.find(it->first) == both.end())
                    cnt = cnt + 1;
                if(it->second == 1 && french.find(it->first) != french.end() && both.find(it->first) == both.end())
                    cnt = cnt + 1;
                if(it->second == 2 && english.find(it->first) != english.end() && both.find(it->first) == both.end())
                    cnt = cnt + 1;
            }
            sol = min(sol, cnt);
        }
        cout<<"Case #"<<t<<": "<<sol+offset<<"\n";
    }
    return 0;
}
