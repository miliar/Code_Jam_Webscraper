#include <iostream>
#include <string.h>
#include <fstream>
#include <algorithm>
#include <vector>

using namespace std;

int dinner;
int D[1001];
int cache[1000];

int compare(const void* one, const void* two)
{
	return *(int *)two - *(int *)one;
}

bool myfunction (int i,int j) { return (i>j); }


int pancakes(vector<int> v)
{
	int L=v.size();
	if(L==0)
		return 0;

	sort(v.begin(),v.end(),myfunction);

	int largest=v[0];
	int res=v[0];
	for (int i = 2; i <= largest/2; i++)
	{
		if(v[0]%i == 0)
		{
			int tmp=v[0];
			v.push_back(v[0]/i);
			v[0]=v[0] - v[0]/i;
			res=min(res,pancakes(v)+1);
			v.pop_back();
			v[0]=tmp;
		}
	}

	for (int i = 0; i < L; i++)
	{
		v[i]--;
		if(v[i]==0)
		{
			for (int j = 0; j < L-i; j++)	v.pop_back();
			break;
		}
	}

	return min(res,pancakes(v) + 1);
}


int main()
{
	ifstream OpenFile("B-small-attempt6.txt");
	ofstream SaveFile("output6.txt");
	int T;
	OpenFile>>T;
	for (int t = 0; t < T; t++)
	{
		vector<int> v;
		OpenFile>>dinner;
		memset(D,0,dinner);
		int in;
		for (int i = 0; i < dinner; i++){

			OpenFile>>in;
			v.push_back(in);
		}
		int res=pancakes(v);
		SaveFile<<"Case #"<<t+1<<": "<<res<<endl;
	}
	OpenFile.close();
	SaveFile.close();
	return 0;
}
