#include <fstream>
#include <iostream>
#include <set>
#include <vector>
#include <map>
#include <iomanip>
#include <queue>
#include <deque>
#include <algorithm>
#include <cstring>

using namespace std;

typedef pair<int, int> pie;
#define L first
#define R second
#define MP make_pair
#define PB push_back

vector<int> v, q;

main()
{
    ios_base::sync_with_stdio(false);
    ifstream cin("A-small-attempt0.in");
    ofstream cout("A-small-attempt0.out");
    int t, num = 0;
    cin>>t;
    while(t--){
        num++;
        v.clear();
        q.clear();
        int fi, se;
        cin>>fi;
        for(int i=1;i<=4;i++)
            for(int j=1;j<=4;j++){
                int x;
                cin>>x;
                if(i == fi)
                    v.PB(x);
            }
        cin>>se;
        for(int i=1;i<=4;i++)
            for(int j=1;j<=4;j++){
                int x;
                cin>>x;
                if(i == se)
                    q.PB(x);
            }
        int ted = 0, tmp;
        for(int i=0;i<=3;i++)
            for(int j=0;j<=3;j++)
                if(v[i] == q[j]){
                    ted++;
                    tmp = v[i];
                }
        cout<<"Case #"<<num<<": ";
        if(ted == 0)
            cout<<"Volunteer cheated!"<<endl;
        if(ted == 1)
            cout<<tmp<<endl;
        if(ted > 1)
            cout<<"Bad magician!"<<endl;
    }
}
