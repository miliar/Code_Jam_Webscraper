#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdlib>
#include <queue>

using namespace std;

typedef pair<vector<int>, int> com;
typedef vector<int> vec;

bool dp[2048];
vector <int> pan;
int target = 0;
queue<com> Q;

vector<int> swap(int n, vector<int> ory)
{
    vector<int> ret;
    for(int i=n-1; i>=0; i--)
        ret.push_back((ory[i]+1) % 2);
    
    for(int i=n; i<ory.size(); i++)
    {
        ret.push_back(ory[i]);
    }
    
    return ret;
}

int binary(vector<int> oryg)
{
    int res = 0;
    
    for(int i=0; i<oryg.size(); i++)
    {
        res *= 2;
        res += oryg[i];
    }
    
    return res;
}

int bfs(vector<int> fir)
{
    Q.push(com(fir, 0));
    dp[binary(fir)] = true;
    
    while(!Q.empty() )
    {
        //cout<<"here\n";
        vec akt = Q.front().first;
        int mov = Q.front().second;
        Q.pop();
        
        if(binary(akt) == target)
        {
            return mov;
        }
        
        for(int i=1; i<=akt.size(); i++)
        {
            vec news = swap(i, akt);
            if(!dp[binary(news)])
            {
                dp[binary(news)] = true;
                Q.push(com(news, mov+1));
            }
        }
    }
    
    return 0;
}

void klir()
{
    memset(dp, 0, sizeof(dp));
    pan.clear();
    while(!Q.empty() )
        Q.pop();
}

int main()
{
    ios_base::sync_with_stdio(0);
    
    int t;
    cin>>t;
    
    for(int x=1; x<=t; x++)
    {
        klir();
        
        string input;
        cin>>input;
        
        int s;
        s = input.size();
        target = (1<<s) - 1;
        
        for(int i=0; i<s; i++)
        {
            char k = input[i];
            if(k == '+')
                pan.push_back(1);
            else
                pan.push_back(0);
        }
        
        /*cout<<target<<"\n";
        for(int i=0; i<pan.size(); i++)
            cout<<pan[i];
        cout<<"\n"; */
        
        cout<<"Case #"<<x<<": "<<bfs(pan)<<"\n";
    }
    
    
    return 0;
}