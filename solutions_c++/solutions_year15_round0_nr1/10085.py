#include <iostream>
#include <string>

/*
�㿡 ������ ����� ���� ģ���� ���� ������ �ִ�.
�ʴ� ��û�ڴ� �ƴ����� �׳డ ����鿡�� �Ͼ�� �ڼ��� �ޱ⸦ ���Ѵ�.

ó������ ��û�ڴ� �ɾ��ִ�. �׸��� ��� ��û�ڵ��� �������� ���� ������ �ִ�.
���� �� ������ ������ 2��� ������ 2���� û���� �ڼ��� ġ�°��� ���� �ش� ������
����� �Ͼ �ڼ��� ġ�� �ȴ�. �׶����� ��ٸ��� �� ���̴�.

����� ��� û���� ������ ������ �˰� ������ �̶����� �׳��� ģ���� �߰��� �ʴ��ϰ���
�Ѵ�. �׷��� �ʴ�Ǵ� ģ������ ������ ������ �󸶰� �ǵ� ����� ����.

�̶� ����� ģ���� �ʴ��ؾ��ϴ°��� ���ؾ� �ϴ� �����̴�.

�Է� :
ù������ �׽�Ʈ ���̽� T

�״��� ���� ������ �׽�Ʈ ���̽� ���� ù��°�� Smax�� �־�����.
�̴� û�� �������� �ִ� ������ �����̴�.

�� ������ û���� ���� ���� ���ڸ� ��Ÿ���µ� �ش� ���� ������ ������ 0���� ī��Ʈ
�Ǹ�, ���� ��� �Ʒ��� ����.

"409"�� ��� ���� û���� 4��, 0��, 9�� �ִٴ� ���̰� ������ ������ ����
Si = 0, 1, 2 ������ �̷�� ���� �ȴ�.

û���� ���� �ϳ��� ���� ������ 0 ~ 9������ ���ڷ� �ʱ�ȭ �ȴ�.
*/
using namespace std;

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);

	int T = 0;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		int Smax = 0;
		char stringPeople[1002] = { 0, };
		cin >> Smax >> stringPeople;

		int needFriends = 0;
		int appendPeople = 0;
		int stringLength = strlen(stringPeople);
		for (int j = 0; j < stringLength; j++) {
			int Si = j;
			int stringCount = stringPeople[j] - '0';

			// �̰����� �ʿ��� �ο��� ���� ���
			// �ϳ��� ���� �ִ� �ο����� 9��
			if (stringCount > 0 && appendPeople < Si) {
				// ���� �̹��ٿ� ������ ������ ���� �ڼ��� ĥ �� ���� ��Ȳ�� ���
				needFriends += Si - appendPeople;
				appendPeople += needFriends;
			}

			// �ʿ� �ο����� ����
			appendPeople += stringCount;
		}
		cout << "Case #" << i << ": " << needFriends << endl;
	}
	return 0;
}