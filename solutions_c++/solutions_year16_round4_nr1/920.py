#include <cstdio>
#include <iostream>
#include <cstring>

using namespace std;

int ans[13][3];
int p2[13];

string s;

void init() {
    int i, j;
    memset(ans,0,sizeof(ans));
    ans[1][0] = 1; ans[1][1] = 1;
    for ( i = 2 ; i <= 12 ; ++ i ) {
        ans[i][0] = ans[i-1][0] + ans[i-1][2];
        ans[i][1] = ans[i-1][1] + ans[i-1][0];
        ans[i][2] = ans[i-1][2] + ans[i-1][1];
        //printf("i = %2d, %d %d %d\n",i,ans[i][0],ans[i][1],ans[i][2]);
    }
    p2[0] = 1;
    for ( i = 1 ; i <= 12 ; ++i ){
        p2[i] = p2[i-1]*2;
        //printf("p2[%d] = %d\n",i,p2[i]);
    }

}

void p( int n , char c ) {
    if ( n == 0 ) {
        s += c;
        return ;
    }
    else {
        if ( c == 'P') {
            p(n-1,'P');
            p(n-1,'R');
        }
        else if ( c == 'S' ) {
            p(n-1,'P');
            p(n-1,'S');
        }
        else if ( c == 'R' ) {
            p(n-1,'R');
            p(n-1,'S');
        }
        else {
            printf("ERROR\n");
            return ;
        }
    }
}




int main() {
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    init();
    int i, j, t, T, N, R, P, S, per;
    scanf("%d",&T);
    for ( t = 1 ; t <= T ; ++ t ) {
        scanf("%d %d %d %d",&N,&R,&P,&S);
        printf("Case #%d: ",t);
        s ="";
        if ( P == ans[N][0] && R == ans[N][1] && S == ans[N][2] ) { // P WIN
            p(N,'P');
        }
        else if ( R == ans[N][0] && S == ans[N][1] && P == ans[N][2] ) { // R WIN
            //printf("RWIN!\n");
            p(N,'R');
        }
        else if ( S == ans[N][0] && P == ans[N][1] && R == ans[N][2] ) {
            p(N,'S');
        }
        else {
            printf("IMPOSSIBLE");
        }
        if( s.compare("") != 0 ) {
            //cout << s << endl;
            for ( per = 1, j = 1; j <= N ; ++ j, per = per*2 ) {
                //cout << "per = " << per << endl;
                for ( i = 0 ; i < p2[N]; i = i + per*2 ) {
                    //cout << "s size = " << s.size() << endl;
                    //cout << s.substr(i,per) << " vs " << s.substr(i+per,per) << endl;
                    if ( s.compare(i,per,s,i+per,per) > 0 ) {
                        string s1 = s.substr(0,i);
                        string s2 = s.substr(i,per);
                        string s3 = s.substr(i+per,per);
                        string s4 = s.substr(i+per*2);
                        s = s1+s3+s2+s4;
                    }
                    //printf("s size = %d\n\n",s.size());
                }
            }
            cout << s;
        }


        printf("\n");
    }
    return 0;
}
