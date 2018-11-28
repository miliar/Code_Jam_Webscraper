#include <iostream>
#include <string>
#include <vector>
#include <math.h>
#include <sstream>
#include <fstream>
#include <cctype>
#include <stdlib.h>
#include <iomanip>

using namespace std;

int CharToNumber (char Text)
{                              
	return Text-'0';
}


int main()
{
	freopen("A-small-attempt0.in","r",stdin);
    freopen("solution.out","w",stdout);
	
	int T;
	int no=0;

	cin>>T;
	while(T--)
	{
		no++;

		int s;
		int peopleCnt=0;
		int minNo=0;
		string line;
		cin>>s;
		cin>>line;
		for(int i=0;i<=s;i++)
		{
			char p=line[i];
			int pn=CharToNumber(p);
			if(peopleCnt<i && pn!=0)
			{
				minNo+=(i-peopleCnt); 
				peopleCnt+=minNo;
			}
			peopleCnt+=pn;
		}
		cout<<"Case #"<<no<<": "<<minNo<<endl;
		
	}
	return 0;
}
