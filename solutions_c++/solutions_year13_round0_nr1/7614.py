#include <cstdio>
#include <cstring>
using namespace std;

int tests, x, o, t;
char s[5][5];
bool X, O;

int main() {
	scanf("%d", &tests);
	for(int i = 1; i <= tests; i++) {
		X = O = false;
		for(int j = 0; j < 4; j++)
			scanf("%s", s[j]);
		X = O = false;
		for(int j = 0; j < 4; j++) {
			x = o = t = 0;
			for(int k = 0; k < 4; k++) {
				if(s[j][k]=='X')
					x++;
				else if(s[j][k]=='O')
					o++;
				else if(s[j][k]=='T')
					t++;
			}
			if(x==4 || (x==3 && t==1))
				X = true;
			if(o==4 || (o==3 && t==1))
				O = true;
			x = o = t = 0;
			for(int k = 0; k < 4; k++) {
				if(s[k][j]=='X')
					x++;
				else if(s[k][j]=='O')
					o++;
				else if(s[k][j]=='T')
					t++;
			}
			if(x==4 || (x==3 && t==1))
				X = true;
			if(o==4 || (o==3 && t==1))
				O = true;
		}
			x = o = t = 0;
			for(int k = 0; k < 4; k++) {
				if(s[k][k]=='X')
					x++;
				else if(s[k][k]=='O')
					o++;
				else if(s[k][k]=='T')
					t++;
			}
			if(x==4 || (x==3 && t==1))
				X = true;
			if(o==4 || (o==3 && t==1))
				O = true;
			x = o = t = 0;
			for(int k = 0; k < 4; k++) {
				if(s[k][3-k]=='X')
					x++;
				else if(s[k][3-k]=='O')
					o++;
				else if(s[k][3-k]=='T')
					t++;
			}
			if(x==4 || (x==3 && t==1))
				X = true;
			if(o==4 || (o==3 && t==1))
				O = true;
		if(X)
			printf("Case #%d: X won\n", i);
		else if(O)
			printf("Case #%d: O won\n", i);
		else {
			bool dot=false;
			for(int j = 0; j < 4; j++) {
				for(int k = 0; k < 4; k++)
					if(s[j][k]=='.')
						dot = true;
			}
			if(dot)
				printf("Case #%d: Game has not completed\n", i);
			else
				printf("Case #%d: Draw\n", i);
		}
	}
	return 0;
}
