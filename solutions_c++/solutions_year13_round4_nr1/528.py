#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct passenger{
    int l, r;
    long long cnt;
    inline passenger (){}
    inline passenger( int l, int r, long long cnt ){
        this -> l = l;
        this -> r = r;
        this -> cnt = cnt;
    }
};

int N, M;
const long long modulo = 1000002013;
vector < passenger > v;

void scan(){
    cin >> N >> M;
    v.erase ( v.begin(), v.end() );

    for ( int i = 0; i < M; ++i ){
        passenger t1;
        cin>> t1.l >> t1.r >> t1.cnt;
        v.push_back ( t1 );
    }
}

inline long long calc ( long long x ){
    return x * ( x - 1 ) / 2;
}

long long go( vector < passenger > t ){
    long long res = 0;

    for ( int i = 0; i < t.size(); ++i )
        res = ( res + ( calc( t[i].l - t[i].r ) % modulo ) * t[i].cnt ) % modulo;

    return res;
}

int diff ( vector < passenger > &t1, vector < passenger > &t2 ){
    if ( t1.size() != t2.size() )
        return 1;

    for ( int i = 0; i < t1.size(); ++i )
        if ( t1[i].l != t2[i].l || t1[i].r != t2[i].r || t1[i].cnt != t2[i].cnt )
            return 1;
    return 0;
}

bool f ( passenger t1, passenger t2 ){
    if ( t1.l == t2.l )
        if ( t1.r == t2.r )
            return t1.cnt < t2.cnt;
        else
        return t1.r < t2.r;
    return t1.l < t2.l;
}
inline long long MIN ( long long t1, long long t2 ){
    return ( t1 < t2 ) ? t1 : t2;
}

vector < passenger > workit ( vector < passenger > v ){
    vector < passenger > res;
    sort ( v.begin(), v.end(), f );

    for ( int i = 0; i < v.size(); ++i ){
        for ( int j = i + 1; j < v.size() && v[j].l <= v[i].r; ++j )
        if ( v[i].l < v[j].l && v[j].l <= v[i].r && v[j].r > v[i].r ){
            int cnt = MIN ( v[i].cnt, v[j].cnt );
            if ( cnt == 0 )
                continue;
            v[i].cnt -= cnt;
            v[j].cnt -= cnt;
            res.push_back ( passenger ( v[i].l, v[j].r, cnt ) );
            res.push_back ( passenger ( v[j].l, v[i].r, cnt ) );
            if ( v[i].cnt == 0 )
                break;
        }
        if ( v[i].cnt )
            res.push_back ( v[i] );
    }

    vector < passenger > res2;
    res2.push_back ( res[0] );
    for ( int i = 1; i < res.size(); ++i )
        if ( res2.back().l == res[i].l && res2.back().r == res[i].r )
            res2.back().cnt += res[i].cnt;
        else
            res2.push_back ( res[i] );

    return res;
}

long long solve(){
    long long oldRes = go( v ),  nwRes = 0;

    vector < passenger > t;
    do{
        t = v;
        v = workit(v);
        sort ( v.begin(), v.end(), f );
    //    cout << v.size() << " " << t.size() << endl;
 //       for ( int i = 0; i < v.size(); ++i )
   //         cout << v[i].l << " " << v[i].r << " " << v[i].cnt << endl;
    }
    while ( diff ( t, v ) );


    nwRes = go ( v );

    nwRes -= oldRes;
    nwRes = ( nwRes % modulo + modulo ) % modulo;
    return nwRes;
}
int main(){
    int tests;
    cin >> tests;

    for ( int i = 1; i <= tests; ++i ){
        scan();
        cout << "Case #" << i << ": "<< solve() << endl;
    }
}
