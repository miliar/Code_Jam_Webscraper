#include <iostream>
#include <fstream>

using namespace std;


int main()
{
	int iT;			// ���̽��� ��
	

	ifstream inputText;
	inputText.open("A-small-attempt3.in");

	ofstream outputText;
	outputText.open("Solve.txt");


	if (!inputText)
	{
		cout << "Cannot Open" << endl;

		return 0;
	}

	
	inputText >> iT;
	//cout << iT << endl;


	
	for (int i = 0; i < iT; i++ )
	{
		int audience;	// û���� ����
		inputText >> audience;

		int standAudience  = 0; // �Ͼ û���� ����
		int inviteAudience = 0; // �����ؾ� �� û���� ����

		int calcString;	// �������� ���õ� ���ڿ�
		inputText >> calcString;

		int temp = 1; // ��������� �ӽ� ����
		for (int k = 0; k < audience; k++ )
		{
			temp *= 10;
		}

		
		standAudience += calcString / temp;	//�ٷ� �Ͼ�� ������ ���� ���Ѵ�.
		calcString -= calcString / temp * temp;


		for (int j = 1; j <= audience; j++ )
		{
			temp /= 10;

			int temp2 = calcString / temp;

			if ( temp2 > 0 )
			{
				if (standAudience >= j) // ������ �����Ǹ� �ٷ� ������ �Ͼ�ٴ� �ǹ��̴�.
				{
					standAudience += calcString / temp;	//�ٷ� �Ͼ�� ������ ���Ѵ�.
				}
				else // ������ �������� �ʾ����Ƿ� ������ ������Ų��.
				{
					inviteAudience += j - standAudience;
					standAudience += inviteAudience;
					standAudience += calcString / temp;
				}
			}

			calcString -= calcString / temp * temp;
		}

		//cout << "Case #" << i+1 << ": " << inviteAudience << endl;
		outputText << "Case #" << i + 1 << ": " << inviteAudience << endl;
	}
	
	
	inputText.close();
	outputText.close();


	return 0;
}


