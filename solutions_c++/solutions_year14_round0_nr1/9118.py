#include"iostream"
using namespace std;
#include"fstream"
void main()
{
	fstream file,out;
	file.open("A-small-attempt1.in",ios::in);
	if(file.fail()) cout<<"can not open file A-small-attempt1.in";
	else
	{
		int a,b,c,d,dem=0;
		int mang[4];
		out.open("output.txt",ios::out);
		file>>a;//a la so test case
		for(int i=1;i<=a;i++)
		{
			file>>b;//so hang cua quan bai duoc chon sap xep lan 1
			for(int j=1;j<=4;j++)//doc ma tran 4 4
				for(int k=0;k<4;k++)
				{
					if(j==b) file>>mang[k];//dua cac gia tri o hang co quan bai duoc chon vao mang
					else file>>c;
				}
			file>>b;//so hang cua quan bai duoc chon sap xep lan 2
			for(int j=1;j<=4;j++)//doc ma tran 4 4
				for(int k=0;k<4;k++)
				{
					file>>c;
					if(j==b) 
					{
						for(int m=0;m<4;m++) 
							if(c==mang[m]) //so sanh de tim quan bai trung
							{
								dem++;//dem so quan bai trung
								d=c;//gan de xuat ra quan bai trung neu dem=1
							}
					}
				}
			if(dem==1) out<<"Case #"<<i<<": "<<d<<endl;//1 quan bai trung xuat ra dung quan bai do
			else if(dem==0) out<<"Case #"<<i<<": Volunteer cheated!"<<endl;//truong hop con lai xuat ra Volunteer cheater
			else if((dem==4)||(dem==2)||(dem==3)) out<<"Case #"<<i<<": Bad magician!"<<endl;//4 quan bai trung xuat ra  Bad magician
			dem=0;//reset bien dem de tiep tuc chay voi test case khac
		}
		file.close();
		out.close();
	}
}