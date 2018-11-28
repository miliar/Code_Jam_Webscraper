#define _CRT_SECURE_NO_WARNINGS

#include<stdio.h>
#include<math.h>
#include<algorithm>

using namespace std;

typedef long long ll;
ll wn[1000];
ll n;
ll maxans;

ll solve(ll ans, ll depth, ll w)
{
    // ���߂Ȏ�
    if( ans >= maxans ){
        return ans;
    }
    // �I�[
    if( depth >= n ){
        return ans;
    }
    // �H�ׂ���Ȃ�H�ׂ�B
    // �H�ׂ��Ȃ��Ȃ�A�萔�� n �����Ȃ�h�[�v�B
    // �������͈ȍ~�S���̂Ă�B
    if( wn[depth] < w ){
        return solve(ans,depth+1,w+wn[depth]);
    }

    // �ȍ~�S���̂Ă��Ƃ�����H
    ll oa = ans;
    ans += n - depth;
    if( maxans > ans ){ maxans = ans; }

    // �����ŕ⏕�����Ƃ�����H
    ll sup = w-1;
    if( sup > 0 ){
        ll la = solve(oa + 1,depth,w+sup);
        if( la < ans ){ ans = la; }
    }

    return ans;
}

int main(void){

    int T;
    scanf("%d",&T);

    for(int round = 0;round < T;++round){
        ll ans = 0;
        ll w = 0;
        scanf("%lld %lld",&w,&n);
        for(ll i = 0;i < n;++i){
            scanf("%lld",&wn[i]);
        }
        // �\�[�g���āA���������̂��ǂ�ǂ�H�ׂ�B
        // �H�ׂ��Ȃ��Ȃ����ꍇ�A w-1 �� k �񑫂��Ē�����̂������A
        // �S���̂Ă�̂��������v�Z���Ċo���Ă����B
        std::sort(wn,wn+n);
        maxans = n;
        printf("Case #%d: %lld\n",round+1,solve(0,0,w));
    }

    return 0;
}