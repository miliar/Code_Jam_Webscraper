#include <bits/stdc++.h>
using namespace std;
int main(){
	int t;
	scanf("%d",&t);
	for (int j = 1; j <=t; ++j)
	{
		int n;
		scanf("%d",&n);
		char cad[n+2]; 

		scanf("%s",&cad);
		int contar=0;
		int suma=((int)cad[0]-(int)'0');	
		for (int i = 1; i <=n; ++i)
		{
			if (cad[i]!='0'&&suma<i)
			{
				contar+=(i-suma);
				suma+=contar;
			}
			suma+=((int)cad[i]-(int)'0');
		}
		printf("Case #%d: %d\n",j,contar );
	}

	return 0;
}