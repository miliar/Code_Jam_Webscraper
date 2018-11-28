#include <iostream>
using namespace std;

void ReadTestCase(int tNum);

int maxS;
char sList[1001];
FILE *stream1;
FILE *stream2;

int main()
{
	freopen_s(&stream1, "A-large.in", "r", stdin);
	freopen_s(&stream2, "A-large.out", "w", stdout);

	//테스트 케이스의 수 입력
	int t;		//테스트케이스의 수
	cin >> t;

	//테스트 케이스의 수 만큼 읽기
	for (int i = 0; i < t; i++){
		ReadTestCase(i + 1);
	}
	fclose(stream1);
	fclose(stream2);
	return 0;
}

//tNum번째 테스트케이스 읽기
void ReadTestCase(int tNum)
{
	// 조건 읽기
	cin >> maxS >> sList;

	int n = 0; // 누적된 일어난 관객 수
	int a = 0; // 내가 동원한 관객 수
	for (int s = 0; s <= maxS; ++s)
	{
		if (n < s)
		{
			// 누적 수가 부끄러움 레벨보다 부족하면 부족한 만큼 동원
			a += (s - n);
			n += (s - n);
		}

		// 이번 레벨에 일어난 관객수 누적
		n += (sList[s] - '0');
	}

	cout << "Case #" << tNum << ": " << a << endl;
}