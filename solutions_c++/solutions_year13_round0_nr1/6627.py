#include<iostream>
#include<cstdio>
using namespace std;
char check(int b[][4]){
	int i;
	for(i=0;i<4;i++){
		if((b[i][0] == 1 && b[i][1] == 3 ) || b[i][1] == 4)
			return 'X';
		else if(( b[i][0] == 1 && b[i][2] == 3 ) || b[i][2] == 4)
			return 'O';
	}

			
}
char diag(char a[][4]){
	int i,j = 3;
	int cnX=0,cnT=0,cnO=0;
	for(i=0;i<4;i++){
		if(a[i][i] == 'X')
			cnX++;
		else if(a[i][i] == 'O')
			cnO++;
		else if(a[i][i] == 'T')
			cnT++;
	}
	if((cnX == 3 && cnT == 1 ) || cnX == 4)
		return 'X';
	else if ((cnO == 3 && cnT == 1)|| cnO == 4)
		return 'O';
	cnX=cnT=cnO=0;
	for(i=0;i<4;i++){
		if(a[i][j] == 'X')
			cnX++;
		else if(a[i][j] == 'O')
			cnO++;
		else if(a[i][j] == 'T')
			cnT++;
		j--;
	}
	if((cnX == 3 && cnT == 1 ) || cnX == 4 )
		return 'X';
	else if ((cnO == 3 && cnT == 1)|| cnO == 4)
	       	return 'O';

}

int main()
{	int test;
	int t;
	char a[4][4];
	int i;
	int j;
	cin >> test;
	for(t=1;t<=test;t++){
		int b[4][4]={0};
		int c[4][4]={0};
		int cnD = 0;

		
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				cin >> a[i][j];
				if (a[i][j] == '.')
					cnD++;
				if(a[i][j] == 'T')
					b[i][0]++;
				else if(a[i][j] == 'X')
					b[i][1]++;
				else if(a[i][j] == 'O')
					b[i][2]++;
				else
					b[i][3]++;
			}
		}
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				if(a[j][i] == 'T')
					c[i][0]++;
				else if(a[j][i] == 'X')
					c[i][1]++;
				else if(a[j][i] == 'O')
					c[i][2]++;
				else
					c[i][3]++;
			}
		}
		char m;
		m = check(b);
		if (m == 'X' || m == 'O')
			cout << "Case #" << t <<": " << m <<" won" << endl;
		else{
			m = check(c);
			if(m == 'X' || m == 'O')
				cout << "Case #" << t << ": " << m << " won" << endl;
			else{
				m = diag(a);
				if(m == 'X' || m == 'O')
					cout << "Case #" << t << ": "<< m <<" won" << endl;
				else{
					if(cnD == 0)
						cout << "Case #" << t << ": " <<  "Draw" << endl;
					else 
						cout << "Case #" << t << ": " <<  "Game has not completed" << endl;
				}	
			}
				
		}
		
	}
	return 0;
}

