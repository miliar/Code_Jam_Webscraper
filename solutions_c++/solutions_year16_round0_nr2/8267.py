#include <cstdio>
//#include <string>
#include <iostream>
#include <cstring>
using namespace std;
char s[105];
int TestCase;
int main(){
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	scanf("%d",&TestCase);
	for(int O=1; O<=TestCase; O++){
		scanf("%s", s);
		//printf("%s\n",s)
		int ANS=0;
		int L=(int)strlen(s);
		s[L]='+';
		for(int i=0; i<L; i++)
			if(s[i]!=s[i+1]) ANS++;
		printf("Case #%d: ", O);
		printf("%d\n", ANS);
	}
}
