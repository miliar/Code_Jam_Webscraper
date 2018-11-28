// ALLAH IS ALMIGHY /
#include <bits/stdc++.h>
using namespace std;

char alpha[27];
int n,cnt[30];

int findMax(){
    int mx = 0;
    for( int i=1;i<=n;i++ ){
        if( mx < cnt[i] )
            mx = cnt[i];
    }return mx;
}

int main()
{
    //freopen( "A-large (1).in","r",stdin );
    //freopen( "output.in","w",stdout );
    cin.sync_with_stdio( false );
    int j=1, cs=0;
    for( char i='A';i<='Z';i++ ){
        alpha[j++] = i;
    }
    int t;
    cin >> t;
    while( t-- ){
        cin >> n;
        int k = 0;
        for( int i=1;i<=n;i++ ){
            cin >> cnt[i];
            k += cnt[i];
        }
        cout << "Case #" << ++cs << ": ";
        while( k ){
            int maj = findMax();
            int f=0;
            for( int i=1;i<=n;i++ ){
                if( cnt[i]==maj ){
                    cnt[i]--;
                    k--;
                    f++;
                    if( k==2 ){
                        cout << alpha[i] << " ";
                        break;
                    }
                    cout << alpha[i];
                }if( f==2 ){
                    cout << " ";
                    f = 0;
                }
            }
            if( f==1 )cout << " ",f=0;
        }
        cout << endl;
    }return 0;

}
