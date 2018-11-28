#include<iostream>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<map>
#include<fstream>

using namespace std;

#define X "X won"
#define O "O won"
#define D "Draw"
#define N "Game has not completed"


int check (int a[4][4],int d){
/*	for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				cout<<a[i][j];
			}cout<<"\n";
		}
		*/
		
	
	if     ((a[0][0]==d)&&(a[1][1]==d)&&(a[2][2]==d)&&(a[3][3]==d)){cout<<1;return 1;}
	else if((a[0][3]==d)&&(a[1][2]==d)&&(a[2][1]==d)&&(a[3][0]==d)){cout<<2;return 1;}
	else if((a[0][1]==d)&&(a[0][0]==d)&&(a[0][2]==d)&&(a[0][3]==d)){cout<<3;return 1;}
	else if((a[1][1]==d)&&(a[1][0]==d)&&(a[1][2]==d)&&(a[1][3]==d)){cout<<4;return 1;}
	else if((a[2][1]==d)&&(a[2][0]==d)&&(a[2][2]==d)&&(a[2][3]==d)){cout<<5;return 1;}
	else if((a[3][1]==d)&&(a[3][0]==d)&&(a[3][2]==d)&&(a[3][3]==d)){cout<<6;return 1;}
	else if((a[0][0]==d)&&(a[1][0]==d)&&(a[2][0]==d)&&(a[3][0]==d)){cout<<7;return 1;}
	else if((a[0][1]==d)&&(a[1][1]==d)&&(a[2][1]==d)&&(a[3][1]==d)){cout<<8;return 1;}
	else if((a[0][2]==d)&&(a[1][2]==d)&&(a[2][2]==d)&&(a[3][2]==d)){cout<<9;return 1;}
	else if((a[0][3]==d)&&(a[1][3]==d)&&(a[2][3]==d)&&(a[3][3]==d)){cout<<10;return 1;}
	else return 0 ;
	
}

int main()
{   ios_base::sync_with_stdio(false);
	fstream f("new.txt",ios::in);
	fstream fo("new1.txt",ios::out);int ko=1;
	int n;f>>n;
	while(n>0)	{
		char a[4][4];int b[4][4],d[4][4];int cnt=0;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				
				char c;f>>c;
				if(c=='.')cnt++;
				a[i][j]=c;//cout<<a[i][j];
				int x;
				if(c=='X')x=1;
				else if(c=='O')x=2;
				else  if(c=='.')x=0;
				b[i][j]=x;d[i][j]=x;
				if(c=='T'){b[i][j]=1;d[i][j]=2;}
				
			}
		}
		int res1=check(b,1);
		int res2=check(d,2);
		fo<<"Case #"<<ko<<": ";ko++;
		//cout<<res1<<res2;
		if(res1==1)fo<<X;
    	else if (res2==1)fo<<O;
    	else if (cnt!=0)fo<<N;
    	else fo<<D;fo<<"\n";
		n--;
	}
	//system("pause");
	return 0;
}



