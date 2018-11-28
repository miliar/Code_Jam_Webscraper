#include <bits/stdc++.h>
#define loop(i, a, b) for(i=a; i<b; i++)
#define rev(i, a, b) for(i=a; i>=b; i--)
#define SET(x, a) memset(x, a, sizeof(x))
#define PI (acos(-1))
#define READ(fi) freopen(fi, "r", stdin)
#define WRITE(fi) freopen(fi, "w", stdout)
#define x first
#define y second
#define pb push_back
#define pf push_front
#define LIM 105

using namespace std;

typedef long long large;
typedef pair<int,int> ii;
typedef pair<int,ii> tri;
typedef deque<int> di;
typedef deque<ii> dii;

char s[LIM], tm[LIM];

char flip(char c){
	if (c=='+') return '-';
	return '+';
}

int main(void){
	int nc, caso;
	int i, n, a, b, c, j, ct;
	//READ("B.txt");
	scanf("%d", &nc);
	loop(caso, 0, nc){
		scanf("%s", s);
		//puts(s);
		n=strlen(s);
		ct=0;
		rev(i, n-1, 0){
			if (s[i]!='+'){
				if (s[0]=='+'){
					a=b=c=0;
					loop(j, 0, i+1){
						if (s[j]=='-'){
              if (a>b){
              	c=j-1;
								b=a;
              }
              a=0;
						}
						else a++;
					}
					reverse(s, s+c+1);
					loop(j, 0, c+1) s[j]=flip(s[j]);
					i++;
				}else{
					reverse(s, s+i+1);
					loop(j, 0, i+1) s[j]=flip(s[j]);
				}
				ct++;
				//puts(s);
			}
		}
		printf("Case #%d: %d\n", caso+1, ct);
	}
	return 0;
}

