#include "template.h"


/*
	����
	1.
	G�� 1������ �� original seq���� G�� ã�� �� �ִ� ���� ���� �߿�
	��׸� ã�°� �����ϸ� ������ �翬�� �ȴ�

	2.
	k, c=1
	: s�� k��ŭ �ʿ��ϴ�. ��� ĭ�� ���� �Ѵ�.
	
	3.
	c�� 1�� �þ�� 1ĭ���� �����غ� �� �ִ� ����� ���� +1�� �þ��
	
	��
	k=6 c=1 : s�� 6�ʿ�
	k=6 c=2 : s�� 3�ʿ�
	k=6 c=3 : s�� 2�ʿ�
	
	k=3 c=3 : s�� 1�ʿ�
	�� c*s >= k���� �Ѵ� ����?


*/


int main() {
	freopen("D-small-attempt0_.in", "r", stdin);
	freopen("output_D.txt", "w", stdout);
	int TC; cin >> TC;
	for (int tc = 1; tc <= TC; ++tc) {
		long long k, c, s;
		cin >> k >> c >> s;
		long long kc = 1;
		for (long long i = 0; i < c; ++i) {
			kc *= k;
		}
		vector<long long> ans;


		if (k == s) {
			long long kc_1 = kc / k;
			for (long long i = 0; i < k; ++i) {
				ans.push_back(i * kc_1 + 1);
			}
		}
		else if(c*s >= k){

		}
		
		printf("Case #%d: ", tc);
		if (ans.empty()) {
			printf("IMPOSSIBLE\n");
		}
		else {
			for (auto l : ans) {
				cout << l << ' ';
			}cout << endl;
		}
	}
	return 0;
}