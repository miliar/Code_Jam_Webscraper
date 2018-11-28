/*
 * Counting_Sheep.cpp
 *
 *  Created on: Apr 9, 2016
 *      Author: neeraj
 */

#include<iostream>

using namespace std;
typedef long long int lli;

void updateFreq(lli num, int freq[])
{
	while(num)
	{
		freq[num%10]++;
		num=num/10;
	}
}

bool allSeen(int freq[])
{
	for(int i=0;i<10;i++)
	{
		if(freq[i]==0)
			return false;
	}
	return true;
}

int main()
{
	int t;

	FILE *fin = fopen("/Users/neeraj/Documents/codeblocks/Progs New/spoj/GoogleCodeJam/A-large.in","r");
	FILE *fout = fopen("/Users/neeraj/Documents/codeblocks/Progs New/spoj/GoogleCodeJam/A-large.out","w+");
	int c=0;
	fscanf(fin,"%d",&t);
	while(t--)
	{
		c++;
		lli n;
		fscanf(fin,"%lld",&n);
		//cout<<n<<" ";
		int freq[10];

		for(int i=0;i<10;i++)
			freq[i]=0;

		lli mult=1;

		while(1)
		{
			lli newNum = mult*n;
		//	cout<<newNum<<" ";
			if(newNum==0)
			{
				fprintf(fout,"Case #%d: %s\n",c,"INSOMNIA");
				break;
			}
			updateFreq(newNum,freq);
			if(allSeen(freq))
			{
				fprintf(fout,"Case #%d: %lld\n",c,newNum);
				break;
			}
			mult++;
		}
	}
	return 0;
}
