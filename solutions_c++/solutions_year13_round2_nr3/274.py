#include <iostream> 
#include <vector> 
#include <queue> 
#include <string> 
#include <cctype> 
#include <cmath> 
#include <list> 
#include <iomanip> 
#include <sstream> 
#include <algorithm> 
#include <map> 
#include <set> 
#include <fstream>
using namespace std;

const int INF = 1000000000;
const int MIN_DIFF = 5;

const int W = 521196;
string words[W];

string inp;

int DP[64][64];
int len;

vector< pair<string, int> > preWords[64];
vector< pair<int, int> > prePosi[64];

void loadDict()
{
    ifstream fin("dict.txt"); 
    for (int i = 0; i < W; i++)
        fin >> words[i];
    
    fin.close();
}

int rec(int pos, int lastChangedPos)
{
    if (pos == len) return 0;
    
    int& ans = DP[pos][lastChangedPos];
    if (ans != -1) return ans;
    
    ans = INF;
    
    for (int i = 0; i < preWords[pos].size(); i++)
    {
        string word = preWords[pos][i].first;
        int wordLen = word.size();
        
        if (pos + wordLen > len) continue;
        
        int firstPos = prePosi[pos][i].first;
        if (firstPos != -1 && lastChangedPos != 63 && 
            firstPos - lastChangedPos < MIN_DIFF) 
           continue;
        
        int prevPos = prePosi[pos][i].second;
        if (prevPos == -1) prevPos = lastChangedPos;    
        
        int changes = preWords[pos][i].second;
        ans = min(ans, rec(pos + wordLen, prevPos) + changes);       
    } 
    
    return ans;
}

void precompute()
{
    for (int i = 0; i < len; i++)
    {
        preWords[i].clear();
        prePosi[i].clear();
        
        for (int j = 0; j < W; j++)
        {
            string word = words[j];
            int wordLen = word.size();
            
            if (i + wordLen > len) continue;
            
            int changes = 0;
            bool can = true;
            
            int firstDiff = -1;
            int lastDiff = -1;
            
            for (int k = 0; k < wordLen; k++)
            {
                if (word[k] != inp[i + k])
                {
                    if (lastDiff != -1 && (i + k) - lastDiff < MIN_DIFF)
                    {
                        can = false;
                        break;         
                    }
                            
                    changes++;  
                    
                    if (firstDiff == -1) firstDiff = i + k;
                    lastDiff = i + k;      
                }
            }
            
            if (can) 
            {
                preWords[i].push_back(make_pair(word, changes));               
                prePosi[i].push_back(make_pair(firstDiff, lastDiff));
            }
        }
    }
}

int solve()
{
    memset(DP, -1, sizeof(DP));
    len = inp.size();
    
    precompute();
    
    return rec(0, 63);
}

int main()
{
    loadDict();
    
    int T; cin >> T;
    
    for (int t = 1; t <= T; t++)
    {
        cin >> inp;
        printf("Case #%d: %d\n", t, solve());
    }
    
    return 0;
}
