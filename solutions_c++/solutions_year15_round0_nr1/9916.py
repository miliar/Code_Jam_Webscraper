#include <iostream>
#include <string>
#include <fstream>
using namespace std;
int T,N,KQ,dem;
string S;

int main()
{
	ifstream Nhap("A-small-attempt1.in");
	ofstream Xuat("Sochan.out");
	Nhap>>T;
	dem=0;
	while (T>=1)
	{
		dem++;
		T--;
		Nhap>>N>>S;
		int songuoidd=0;
		KQ=0;
		for (int i=0;i<=N;i++)
		{
			int a=(int) S[i]-48;
			if (songuoidd>=i) songuoidd+=a;
			else if (a!=0)
			{
				KQ+=i-songuoidd;
				songuoidd+=KQ+a;
			}
		}
		Xuat<<"Case #"<<dem<<": "<<KQ<<endl;
	}
	Nhap.close();
	Xuat.close();
}
