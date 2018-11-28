#include <iostream>
#include <vector>
#include <string>
using namespace std;
int main(){
	int T;
	cin >> T;
	for(int t = 1 ; t <= T ; t++){
		char a[4][4];
		for(int i = 0 ; i < 4 ; i++)
			for(int j = 0 ; j < 4 ; j++)
				cin >> a[i][j];
		int ans = 0;
		for(int i = 0 ; i < 4 ; i++)
		{
			bool can = true;
			for(int j = 0 ; j < 4 ; j++)
				if(a[i][j] == 'X' || a[i][j] == '.')
					can = false;
			if(can)
				ans = 1;
			can = true;
			for(int j = 0 ; j < 4; j++)
				if(a[i][j] == 'O' || a[i][j] == '.')
					can = false;
			if(can)
				ans = -1;
		}
		for(int i = 0 ; i < 4 ; i++)
		{
			bool can = true;
			for(int j = 0 ; j < 4 ; j++)
				if(a[j][i] == 'X' || a[j][i] == '.')
					can = false;
			if(can)
				ans = 1;
			can = true;
			for(int j = 0 ; j < 4; j++)
				if(a[j][i] == 'O' || a[j][i] == '.')
					can = false;
			if(can)
				ans = -1;
		}
		bool can = true;
		for(int i = 0 ;	i < 4 ; i++)
			if(a[i][i] == 'O' || a[i][i] == '.')
				can = false;
		if(can)
			ans = -1;
		can = true;
		for(int i = 0 ;	i < 4 ; i++)
			if(a[i][i] == 'X' || a[i][i] == '.')
				can = false;
		if(can)
			ans = 1;
		can = true;
		for(int i = 0 ;	i < 4 ; i++)
			if(a[i][3 - i] == 'O' || a[i][3 - i] == '.')
				can = false;
		if(can)
			ans = -1;
		can = true;
		for(int i = 0 ;	i < 4 ; i++)
			if(a[i][3 - i] == 'X' || a[i][3 - i] == '.')
				can = false;
		if(can)
			ans = 1;
		bool fill = true;
		for(int i = 0 ; i < 4 ; i++)
			for(int j = 0 ; j < 4 ; j++)
				if(a[i][j] == '.')
					fill = false;
		cout << "Case #" << t << ": ";
		if(ans == 0 && fill)
			cout << "Draw";
		else if(ans == 0 && !fill)
			cout << "Game has not completed";
		else if(ans == 1)
			cout << "O won";
		else
			cout << "X won";
		cout << endl;
	}
}
