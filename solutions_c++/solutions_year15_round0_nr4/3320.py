#include <bits/stdc++.h>
#define MAX 5
#define pii pair<int,int>

using namespace std;

bool b[MAX][MAX];
int t,x,r,c;

int main(){

  //  freopen("D-small-attempt1.in","r",stdin);
  //  freopen("D_small.out","w",stdout);
    cin >> t ;
    for(int u=1; u<=t; u++){
        cin >> x >> r >> c;
        for(int i=0; i<r; i++)
            for(int j=0; j<c; j++)
                b[i][j] = 0;

        cout << "Case #" << u << ": ";
        int a = min(r,c), b = max(r,c);
        if( x == 1 ) cout << "GABRIEL";
        else if( x == 2 ){
            if( r % 2 == 0 || c % 2 == 0 ) cout << "GABRIEL";
            else cout << "RICHARD";
        }else if( x == 3 ){
            if( (a == 2 && b == 3) || (r == 3 && c == 3) || (a == 3 && b == 4)  ) cout << "GABRIEL";
            else cout << "RICHARD";
        }else{
            if( min(r,c) == 1 ) cout << "RICHARD";
            else if( min(r,c) == 2 ) cout << "RICHARD";
            else{
                if( r == 3 && c == 3 ) cout << "RICHARD";
                else cout << "GABRIEL";
            }
        }

        cout << endl;
    }
}
