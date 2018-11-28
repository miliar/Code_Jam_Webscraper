#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <map>
using namespace std;

vector<int> string_to_num_rep (string s)
{
    vector<char> chars(26);
    vector<string> words {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
    for(auto i=0;i<26;i++)
    {
        chars[i]=(char)('A'+i);
        //cout<<chars[i];
    }
    map<char,int> charmap;
    for(auto i=0;i<26;i++)
    {
        charmap[chars[i]]=0;
    }
    for(auto i=0;i<s.length();i++)
    {
        for(auto j=0;j<26;j++)
        {
            if (s[i]==chars[j])
            {
                charmap[chars[j]]+=1;
                break;
            }
        }
    }
    vector<int> ans(10);
    ans[0]=charmap['Z'];
    for(int i=0; i<words[0].length();i++)
    {
        charmap[(words[0])[i]]-=ans[0];
    }
    ans[6]=charmap['X'];
    for(int i=0; i<words[6].length();i++)
    {
        charmap[(words[6])[i]]-=ans[6];
    }
    ans[2]=charmap['W'];
    for(int i=0; i<words[2].length();i++)
    {
        charmap[(words[2])[i]]-=ans[2];
    }
    ans[8]=charmap['G'];
    for(int i=0; i<words[8].length();i++)
    {
        charmap[(words[8])[i]]-=ans[8];
    }
    ans[3]=charmap['H'];
    for(int i=0; i<words[3].length();i++)
    {
        charmap[(words[3])[i]]-=ans[3];
    }
    ans[4]=charmap['R'];
    for(int i=0; i<words[4].length();i++)
    {
        charmap[(words[4])[i]]-=ans[4];
    }
    ans[1]=charmap['O'];
    for(int i=0; i<words[1].length();i++)
    {
        charmap[(words[1])[i]]-=ans[1];
    }
    ans[5]=charmap['F'];
    for(int i=0; i<words[5].length();i++)
    {
        charmap[(words[5])[i]]-=ans[5];
    }
    ans[9]=charmap['I'];
    for(int i=0; i<words[9].length();i++)
    {
        charmap[(words[9])[i]]-=ans[9];
    }
    ans[7]=charmap['S'];
    for(int i=0; i<words[7].length();i++)
    {
        charmap[(words[7])[i]]-=ans[7];
    }
    return ans;
}


int main()
{
    ifstream in;
    ofstream out;
    in.open("in.in");
    out.open("out.txt");
    int T;
    string S;
    int t;
    in>>T;
    for(t=1;t<=T;t++)
    {
        in>>S;
        out<<"Case #"<<t<<": ";
        auto v=string_to_num_rep(S);
        for(int i=0;i<10;i++)
        {
            for(int j=0;j<v[i];j++)
                out<<i;
        }
        out<<endl;
    }
    in.close();
    out.close();
}
