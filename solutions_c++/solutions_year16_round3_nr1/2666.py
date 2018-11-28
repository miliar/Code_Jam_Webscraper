#include <bits/stdc++.h>

#define size(n) ( int( n.size() ) )
#define sqr(n) ( (n) * (n) )

using namespace std;

int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t, n, k, i, j, sum = 0;
    cin >> t;
    for ( k = 1; k <= t; k++ ){
        cin >> n;
        priority_queue < pair < int, int > > q;
        int tmp, num, tmp2, num2;
        sum = 0;
        for ( i = 1; i <= n; i++ ){
            cin >> tmp;
            sum += tmp;
            q.push( make_pair( tmp, i ) );
        }
        cout << "Case #" << k << ": ";
        while( !q.empty() ){
            tmp = q.top().first;
            num = q.top().second;
            if ( ( tmp == 1 ) && ( size(q) == 2 ) ){
                cout << char( int('A') + num - 1 );
                q.pop();
                cout << char( int('A') + q.top().second - 1 );
                break;
            }
            cout << char( int('A') + num - 1 );
            q.pop();
            if ( tmp != 1 ){
                q.push( make_pair(tmp-1,num) );
            }
            sum--;
            if ( tmp != 1 ){
                //cout << q.top().first << endl;
                if ( q.top().first > sum - q.top().first ){
                    tmp2 = q.top().first;
                    num2 = q.top().second;
                    q.pop();
                    cout << char( int('A') + num2 - 1 );
                    if ( tmp2 != 1 ){
                        q.push( make_pair(tmp2-1,num2) );
                    }
                    sum--;
                }
            }
            cout << " ";
        }
        cout << endl;
    }


    return 0;
}

