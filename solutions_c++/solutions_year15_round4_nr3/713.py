#include <bits/stdc++.h>

typedef long long ll;
using namespace std;

void mod(ll &a, ll b)
{
    a %= b;
    if(a < 0) a += b;
}

#define all(x) x.begin(), x.end()
#define f(i,a,b) for(int i = (a); i <= (b); i++)
#define fd(i,a,b) for(int i = (a); i >= (b); i--)
#define mp make_pair
#define faster_io() ios_base::sync_with_stdio(false)
#define pb push_back
#define pii pair<int,int>
#define SZ(x) ((int)x.size())
#define vii vector<pair<int,int>>

const int INF = 1000000005;
const ll INFLL = 1000000000000000002ll;
const ll MOD = 1000000007;

// ----------------------------------------------------------------------------------------------------------

ifstream fin("C.txt");
ofstream fout("C.out");

int Ans, Ids, Lang[100005][2], Tests, N;
map<string,int> ID;
set<string> Words;
vector<int> Line[25];

void process(int i, int l)
{
    if(i == N)
    {
        int curr = 0;
        f(id,1,Ids) if(Lang[id][0] && Lang[id][1]) curr++;
        Ans = min(Ans, curr);
        return;
    }
    for(int id : Line[i]) Lang[id][l]++;
    if(i == 0) process(i+1,1);
    else
    {
        process(i+1,0);
        process(i+1,1);
    }
    for(int id : Line[i]) Lang[id][l]--;
}

int main()
{
    fin >> Tests;

    f(tt,1,Tests)
    {
        cout << tt << "\n";
        fin >> N;
        string trash;
        getline(fin,trash);
        Ids = 0;
        ID.clear();
        Words.clear();
        f(i,0,N-1)
        {
            Line[i].clear();

            string s;
            getline(fin,s);

            s += ' ';
            int pos = 0;

            while(true)
            {
                int nx = s.find(" ", pos);
                if(pos < 0 || pos >= SZ(s) - 1) break;
                string w = s.substr(pos,nx-pos);
                if(Words.find(w) == Words.end()) ID[w] = ++Ids;
                Words.insert(w);
                Line[i].pb(ID[w]);
                pos = nx+1;
            }
        }

        if(tt )

        Ans = 999999999;
        process(0,0);
        fout << "Case #" << tt << ": " << Ans << "\n";
    }
}
