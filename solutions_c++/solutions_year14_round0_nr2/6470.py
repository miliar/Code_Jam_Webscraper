#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <iterator>
#include <iomanip>
#include <fstream>
using namespace std;
int main()
{
	ifstream in("in.in");
	ofstream out("out.out");
	long float C, F, X;
	int T;
	in >> T;
	int loop = 1;
	while (T--)
	{
		in >> C >> F >> X;

		long float gainper = 2;//ÿ�������
		long float farmtime = 0;//��ũ���Ļ���
		long float pretime = 0;//��n-1ũ���ﵽĿ��ʱ��
		long float nowtime = 0;//���ڵ�ʱ��

		
		for (long int nfarm = 0; nfarm<100000000; nfarm++)//��ũ��
		{
			nowtime = farmtime + X / gainper;//����Ҫ����ʱ��
			if (nowtime>pretime && nfarm != 0)
			{
				out << "Case #" << loop << ": " << fixed << setprecision(7) << pretime << endl;
				break;
			}
			farmtime += C / gainper;
			gainper += F;//��������
			pretime = nowtime;
		}
		loop++;
	}
	//getchar();
	//getchar();
}