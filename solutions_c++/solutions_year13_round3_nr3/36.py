#include <iostream>
#include <cstring>
#include <vector>
#include <map>

using namespace std;

struct attack{
    int l, r, s, d;
    attack(){};
    attack ( int l, int r, int s, int d ){
        this -> l = l;
        this -> r = r;
        this -> s = s;
        this -> d = d;
    }
};

int N;
int n[1024], d[1024], w[1024], e[1024], s[1024], delta_d[1024], delta_p[1024], delta_s[1024];

map < int, vector <attack> >mp;
map < double, int > wall;
int it[1 << 25], sz;
int leftSon[1 << 25];
int rightSon[1 << 25];
int up[1 << 25];

void scan(){
    cin >> N;

    for ( int i = 0; i < N; ++i )
        cin >> d[i] >> n[i] >>w[i] >> e[i] >> s[i] >> delta_d[i] >> delta_p[i] >> delta_s[i];
}

int find ( long long l, long long r, int idx, long long L, long long R ){
    if ( R < l || r < L )
        return 2e9;

    if ( L <= l && r <= R ){
        return max ( it[idx], up[idx] );
    }

    long long mid = ( l + r ) / 2;
  //  cout << l << " " << r << " " <<  idx << " " << mid <<  endl;
    if ( !leftSon[idx] )
        leftSon[idx] = ++sz;
    if( !rightSon[idx] )
        rightSon[idx] = ++sz;

    return max ( min ( find ( l, mid, leftSon[idx], L, R ), find ( mid + 1, r, rightSon[idx], L, R ) ) , up[idx] );
}

int find ( long long l, long long r ){
    return find ( 0, 4e9 + 1, 1, l, r );
}

int successfulAttack ( attack t ){
    long long l = t.l, r = t.r;
    l += 1e9;
    r += 1e9;
    l *= 2;
    r *= 2;


    int x = find ( l, r );
   // cout << l << " " << r << " " << x << " " << t.s<<endl;

    return x < t.s;
}

void update ( long long l, long long r, int idx, long long L, long long R, int val ){
    if ( R < l || r < L )
        return;

    if ( L <= l && r <= R ){
        if ( up[idx] < val ) up[idx] = val;
  //      cout << l << " " << r << " " << val << endl ;
        it[idx] = max ( it[idx], val );
        return;
    }

    long long mid = ( l + r ) / 2;

    if ( !leftSon[idx] )
        leftSon[idx] = ++sz;
    if ( !rightSon[idx] )
        rightSon[idx] = ++sz;

    update ( l, mid, leftSon[idx], L, R, val );
    update ( mid + 1, r, rightSon[idx], L, R, val );

    it[idx] = min ( it[leftSon[idx]], it[rightSon[idx]] );
    it[idx] = max ( it[idx], up[idx] );
       // cout << l << " " << r << " " << it[idx] << endl ;
}
void update ( long long l, long long r, int val ){

    update ( 0, 4e9 + 1, 1, l, r, val );
}

void update ( attack t ){
    long long l = t.l, r = t.r;
    l += 1e9;
    r += 1e9;
    l *= 2;
    r *= 2;


    update ( l, r, t.s );
}


void solve(int testNumber){
    mp.erase ( mp.begin(), mp.end() );
    wall.erase ( wall.begin(), wall.end() );
    memset ( leftSon, 0, sizeof ( leftSon ) );
    memset ( it, 0, sizeof ( it ) );
    memset ( rightSon, 0, sizeof ( rightSon )  );
    memset ( up, 0, sizeof ( up ) );
    sz = 1;

    for ( int i = 0; i < N; ++i ){
        int dd = d[i], ww = w[i], ee = e[i], ss = s[i];
        for ( int j = 0; j < n[i]; ++j ){
            mp[dd].push_back ( attack ( ww, ee, ss, dd ) );
            ww += delta_p[i];
            ee += delta_p[i];
            ss += delta_s[i];
            dd += delta_d[i];
        }
    }
    int res = 0;

    for ( map < int, vector < attack > > :: iterator it = mp.begin(); it != mp.end(); ++it ){
        vector < attack > &v = it -> second;

        for ( int i = 0; i < v.size(); ++i )
            res += successfulAttack ( v[i] );
      //  cout << it->first << " " << it->second[0].l << endl;

        for ( int i = 0; i < v.size(); ++i)
            update ( v[i] );
       // return;
    }
    cout << "Case #" << testNumber << ": " << res << endl;
}
int main(){
    int tests;
    cin >> tests;

    for ( int i = 1; i <= tests; ++i ){
        scan();
        solve(i);
    }
}
