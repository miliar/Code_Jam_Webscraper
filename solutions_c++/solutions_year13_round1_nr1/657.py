#define _CRT_SECURE_NO_WARNINGS

#include<stdio.h>
#include<math.h>

typedef long long ll;

ll func(ll r, ll g)
{
    return g * (2*g + 2*r - 1);
}

ll solve(ll r, ll t)
{
    // g == 1 �Œʉ߂ł��邱�Ƃ͖�肩��ۏ؂���Ă���B
    // ��E�� t �Ɏ���āA�������n�߂�B
    ll left = 1;
    ll right = t / r;
    if( right > 707106780LL*2 ){
        right = 707106781LL*2;
    }
    while(true)
    {
        ll g = (left + right) / 2;
        if( func(r,g) <= t ){
            // �`����B���₷�B
            if( right - left == 1 ){
                g = right;
            }else if( right == left ){
                break;
            }
            left = g;
        }else{
            // �����Ȃ��B���炷�B
            if( right == left ){
                --left;
                break;
            }else if( right - left == 1 ){
                g = left;
            }
            right = g;
        }
    }
    return left;
}

int main(void){

    int T;
    scanf("%d",&T);

    for(int round = 0;round < T;++round){
        // r ����h��n�߂āA g �{�̃����O�������̂ɕK�v�ȓh����
        // T(g) = g(2g + 2r - 1) �ŕ\�����B
        // �񕪒T���� T(g) <= t < T(g+1) �ɂȂ� g ��T��
        ll r;
        ll t;
        scanf("%lld %lld",&r,&t);
        printf("Case #%d: %lld\n",round+1,solve(r,t));
    }

    return 0;
}