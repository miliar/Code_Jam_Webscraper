#include <cstdio>
#include <iostream>

using namespace std;

int main() {
    //freopen("D-small-attempt0.in","r",stdin);
    //freopen("D-small.out","w",stdout);
    freopen("D-large.in","r",stdin);
    freopen("D-Large.out","w",stdout);
    int t, T, X, R, C, W, ans;
    scanf("%d",&T);
    for ( t = 1 ; t <= T ; t ++ ) {

        scanf("%d %d %d",&X,&R,&C);
        if ( C > R )
            swap(R,C);

        W = (X+1)/2; // �̤j�e��
        if ( X >= 7 ) ans = 0; // R �靈�Ŭ}������
        else if ( R >= X && C >= W ) { // �T�O R ���޿����omino �ܤ֤��|�񤣶i�h ( �����1���u )
            if ( (R*C)%X != 0 ) ans = 0; // ���n���X�k, R����
            else if ( C == W && X > 3 ) {// �I�_�����p�BX > 3 ( ���� )
                if ( X == 4 ) ans = 0;
                else if ( X == 5 ) {
                    if ( R >= 10 ) ans = 1;
                    else ans = 0;
                }
                else ans = 0; // X == 6
            }
            else ans = 1;
        }
        else ans = 0;

        printf("Case #%d: %s\n",t,ans==0?"RICHARD":"GABRIEL");
    }

    return 0;
}
