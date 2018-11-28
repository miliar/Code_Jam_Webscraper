#include <iostream>
#include <stdio.h>
using namespace std;

int main() {
	int t,flag=0,chk;
	scanf("%d", &t);
	chk=t;
	while(t--)
	{
		flag = 0;
		int x,r,c;
		scanf("%d %d %d",&x,&r,&c);
		if(r%x!=0 && c%x!=0)
			flag = 0;
		else
		{
			if(r>x-2 && c>x-2)
				flag = 1;
			else
				flag = 0;
		}
		if(flag == 0)
		{
			printf("Case #%d: RICHARD\n",chk-t);
		}
		else
			printf("Case #%d: GABRIEL\n",chk-t);
	}
	return 0;
}