//#include <iostream>
//#include <fstream>
//#include <streambuf>
//#include <iomanip>
//#include <time.h>
//
//using namespace std;
//
//int main()
//{
//	ifstream ifs("B-large.in");
//	ofstream ofs("B-large.out");
//	int T;
//	double C, F, X, f, time;
//
//	streambuf *cin_backup = cin.rdbuf();
//	cin.rdbuf(ifs.rdbuf());
//
//	cin >> T;
//	for (int i = 0; i < T; i++)
//	{
//		cin >> C >> F >> X;
//
//		f = 2.0;
//		time = 0.0;
//		while (C/f+X/(f+F) < X/f)
//		{
//			time += C/f;
//			f += F;
//		}
//
//		time += X/f;
//		ofs << "Case #" << i+1 << ":" << " " << fixed << setprecision(7) << time << endl;;
//	}
//
//	cin.rdbuf(cin_backup);
//
//	//clock_t start = clock();
//	//clock_t end = clock();
//	//cout << end-start;
//
//	system("pause");
//}

#include <iostream>
#include <stdlib.h>
#include <fstream>
using namespace std;
int main()
{
	ifstream fin("A-small-attempt0.in");
	ofstream fout("A-small-attempt0.out",ofstream::out | ofstream::app);
	cin.rdbuf(fin.rdbuf());
	int T;
	cin>>T;
	for(int i=0;i<T;i++)
	{
		int r1,r2,num=0,choose;
		int a[4][4];
		int b[4][4];
		cin>>r1;
		for(int j=0;j<4;j++)
		{
			cin>>a[j][0]>>a[j][1]>>a[j][2]>>a[j][3];
		}
		cin>>r2;
		for(int j=0;j<4;j++)
		{
			cin>>b[j][0]>>b[j][1]>>b[j][2]>>b[j][3];
		}
		for(int k=0;k<4;k++)
		{
			for(int m=0;m<4;m++)
			{
				if(a[r1-1][k]==b[r2-1][m])
				{
					num++;
					choose=a[r1-1][k];
				}
			}
		}
		if(num==0)fout<<"Case #"<<i+1<<": "<<"Volunteer cheated!"<<endl;
		else if(num==1)fout<<"Case #"<<i+1<<": "<<choose<<endl;
		else if(num>1)fout<<"Case #"<<i+1<<": "<<"Bad magician!"<<endl;
	}
	fin.close();
	fout.close();
	system("pause");
	return 0;
}
