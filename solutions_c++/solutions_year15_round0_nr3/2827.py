/**
 * Md Imran Hasan Hira (imranhasanhira@gmail.com)
 */

#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>

using namespace std;

typedef long long LL;
typedef pair<int,int> PII;

int grid[256][256];
int sgrid[256][256];
int data[]={'1', 'i','j','k'};

void initData(){
    grid['h']['h']='h'; grid['h']['i']='i'; grid['h']['j']='j'; grid['h']['k']='k';
    grid['i']['h']='i'; grid['i']['i']='h'; grid['i']['j']='k'; grid['i']['k']='j';
    grid['j']['h']='j'; grid['j']['i']='k'; grid['j']['j']='h'; grid['j']['k']='i';
    grid['k']['h']='k'; grid['k']['i']='j'; grid['k']['j']='i'; grid['k']['k']='h';

    sgrid['h']['h']= 1; sgrid['h']['i']= 1; sgrid['h']['j']= 1; sgrid['h']['k']= 1;
    sgrid['i']['h']= 1; sgrid['i']['i']=-1; sgrid['i']['j']= 1; sgrid['i']['k']=-1;
    sgrid['j']['h']= 1; sgrid['j']['i']=-1; sgrid['j']['j']=-1; sgrid['j']['k']= 1;
    sgrid['k']['h']= 1; sgrid['k']['i']= 1; sgrid['k']['j']=-1; sgrid['k']['k']=-1;
}



bool calc(string &s, vector<vector<vector<int> > > &v, int curpos, int last, int lastsign, int di){
    if(curpos==s.size()) return di==4;
    if(di==4) return curpos==s.size();

    //cout << "curpos " << curpos << ", di " << di << endl;
    int next = s[curpos];

    int &r = v[di-1][next-'h'][curpos];
    if(r !=-1 ) return r;

    int tr = false;
    if( lastsign * sgrid[last][next] == 1
       && grid[last][next] == data[di]){
        tr = calc(s, v, curpos+1, 'h', 1, di+1);
    }
    if(!tr){
        tr = calc(s, v, curpos+1, grid[last][next], lastsign * sgrid[last][next], di);
    }
    r = tr;
    return r;
}

int main(){

    freopen("C-small-attempt1.in", "r", stdin);
    freopen("c.out", "w", stdout);


    initData();


    int T, L, X;
    string t;
    cin >> T;
    for(int test=0;test<T;test++){
        cin >> L >> X >> t;
        string s;
        for(int i=0;i<X;i++){
            s.append(t);
        }

        vector<vector<vector<int> > > v(3, vector<vector<int> >(4, vector<int>(L*X, -1) ));

        bool r = calc(s, v, 0, 'h', 1, 1);
        printf("Case #%d: %s\n", test+1, (r ? "YES" : "NO"));

    }

    return 0;
}
