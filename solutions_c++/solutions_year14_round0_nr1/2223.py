#include <iostream>
#include <set>
#include <vector>
#include <string>
using namespace std;

vector<vector<int> > v1(4),v2(4);
int answ1,answ2;

void ClearVectors()
{
	v1.clear();
	v1.resize(4);
	for(int i=0;i<4;++i)
		v1[i].resize(4);

	v2.clear();
	v2.resize(4);
	for(int i=0;i<4;++i)
		v2[i].resize(4);
}

void ReadTest()
{
	cin>>answ1;
	for(int i=0;i<4;++i)
		for(int j=0;j<4;++j)
		{
			cin>>v1[i][j];
		}
	cin>>answ2;
	for(int i=0;i<4;++i)
		for(int j=0;j<4;++j)
		{
			cin>>v2[i][j];
		}
}

string GetAnswerForTest()
{
	set<int> st1,st2;
	st1.clear();
	st2.clear();
	--answ1;
	--answ2;
	for(int i=0;i<4;++i)
		st1.insert(v1[answ1][i]);
	for(int i=0;i<4;++i)
		st2.insert(v2[answ2][i]);

	vector<int> answ;
	for(int i=1;i<17;++i)
	{
		if(st1.find(i)!=st1.end() && st2.find(i)!=st2.end())
			answ.push_back(i);
	}

	if(answ.size()==1)
		return std::to_string(answ[0]);
	else
		if(answ.size()>1)
			return "Bad magician!";
		else
			return "Volunteer cheated!";
}



int main()
{
	freopen("D:\\in.txt","r",stdin);
	freopen("D:\\out.txt","w",stdout);

	int T;
	cin>>T;
	for(int i=0;i<T;++i)
	{
		ClearVectors();
		ReadTest();
		string A=GetAnswerForTest();
		cout<<"Case #"<<i+1<<": "<<A<<endl;
	}
	return 0;
}
