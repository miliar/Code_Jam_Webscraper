#include<iostream>
#include<string>
#include<cmath>
#include<algorithm>
#include<iomanip>
#include<map>
#include<stdio.h>
#include<vector>
#include<string.h>
#include<set>
#include<stack>
#include<queue>
#include<sstream>
#include<fstream>
using namespace std;
vector<string> generatePalindromes()
{
	vector<string> palins;
	map<int,vector<string> > hopa;
	for (int i = 1; i < 14 ; i++)
	{
		string palin;
		palin.resize(i);
		vector<string> temp;
		for (int j = 0; j < 10 ; j++)
		{
			palin[0]=palin[i-1]=j+'0';
			temp.push_back(palin);
			if(i<3&&j!=0)
			{
				palins.push_back(palin);
			}
		}
		if(i>2)
		{
			for (int j = 0; j < temp.size() ; j++)
			{
				string data = temp[j];
				
				
				for (int m = 0; m < hopa[i-2].size() ; m++)
				{
					data.replace(1,i-2,hopa[i-2][m]);
					if(data[0]!='0')
						palins.push_back(data);
					hopa[i].push_back(data);
				}
				
			}
		}
		else
		{
			hopa[i]=temp;
		}
		
	}
	return palins;
}
bool isPalindrome(long long number)
{
	string numToWord;
	ostringstream os;
	os<<number;
	numToWord = os.str();
	if(numToWord.size()==1)
		return true;
	for (int i = 0; i < numToWord.size()/2 ; i++)
	{
		if(numToWord[i]!=numToWord[numToWord.size()-1-i])
			return false;
	}
	return true;
}
int main()
{
	ifstream cin("C-large-1.in");
	ofstream cout("C-large.out");
	//generatePalindromes();
	vector<long long> squarePalin(39);
	squarePalin[0]=1;
	squarePalin[1]=4;
	squarePalin[2]=9;
	squarePalin[3]=121;
	squarePalin[4]=484;
	squarePalin[5]=10201;
	squarePalin[6]=12321;
	squarePalin[7]=14641;
	squarePalin[8]=40804;
	squarePalin[9]=44944;
	squarePalin[10]=1002001;
	squarePalin[11]=1234321;
	squarePalin[12]=4008004;
	squarePalin[13]=100020001;
	squarePalin[14]=102030201;
	squarePalin[15]=104060401;
	squarePalin[16]=121242121;
	squarePalin[17]=123454321;
	squarePalin[18]=125686521;
	squarePalin[19]=400080004;
	squarePalin[20]=404090404;
	squarePalin[21]=10000200001;
	squarePalin[22]=10221412201;
	squarePalin[23]=12102420121;
	squarePalin[24]=12345654321;
	squarePalin[25]=40000800004;
	squarePalin[26]=1000002000001;
	squarePalin[27]=1002003002001;
	squarePalin[28]=1004006004001;
	squarePalin[29]=1020304030201;
	squarePalin[30]=1022325232201;
	squarePalin[31]=1024348434201;
	squarePalin[32]=1210024200121;
	squarePalin[33]=1212225222121;
	squarePalin[34]=1214428244121;
	squarePalin[35]=1232346432321;
	squarePalin[36]=1234567654321;
	squarePalin[37]=4000008000004;
	squarePalin[38]=4004009004004;
	int T;
	cin>>T;
	vector<int> palins;
	int k=1;
	while(T--)
	{
		long long A,B;
		cin>>A>>B;
		int index = upper_bound(squarePalin.begin(),squarePalin.end(),A)-squarePalin.begin();
		index = max(index-1,0);
		int counter = 0;
		while(index<squarePalin.size()&&squarePalin[index]<=B)
		{
			long long y = squarePalin[index];
			if(y>=A)
				counter++;
			index++;
		}
		cout<<"Case #"<<k++<<": "<<counter<<endl;
	}
	return 0;
}