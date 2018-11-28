#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <iostream>

using namespace std;
int main()
{
	int n,m,tmp;
	int chk=0;
	string str;
	scanf("%d",&n);
	for(int i=0; i<n; i++)
	{
		printf("Case #%d: ",i+1);
		scanf("%d", &m);
		if(m==0){
			printf("INSOMNIA\n");
			continue;
		}
		tmp=m;
		chk=0;
		while(chk != 0x3ff){
			str = to_string(tmp);
			for(int j=0; j<str.length(); j++)
				chk |= (1<<(str.at(j)-'0'));
			tmp += m;
		}
		cout << str << endl;
	}
	return 0;
}