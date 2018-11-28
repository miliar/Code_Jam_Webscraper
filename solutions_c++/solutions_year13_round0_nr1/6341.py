#include<fstream>
using namespace std;

char grid[4][4];
int n;
ifstream fin("input.in");
ofstream fout("output.out");

bool check(char c){
	for(int i=0;i<4;i++){
		int x=0;
		for(int j=0;j<4;j++)if(grid[i][j]==c||grid[i][j]=='T')x++;
		if(x==4)return true;
		x=0;
		for(int j=0;j<4;j++)if(grid[j][i]==c||grid[j][i]=='T')x++;
		if(x==4)return true;
	}
	int x=0;
	for(int i=0;i<4;i++)if(grid[i][i]==c||grid[i][i]=='T')x++;
	if(x==4)return true;
	x=0;
	for(int i=0;i<4;i++)if(grid[i][3-i]==c||grid[i][3-i]=='T')x++;
	return x==4;
}

int main(){
	fin>>n;
	for(int k=1;k<=n;k++){
		for(int i=0;i<4;i++)for(int j=0;j<4;j++)fin>>grid[i][j];
		int period=0;
		for(int i=0;i<4;i++)for(int j=0;j<4;j++)if(grid[i][j]=='.')period++;
		fout<<"Case #"<<k<<": ";
		if(check('X'))fout<<"X won\n";
		else if(check('O'))fout<<"O won\n";
		else if(period==0)fout<<"Draw\n";
		else fout<<"Game has not completed\n";
	}
}