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

	//�׽�Ʈ ���̽��� �� �Է�
	int t;		//�׽�Ʈ���̽��� ��
	cin >> t;

	//�׽�Ʈ ���̽��� �� ��ŭ �б�
	for (int i = 0; i < t; i++){
		ReadTestCase(i + 1);
	}
	fclose(stream1);
	fclose(stream2);
	return 0;
}

//tNum��° �׽�Ʈ���̽� �б�
void ReadTestCase(int tNum)
{
	// ���� �б�
	cin >> maxS >> sList;

	int n = 0; // ������ �Ͼ ���� ��
	int a = 0; // ���� ������ ���� ��
	for (int s = 0; s <= maxS; ++s)
	{
		if (n < s)
		{
			// ���� ���� �β����� �������� �����ϸ� ������ ��ŭ ����
			a += (s - n);
			n += (s - n);
		}

		// �̹� ������ �Ͼ ������ ����
		n += (sList[s] - '0');
	}

	cout << "Case #" << tNum << ": " << a << endl;
}