#include<iostream>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
#include<fstream>
#include<sstream>
using namespace std;

int M, N;
vector<string> S;
map<int, int> MAP;
int Max;
int HowMany(vector<string> v)
{
    set<string> Set;
    Set.insert("");
    for(int i = 0; i < v.size(); i++)
    {
        Set.insert(v[i]);
        for(int j = 0; j < v[i].size(); j++)
        {
            Set.insert(v[i].substr(0,j));
        }
    }
    if(Set.size() == 1) return -1000000;
    return Set.size();
}
void rec(string s)
{
    if(s.size() == M)
    {
        long long tot = 0;
        for(int i =0 ;i < N; i++)
        {
            char cur = (i + '0');
            vector<string> vec;
            for(int j =0; j < s.size(); j++)
            {
                if(s[j] == cur)
                    vec.push_back(S[j]);
            }
            tot += HowMany(vec);
            vec.clear();
        }
        MAP[tot] = ( MAP[tot] + 1) %  1000000007;
        if(tot > Max) 
            Max = tot;    
        if(Max == 7) 
            cout << s << endl;
    }
    else
    {
        for(int i = 0; i < N; i++)
        {
            rec(s + char(i + '0'));
        }
    }
}
int main()
{
    int T;
    ifstream in("in.txt");
    ofstream out("out.txt");
    in >> T; 
    for (int t = 1; t <= T; t++)
    {
        in >> M >> N;
        S.clear();
        Max = 0;
        MAP.clear();
        for(int i = 0; i < M; i++)
        {
            string s;
            in >> s;
            S.push_back(s);
        }
        rec("");
        out << "Case #" << t <<": " << Max <<" "<< MAP[Max] << endl;
    }
    return 0;
}
