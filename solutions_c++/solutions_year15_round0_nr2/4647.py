#include <iostream>
#include <algorithm>
#include <queue>

using namespace std;

const int inf = 1e9;

priority_queue<int> S;

int tim = inf;

void klir()
{
    while(!S.empty() )
        S.pop();
    
    tim = inf;
}

void reku(priority_queue<int> Q, int moves, int limit)
{
    int maksi = Q.top();
    //cout<<maksi<<"\n";
    
    tim = min(tim, maksi + moves);
    
    Q.pop();
    
    for(int i=1; i<=maksi/2; i++)
    {
        priority_queue<int> cp = Q;
        cp.push(i);
        cp.push(maksi-i);
        
        if(moves <= limit)
            reku(cp, moves+1, limit);
    }
}

int main()
{
    ios_base::sync_with_stdio(0);
    
    int testy;
    cin>>testy;
    
    for(int x=1; x<=testy; x++)
    {
        klir();
        int d;
        cin>>d;
        
        for(int i=1; i<=d; i++)
        {
            int p;
            cin>>p;
            S.push(p);
        }
        
        reku(S, 0, S.top() );
        
        cout<<"Case #"<<x<<": "<<tim<<"\n";
    }
    
    
    
    return 0;
}