#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

int main()
{
	// freopen("input.txt","r",stdin);
	int testCase=0;
	scanf("%d",&testCase);

	for(int i=1;i<=testCase;i++){

		int shyMax=0;
		scanf("%d",&shyMax);

		string shyLevelOfAudi;
		cin>>shyLevelOfAudi;

		int totalAudi=0;
		int invite=0;

		for(int j=0;j<=shyMax;j++){

			if((shyLevelOfAudi[j]-'0')!=0 && totalAudi<j)
			{
				invite=invite+(j-totalAudi);
				totalAudi=totalAudi+invite;
			}

			totalAudi=totalAudi+(shyLevelOfAudi[j]-'0');
		}

		printf("Case #%d: %d\n",i,invite);

	}

	return 0;
}



