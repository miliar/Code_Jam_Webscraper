#include <cstdio>

using namespace std;

int cc[256];

int sub_s( int a, const char *s ) {
    while ( *s ) {
        cc[*s] -= a;
        s++;
    }
    return a;
}

int main() {
    int tttt;
    scanf("%d",&tttt);
    for ( int jhvchjsvdj = 1; jhvchjsvdj<=tttt; jhvchjsvdj++ ) {
        char t[ 20004 ];
        int w[10];
        for ( int i=0; i<256; i++ ) cc[i]=0;
        scanf("\n%s",t);
        char *ee = t;
        while ( *ee ) {
            cc[*ee]++;
            ee++;
        }
        w[6]=sub_s( cc['X'], "SIX" );
        w[8]=sub_s( cc['G'], "EIGHT" );
        w[4]=sub_s( cc['U'], "FOUR" );
        w[2]=sub_s( cc['W'], "TWO" );
        w[3]=sub_s( cc['H'], "THREE" );
        w[0]=sub_s( cc['R'], "ZERO" );
        w[1]=sub_s( cc['O'], "ONE" );
        w[7]=sub_s( cc['S'], "SEVEN" );
        w[5]=sub_s( cc['V'], "FIVE" );
        w[9]=sub_s( cc['I'], "NINE" );
        printf("Case #%d: ",jhvchjsvdj);
        for ( int i=0; i<10; i++ ) {
            for ( int j=0; j<w[i]; j++ ) printf("%c",'0'+i);
        }
        printf("\n");
    }
    return 0;
}

