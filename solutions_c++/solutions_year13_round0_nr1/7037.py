#include <iostream>
#include <cstdio>
#include <map>

#define f(i,beg,end) for(int i=beg; i<=end; i++)

using namespace std;

void redirect()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
}

string board[5];

void init()
{
    f(i,1,4) 
    {
        cin >> board[i];
        board[i] = " " + board[i];
    }
}

void solve(int testnum)
{
    int ans = -1;
    string ret[4] = { "X won", "O won", "Draw", "Game has not completed" };
    
    // checking rows
    
    f(i,1,4)
    {
        map < char, int > cnt;
    
        f(j,1,4)
            cnt[ board[i][j] ]++;
        
        if (cnt['O'] + cnt['T'] == 4)
        {
            ans = 1;
            break;
        }
        
        if (cnt['X'] + cnt['T'] == 4)
        {
            ans = 0;
            break;
        }
    }
    
    // checking cols
    f(i,1,4)
    {
        map < char, int > cnt;
    
        f(j,1,4)
            cnt[ board[j][i] ]++;
        
        if (cnt['O'] + cnt['T'] == 4)
        {
            ans = 1;
            break;
        }
        
        if (cnt['X'] + cnt['T'] == 4)
        {
            ans = 0;
            break;
        }
    }
    
    // checking main diagonal
    {
        map < char,int > cnt;
        
        f(i,1,4)
            cnt[ board[i][i] ]++;
        
        if (cnt['O'] + cnt['T'] == 4)
        {
            ans = 1;
        }
        
        if (cnt['X'] + cnt['T'] == 4)
        {
            ans = 0;
        }
    }
    
    // checking secondary diagonal
    {
        map < char,int > cnt;
        
        f(i,1,4)
            cnt[ board[i][5-i] ]++;
        
        if (cnt['O'] + cnt['T'] == 4)
        {
            ans = 1;
        }
        
        if (cnt['X'] + cnt['T'] == 4)
        {
            ans = 0;
        }
    }
    
    if (ans==-1)
    {
        f(i,1,4)
            f(j,1,4)
                if (board[i][j]=='.') ans = 3;
    }
    
    if (ans==-1) ans = 2;
    
    cout << "Case #" << testnum << ": " << ret[ans] << endl;
}

int main()
{
    redirect();
    
    int tests = 1;   cin >> tests;
    
    f(i,1,tests)
    {
        init();
        solve(i);
    }
    
    return 0;
}