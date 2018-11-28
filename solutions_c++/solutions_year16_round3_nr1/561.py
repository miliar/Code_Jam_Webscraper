#include <iostream>
#include <fstream>
#include <queue>
using namespace std;
#define LL long long
#define P pair<int, char>

priority_queue<P> q;
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t;

    cin >> t;
    for(int i = 0; i < t; i++){
        int n, p;
        cin >> n;
        for(int j = 0; j < n; j++){
            cin >> p;
            q.push(P(p, j));
        }

        cout << "Case #" << i + 1 << ":";
        while(!q.empty()){
            P f1 = q.top();
            q.pop();
            if(f1.first > 1)
                q.push(P(f1.first - 1, f1.second));
            P f2 = P(-1, -1);
            if(!q.empty()){
                f2= q.top();
                q.pop();
                if(f2.first > 1)
                    q.push(P(f2.first - 1, f2.second));
                else if(q.size() == 1){
                    q.push(f2);
                    f2 = P(-1, -1);
                }
            }

            cout << " " << (char)(f1.second + 'A');
            if(f2.first != -1)
                cout << (char)(f2.second + 'A');
        }

        cout << endl;

    }
    return 0;
}

