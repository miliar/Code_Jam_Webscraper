#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
int T, x, a[4][4], y, b[4][4];

void doit(){
	int ct = 0, tg = 0;
	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			if (a[x][i] == b[y][j]){
				ct++;
				tg = a[x][i];
			}
	if (ct == 0){
		cout<<"Volunteer cheated!"<<endl;
	}
	else if (ct == 1){
		cout<<tg<<endl;
	}
	else{
		cout<<"Bad magician!"<<endl;
	}	
}

int main(){
	freopen("A0.in","r",stdin);
	freopen("A0.out","w",stdout);
	cin>>T;
	for (int cs = 1; cs <= T; cs ++){
		cin >> x;
		x--;
		for (int i = 0; i < 4; i ++)
			for (int j = 0; j < 4; j++)
				cin >> a[i][j];
		cin >> y;
		y--;
		for (int i = 0; i < 4; i ++)
			for (int j = 0; j < 4; j++)
				cin >> b[i][j];
		cout << "Case #" << cs <<": ";
		doit();
	}
	return 0;
}
