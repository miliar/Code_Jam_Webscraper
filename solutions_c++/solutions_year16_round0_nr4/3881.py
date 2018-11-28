#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <complex>
#include <sstream>
#include <iostream>
#include <iomanip>

using namespace std;

template<class T> inline T sqr(T x) { return x*x; }

typedef long long ll;//int(4�o�C�g)��2�~10^9���x�܂� %llu �iint��long�͓����j

#define REP(i,n) for (int i=0;i<(n);i++) //for�����������������H

#define ALL(a)  (a).begin(),(a).end()
#define RALL(a) (a).rbegin(),(a).rend()
#define PB push_back
#define MP make_pair
#define SORT(c) sort((c).begin(),(c).end())//�R���e�i�̂� �z��̃\�[�g��sort(array,array+N)
#define CLR(a) memset((a), 0 ,sizeof(a)) //1byte�P�� �R���e�i��fill

const double PI = acos(-1.0);
/*int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};*/

int main() {
	/*�e�X�g�P�[�X�ϐ�*/
	int Test;
	scanf("%d", &Test);
	/*�J��Ԃ����̕ϐ��������Y��ɋC��t����*/
	for (int Case = 1; Case <= Test; Case++){
		int k,c,s;
		scanf("%d %d %d",&k, &c, &s); //���������͂̏ꍇ��%*c�ɂ�鐔���̌�Ɏc����s�̓ǂݎ̂ĕK�v���� �ǂݎ̂Ă�̂ɕϐ��͂���Ȃ�
		if(c == 1) {
			if(s < k) {
				printf("Case #%d: IMPOSSIBLE\n", Case);
			} else {
				printf("Case #%d:", Case);
				for(int i = 1; i <= k; i++) printf(" %d", i);
				printf("\n");			
			}
			continue;
		}
		if(s < (k / 2) + 1) {
			printf("Case #%d: IMPOSSIBLE\n", Case);
			continue;
		}
		else {
			ll l = 1;
			for(int i = 0; i < c; i++) l *= k;
			printf("Case #%d:", Case);
			for(int i = 1; i <= (k / 2) + 1; i++) printf(" %llu", (l / k) * i - (i - 1));
			printf("\n");
		}
	}
	return 0;
}