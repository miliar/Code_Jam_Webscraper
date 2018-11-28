#include <iostream>
#include <fstream>

using namespace std;

ifstream fin("A-small-attempt0.in");
ofstream fout("output.txt");

int n;
char arr[11][11];

int win;

void run1(int x,int y,int cnt, int cht, char ch)
{
	if(x<0 || y<0 || x>=4 || y>=4) return;
	if(cnt == 4){
		if(ch =='X') win = 1;
		if(ch =='O') win = 2;
	}


	if(arr[x+1][y] == ch) run1(x+1,y,cnt+1,cnt,ch);
	else if(arr[x+1][y] == 'T' && cht == 0) run1(x+1,y,cnt+1,1,ch);
}

void run2(int x,int y,int cnt, int cht, char ch)
{
	if(x<0 || y<0 || x>=4 || y>=4) return;
	if(cnt == 4){
		if(ch =='X') win = 1;
		if(ch =='O') win = 2;
	}


	if(arr[x][y+1] == ch) run2(x,y+1,cnt+1,cht,ch);
	else if(arr[x][y+1] == 'T' && cht == 0) run2(x,y,cnt+1,1,ch);

}

void run3(int x,int y,int cnt, int cht, char ch)
{
	if(x<0 || y<0 || x>=4 || y>=4) return;
	if(cnt == 4){
		if(ch =='X') win = 1;
		if(ch =='O') win = 2;
	}


	if(arr[x+1][y+1] == ch) run3(x+1,y+1,cnt+1,cht,ch);
	else if(arr[x+1][y+1] == 'T' && cht == 0) run3(x+1,y+1,cnt+1,1,ch);

	
}

void run4(int x,int y,int cnt, int cht, char ch)
{
	if(x<0 || y<0 || x>=4 || y>=4) return;
	if(cnt == 4){
		if(ch =='X') win = 1;
		if(ch =='O') win = 2;
	}

	if(arr[x-1][y+1] == ch) run4(x-1,y+1,cnt+1,cht,ch);
	else if(arr[x-1][y+1] == 'T' && cht == 0) run4(x-1,y+1,cnt+1,1,ch);

}

void run5(int x,int y,int cnt, int cht, char ch)
{
	if(x<0 || y<0 || x>=4 || y>=4) return;
	if(cnt == 4){
		if(ch =='X') win = 1;
		if(ch =='O') win = 2;
	}

	if(arr[x-1][y-1] == ch) run5(x-1,y-1,cnt+1,cht,ch);
	else if(arr[x-1][y-1] == 'T' && cht == 0) run5(x-1,y-1,cnt+1,1,ch);

}

void run6(int x,int y,int cnt, int cht, char ch)
{
	if(x<0 || y<0 || x>=4 || y>=4) return;
	if(cnt == 4){
		if(ch =='X') win = 1;
		if(ch =='O') win = 2;
	}

	if(arr[x-1][y] == ch) run6(x-1,y,cnt+1,cht,ch);
	else if(arr[x-1][y] == 'T' && cht == 0) run6(x-1,y,cnt+1,1,ch);

}

void run7(int x,int y,int cnt, int cht, char ch)
{
	if(x<0 || y<0 || x>=4 || y>=4) return;
	if(cnt == 4){
		if(ch =='X') win = 1;
		if(ch =='O') win = 2;
	}

	if(arr[x+1][y-1] == ch) run7(x+1,y-1,cnt+1,cht,ch);
	else if(arr[x+1][y-1] == 'T' && cht == 0) run7(x+1,y-1,cnt+1,1,ch);

}

void run8(int x,int y,int cnt, int cht, char ch)
{
	if(x<0 || y<0 || x>=4 || y>=4) return;
	if(cnt == 4){
		if(ch =='X') win = 1;
		if(ch =='O') win = 2;
	}

	if(arr[x][y-1] == ch) run8(x,y-1,cnt+1,cht,ch);
	else if(arr[x][y-1] == 'T' && cht == 0) run8(x,y-1,cnt+1,1,ch);

}

void main()
{
	int comma;
	fin >> n;
	for(int i=0;i<n;i++){
		for(int j=0;j<4;j++){
			fin >> arr[j];
		}
		win = -1;		
		comma = 0;
		for(int k=0;k<4;k++){
			for(int m=0;m<4;m++){
					if(arr[k][m] != '.'){
						run1(k,m,1,0,arr[k][m]);
						run2(k,m,1,0,arr[k][m]);
						run3(k,m,1,0,arr[k][m]);
						run4(k,m,1,0,arr[k][m]);
						run5(k,m,1,0,arr[k][m]);
						run6(k,m,1,0,arr[k][m]);
						run7(k,m,1,0,arr[k][m]);
						run8(k,m,1,0,arr[k][m]);
					}
					else comma++;
			}
		}



		fout << "Case #" << i+1 << ": ";
		if(win==1) fout << "X won" << endl;
		else if(win==2) fout << "O won"<< endl;
		else if(comma == 0) fout << "Draw" << endl;
		else if(comma > 0) fout << "Game has not completed" << endl;
	}
}