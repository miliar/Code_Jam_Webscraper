#include <iostream>
#include <string>

/*
밤에 열리는 오페라에 너의 친구가 유명 가수로 있다.
너는 시청자는 아니지만 그녀가 사람들에게 일어나서 박수를 받기를 원한다.

처음에는 시청자는 앉아있다. 그리고 모든 시청자들은 수줍음에 대한 레벨이 있다.
만약 이 수줍음 레벨이 2라면 이전의 2명의 청중이 박수를 치는것을 봐야 해당 레벨의
사람이 일어나 박수를 치게 된다. 그때까진 기다리게 될 것이다.

당신은 모든 청중의 수줍음 레벨을 알고 있으며 이때문에 그녀의 친구를 추가로 초대하고자
한다. 그렇게 초대되는 친구들의 수줍음 레벨은 얼마가 되도 상관이 없다.

이때 몇명의 친구를 초대해야하는가를 구해야 하는 문제이다.

입력 :
첫라인은 테스트 케이스 T

그다음 부터 각각의 테스트 케이스 마다 첫번째에 Smax가 주어진다.
이는 청중 개개인의 최대 수줍음 레벨이다.

그 다음은 청중의 각각 열의 숫자를 나타내는데 해당 열의 수줍음 레벨은 0부터 카운트
되며, 예를 들면 아래와 같다.

"409"일 경우 각각 청중이 4명, 0명, 9명 있다는 것이고 수줍음 레벨은 각각
Si = 0, 1, 2 순서로 이루어 지게 된다.

청중의 수는 하나의 열당 무조건 0 ~ 9사이의 숫자로 초기화 된다.
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

			// 이곳에서 필요한 인원의 수를 계산
			// 하나의 열에 최대 인원수는 9명
			if (stringCount > 0 && appendPeople < Si) {
				// 만약 이번줄에 수줍음 레벨에 의해 박수를 칠 수 없는 상황일 경우
				needFriends += Si - appendPeople;
				appendPeople += needFriends;
			}

			// 필요 인원수를 누적
			appendPeople += stringCount;
		}
		cout << "Case #" << i << ": " << needFriends << endl;
	}
	return 0;
}