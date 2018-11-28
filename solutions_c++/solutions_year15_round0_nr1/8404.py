#include <bits/stdc++.h>
#include <fstream>

using namespace std;

int main()
{
	int t;;
	scanf("%d",&t);
	int s,count,sum;
	ofstream outputFile;
	outputFile.open("out.txt");

	for (int i = 0; i < t; ++i)
	{
		count=0;
		sum=0;
		scanf("%d",&s);	
		char c[s+1];
		scanf("%s",c);
		int num[s+1];
		for(int j=0;j<=s;j++)
		{
			num[j]=c[j]-'0';
			if(j>sum && num[j]!=0)
			{
				count+=j-sum;
				sum+=j-sum;
			}
			sum+=num[j];
		}
		outputFile << "Case #" << (i+1) << ": " <<count << "\n";
	}
	outputFile.close();
	return 0;
}