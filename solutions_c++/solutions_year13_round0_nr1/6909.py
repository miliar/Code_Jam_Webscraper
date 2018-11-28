#include <iostream>
#include <string>
#include <cmath>
using namespace std;

string s; 
const int MAXN = 4; 
int r, ti, tj, a, b, ans, tests, test, Time, n, data; 
char ch[MAXN][MAXN]; 
char x = 'X'; 
char o = 'O'; 
char d = '.';  
char t = 'T';

int min(int a, int b){ return a < b ? a : b; }

int main(){
    freopen("1.in","r",stdin); 
    freopen("1.out","w",stdout);

    scanf("%d",&tests);
     
    for (test = 1; test <= tests; ++test){
        scanf("%d", &n); 
        ti = -1; 
        for (int i = 0; i < 4; ++i)
        {
        	for (int j = 0; j < 4; ++j)
        	{
        		scanf("%c", &ch[i][j]);
				if (ch[i][j] == t)     
				{
					ti = i; 
					tj = j; 
				}    	
				//printf("%c", ch[i][j]);	
        	}
        	scanf("\n"); 
        	//printf("\n"); 
        }
        
        bool xw = false; 
        bool ow = false; 
        bool nc = false; 
        
        if (ti != -1)
        {
        	ch[ti][tj] = x; 
        }
        
        for (int i = 0; i < 4; ++i)
        {
        	if (ch[i][0] == x && ch[i][1]== x && ch[i][2] == x && ch[i][3] == x) xw = true; 
        	if (ch[0][i] == x && ch[1][i]== x && ch[2][i] == x && ch[3][i] == x) xw = true; 
        }
        if (ch[0][0] == x && ch[1][1]== x && ch[2][2] == x && ch[3][3] == x) xw = true; 
        if (ch[0][3] == x && ch[1][2]== x && ch[2][1] == x && ch[3][0] == x) xw = true; 
        
        if (ti != -1)
        {
        	ch[ti][tj] = o; 
        }
        
        for (int i = 0; i < 4; ++i)
        {
        	if (ch[i][0] == o && ch[i][1]== o && ch[i][2] == o && ch[i][3] == o) ow = true; 
        	if (ch[0][i] == o && ch[1][i]== o && ch[2][i] == o && ch[3][i] == o) ow = true; 
        }
        if (ch[0][0] == o && ch[1][1]== o && ch[2][2] == o && ch[3][3] == o) ow = true; 
        if (ch[0][3] == o && ch[1][2]== o && ch[2][1] == o && ch[3][0] == o) ow = true; 
        
        for (int i = 0; i < 4; ++i)
        {
        	for (int j = 0; j < 4; ++j)
        	{
        		if (ch[i][j] == d) nc = true; 
        	}
        }
        
        if (xw)
        	printf("Case #%d: X won\n", test);          
        else
		if (ow)
        	printf("Case #%d: O won\n", test);          
        else
		if (!nc)
        	printf("Case #%d: Draw\n", test);          
        else
        	printf("Case #%d: Game has not completed\n", test);        
    }   
     
    return 0;  
}
