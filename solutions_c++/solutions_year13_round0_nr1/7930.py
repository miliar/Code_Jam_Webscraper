#include<iostream>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<map>

using namespace std;

#define X "X won"
#define O "O won"
#define D "Draw"
#define N "Game has not completed"


int check (char a[4][4],char d){
	for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				cout<<a[i][j];
			}cout<<"\n";
		}
		
	
	if     ((a[0][0]==d)&&(a[1][1]==d)&&(a[2][2]==d)&&(a[3][3]==d)){cout<<1;return 1;}
	else if(a[0][3]==a[1][2]==a[2][1]==a[3][0]==d){cout<<2;return 1;}
	else if(a[0][1]==a[0][0]==a[0][2]==a[0][3]==d){cout<<3;return 1;}
	else if(a[1][1]==a[1][0]==a[1][2]==a[1][3]==d){cout<<4;return 1;}
	else if(a[2][1]==a[2][0]==a[2][2]==a[2][3]==d){cout<<5;return 1;}
	else if(a[3][1]==a[3][0]==a[3][2]==a[3][3]==d){cout<<6;return 1;}
	else if(a[0][0]==a[1][0]==a[2][0]==a[3][0]==d){cout<<7;return 1;}
	else if(a[0][1]==a[1][1]==a[2][1]==a[3][1]==d){cout<<8;return 1;}
	else if(a[0][2]==a[1][2]==a[2][2]==a[3][2]==d){cout<<9;return 1;}
	else if(a[0][3]==a[1][3]==a[2][3]==a[3][3]==d){cout<<10;return 1;}
	else return 0 ;
	
}

int main()
{   ios_base::sync_with_stdio(false);
	int n;cin>>n;
	while(n>0)	{
		char a[4][4];char b[4][4],d[4][4];int cnt=0;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				
				char c;cin>>c;
				if(c=='.')cnt++;
				a[i][j]=c;//cout<<a[i][j];
				b[i][j]=c;d[i][j]=c;
				if(c=='T'){b[i][j]='X';d[i][j]='O';}
				
			}
		}
		int res1=check(b,'X');
		int res2=check(d,'O');
		cout<<res1<<res2;
		if(res1==1)cout<<X;
    	else if (res2==1)cout<<O;
    	else if (cnt!=0)cout<<N;
    	else cout<<D;cout<<"\n";
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				cout<<b[i][j];
			}cout<<"\n";
		}
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				cout<<d[i][j];
			}cout<<"\n";
		}
		n--;
	}
	system("pause");
	return 0;
}



