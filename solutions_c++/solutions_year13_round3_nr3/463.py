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

const int MAXN = 1024;

int firstDay[MAXN];
int numAttacks[MAXN];
int west[MAXN];
int east[MAXN];
int strength[MAXN];
int deltaDays[MAXN];
int deltaTravel[MAXN];
int deltaStrength[MAXN];

int N;
map<double, int> wall;

struct attack {
    int day;
    int W;
    int E;
    int S;
    
    attack(int day, int W, int E, int S) : day(day), W(W), E(E), S(S) {}
    
    bool operator < (const attack& o) const
    {
        return day < o.day; 
    }
};

int solve()
{
    wall.clear();
    
    int ans = 0;
    
    vector<attack> attacks;
    for (int i = 0; i < N; i++)
    {   
        int curDay = firstDay[i];     
        int W = west[i];
        int E = east[i];
        int S = strength[i];
        for (int j = 0; j < numAttacks[i]; j++)
        {
            attacks.push_back(attack(curDay, W, E, S));
            
            curDay += deltaDays[i];
            W += deltaTravel[i];
            E += deltaTravel[i];
            S += deltaStrength[i];
        }   
    }
    
    sort(attacks.begin(), attacks.end());
    
    int prevDay = 0;
    
    map<double, int> nextWall = wall;
    for (int i = 0; i < attacks.size(); i++)
    {
        attack att = attacks[i];
        int curDay = att.day;
        
        bool newDay = (curDay != prevDay);
        prevDay = curDay;
        
        if (newDay) wall = nextWall;
        
        bool success = false;
        for (double pos = att.W; pos <= att.E; pos += 0.5)
        {
            double curHeight = 0;
            if (wall.count(pos)) curHeight = wall[pos];
            if (curHeight < att.S) 
            { 
                success = true;
                nextWall[pos] = max(nextWall[pos], att.S); 
            }
        }
        
        ans += success;
    }
    
    return ans;
}

int main()
{
    int T; cin >> T;
    
    for (int t = 1; t <= T; t++)
    {
        cin >> N;
        
        for (int i = 0; i < N; i++)
            cin >> firstDay[i] >> numAttacks[i] >> west[i] 
                >> east[i] >> strength[i] >> deltaDays[i]
                >> deltaTravel[i] >> deltaStrength[i];
        
        printf("Case #%d: %d\n", t, solve());
    }
    
    return 0;
}
