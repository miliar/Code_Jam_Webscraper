#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

ifstream input("B-small-attempt4.in");
ofstream output("output.txt");
//ԭ���Լ��ܳԲ��ñ��˳�
//�������˳�Ҫ��һ���ӣ��ڴ��ڼ��Ҷ�û��
//��ͣ�͵�һ���������ܵ���һ���˳�

//����ԤҪ��������
//����Ԥ�Ļ�ʱ����pmax
//Ѱ��һ�ָ�Ԥ��������ȡ�����ţ����ٲ��ử�����㡣


int main()
{
	int T; input >> T;
	int D;
	int p[7];
	int longestemp;
	int minute;
	int next;
	int jb;
	bool isfind;
	int zuidazhi;
	for (int i = 1; i <= T; i++)
	{
		minute = 0;
		input >> D;
		
		//vector<int> TongJi(11, 0);
		int TongJi[10] = { 0 };
		for (int j = 1; j <= D; j++)
			input >> p[j];
		for (int j = 1; j <= D; j++)
			++TongJi[p[j]];
		isfind = false;
		for (int k = 9; k >= 1; k--)
		{
			if (TongJi[k] == 0)  //����k��pancake����
				continue;
			longestemp = k;
			if (isfind == false)
			{
				zuidazhi = longestemp; isfind = true;
			}
			if (longestemp <= 3) break;
			if (longestemp >= 2 * TongJi[longestemp] + 2) //����
			{
				minute += TongJi[longestemp];
				TongJi[longestemp / 2] += TongJi[longestemp];
				TongJi[longestemp - longestemp / 2] += TongJi[longestemp];
				TongJi[longestemp] = 0;
			}
			else
			{
				next = longestemp; 
				while ((--next)>=1&&TongJi[next] == 0);
				jb = longestemp - next;
				//cout << jb;
				minute += jb;
				if (next!=0)
					TongJi[next] += TongJi[longestemp];
				TongJi[longestemp] = 0;
				longestemp = next;
				
				

			}
		}
		minute += longestemp;
		if (zuidazhi < minute)
			minute = zuidazhi;
		output << "Case #" << i << ": " << minute << endl;
	}
	return 0;
}