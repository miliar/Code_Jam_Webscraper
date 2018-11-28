#include <iostream>
#include <vector>
#include <algorithm>
#include <deque>
#include <stack>
#include <cmath>
#include <queue>
#include <string>
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    //freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int _T;
    cin >> _T;
    
    for(int _t=1; _t<=_T; _t++)
    {
        int A;
        int N;
        cin >> A >> N;
        vector <int> mote;
        int m;
        for(int i=0; i<N; i++)
        {
            cin >> m;
            mote.push_back(m);
        }
        
        sort(mote.begin(), mote.end());
        
        int op=0;
        for(int i=0; i<N; i++)
        {
            if(A > mote[i]) A += mote[i];
            else
            {
                int AA = A;
                int opp = 0;
                int need = 0;
                int idx;
                
                for(idx=i; idx<N && opp <= N-i; idx ++)
                {
                    while(AA <= mote[idx])
                    {
                        AA += AA-1, need++, opp++;
                        if(opp > N-i) break;
                    }
                    AA += mote[idx], need --;
                    if(need == 0) break;
                }
                
                op += min(opp, N-i);
                if(opp > N-i) break;
                A = AA;
                i = idx;
            }
        }
        
        cout << "Case #" << _t << ": " << op << endl;
    }
}
