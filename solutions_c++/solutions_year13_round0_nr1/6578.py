#include <iostream>
#include <string>

//g++ -o a.exe a.cpp
//./a.exe < A-small-practice.in > A-small-practice.out

using namespace std;
int cases;
int main()
{
	string line1,line2,line3,line4;
	int c1,c2,c3,c4,c5,c6,c7,c8,c9,c10;
	int no[4][4];
	char gridxy[4][4];
	cin >> cases;
	for (int c=1; c<=cases; c++)
	{
		cin >> line1 >> line2 >> line3 >> line4;
		for (int x=0;x<=3; x++){
		gridxy [x][0]=line1[x];
		gridxy [x][1]=line2[x];
		gridxy [x][2]=line3[x];
		gridxy [x][3]=line4[x];
	}
	for (int x=0;x<=3;x++){
		for (int y=0; y<=3; y++){
			if (gridxy[x][y]=='X'){
				no[x][y]=2;
			}
			else if (gridxy[x][y]=='O'){
				no[x][y]=3;
			}
			else if (gridxy[x][y]=='T'){
				no[x][y]=5;
			}
			else {
				no[x][y]=7;
			}
			
		}
	}
	c1=1;
	c2=1;
	c3=1;
		c4=1;
		c5=1;
		c6=1;
		c7=1;
		c8=1;
		c9=1;
		c10=1;
	for (int x=0;x<=3;x++){
		c1=c1*no[x][0];
		c2=c2*no[x][1];
		c3=c3*no[x][2];
		c4=c4*no[x][3];
		c5=c5*no[0][x];
		c6=c6*no[1][x];
		c7=c7*no[2][x];
		c8=c8*no[3][x];
		}
	
		c9=no[0][0]*no[1][1]*no[2][2]*no[3][3];
		c10=no[0][3]*no[1][2]*no[2][1]*no[3][0];
		
		if (c1==40||c1==16||c2==40||c2==16||c3==40||c3==16||c4==40||c4==16||c5==40||c5==16||c6==40||c6==16||c7==40||c7==16||c8==40||c8==16||c9==40||c9==16||c10==40||c10==16)
		{
			cout << "Case #"<<c<<": X won"<< endl;
		}
		
		else if (c1==81||c1==135||c2==81||c2==135||c3==81||c3==135||c4==81||c4==135||c5==81||c5==135||c6==81||c6==135||c7==81||c7==135||c8==81||c8==135||c9==81||c9==135||c10==81||c10==135)
		{
			cout << "Case #"<<c<<": O won"<< endl;
		}
		else if (c1%7==0||c2%7==0||c3%7==0||c4%7==0||c5%7==0||c6%7==0||c7%7==0||c8%7==0||c9%7==0||c10%7==0)
		{
			cout << "Case #"<<c<<": Game has not completed"<< endl;
		
		}
		else {cout << "Case #"<<c<<": Draw"<< endl;
		}		
	}
	return 0;
}

