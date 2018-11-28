#include <iostream>
#include <string>
#include <vector>
#include <map>
using namespace std;

string getCode(int i)
{
    map<int, string> code;
    code[0] = "ZERO";
    code[1] = "ONE";
    code[2] = "TWO";
    code[3] = "THREE";
    code[4] = "FOUR";
    code[5] = "FIVE";
    code[6] = "SIX";
    code[7] = "SEVEN";
    code[8] = "EIGHT";
    code[9] = "NINE";
    return code[i];
}

void reduce(map<char, int> &m, string c)
{
    for(int i=0;i<c.size();i++)
        m[c[i]]--;
}
bool isGood(map<char, int> &m, int n)
{
    map<char, int> lm = m;
    string c = getCode(n);
    for(int i=0;i<c.size();i++)
    {
        if(!lm[c[i]]--)
            return false;
    }

    reduce(m, c);

    return true;
}

void checkSpecial(map<char, int> &m, vector<int> &v)
{
    while(m['Z'])
    {
        v.push_back(0);
        reduce(m, getCode(0));
    }

    while(m['W'])
    {
        v.push_back(2);
        reduce(m, getCode(2));
    }

    while(m['X'])
    {
        v.push_back(6);
        reduce(m, getCode(6));
    }

    while(m['G'])
    {
        v.push_back(8);
        reduce(m, getCode(8));
    }

    while(m['U'])
    {
        v.push_back(4);
        reduce(m, getCode(4));
    }
}

string solution(string s)
{
    map<char, int> m;
    for(int i=0;i<s.size();i++)
    {
        m[s[i]]++;
    }
    vector<int> v;
    checkSpecial(m, v);
    for(int i=0;i<10;i++)
    {
        while(isGood(m, i))
        {
            v.push_back(i);
        }
   }
   sort(v.begin(), v.end());
   string r = "";
   for(int i=0;i<v.size();i++)
   {
       r+= '0' + v[i];
   }
   return r;
}

int main() 
{
    int T;
    cin>>T;
    for(int t=0;t<T;t++)
    {
        string s;
        cin>>s;
        cout<<"Case #"<<t+1<<": "<<solution(s)<<endl;
    }
    return 0;
}
