#include <cstdio>
#include <cstring>

using namespace std;

int FlipCake(char input[105]){
	int top=0, bot=strlen(input)-1, cnt=0, tmp;
	
	while( 1 ){
		// positive
		while( bot>=top ){
			if(input[bot]=='-')	break;
			else				bot--;
		}
		tmp = top;
		while( top<=bot ){
			if(input[top]=='-')	break;
			else				top++;
		}
		if( tmp!=top )	++cnt;
		if( top>bot )	break;
		else{
			tmp = top;	top = bot;	bot = tmp + 1;	++cnt;
		}
		// reversed
		while( bot<=top ){
			if(input[bot]=='+')	break;
			else				bot++;
		}
		tmp = top;
		while( top>=bot ){
			if(input[top]=='+')	break;
			else				top--;
		}
		if( tmp!=top )	++cnt;
		if( top<bot )	break;
		else{
			tmp = top;	top = bot;	bot = tmp - 1;	++cnt;
		}
	}
	
	return cnt;
}

int main(void){
	freopen("B-large.in", "r", stdin);
	freopen("b.out", "w", stdout);
	int c, cc=0;
	char input[105];
	
	scanf("%d", &c);
	while( c-- ){
		scanf("%s", input);
		printf("Case #%d: %d\n", ++cc, FlipCake(input));
	}
	
	return 0;
}

