#include <iostream>
#include <cstdio>
#include <string>
#include <map>

using namespace std;

int T;
int L,X;
string Line;

map<char,int> M;

string Matrix[4][4];

bool XXX0(string& s)/////////////////////////
{
	int pst = 1;

	while(s.size()>1)
	{

		char x = s[0];
		char y = s[1];

		s.erase(0,2);

		string ans = Matrix[M[x]][M[y]];

		if(s.size() == 0 && ans == "-1" && pst == 1)
			return true;

		if(s.size() > 0)
		{
			if(ans[0] == '-')
			{
				pst *= -1;
				ans.erase(0,1);
			}

			if(ans == "1")
				continue;

			s.insert(0,ans);
		}
	}


	return false;

}

string XXX(string& s)/////////////////////////
{
	int pst = 1;

	if(s.size() == 0)
		return s;

	if(s[0] == '-')
	{
		pst = -1;
		s.erase(0,1);
	}

	while(s.size()>1)
	{

		char x = s[0];
		char y = s[1];

		s.erase(0,2);

		string ans = Matrix[M[x]][M[y]];


			if(ans[0] == '-')
			{
				pst *= -1;
				ans.erase(0,1);
			}

			if(ans == "1")
				continue;

			s.insert(0,ans);
	}


	if(pst == -1)
	{
		string tmp = "-";
		s.insert(0,tmp);
	}

	return s;

}

bool Solve()///////////////////////////////
{
	for(int t1 = 1;t1<Line.size();t1++)
	{
		string s1 = Line.substr(0,t1);

		if(XXX(s1) != "i")
			continue;

		for(int t2 = t1+1;t2<Line.size();t2++)
		{
			
			string s2 = Line.substr(t1,t2-t1);
			string s3 = Line.substr(t2,Line.size()-t2);

			string ss2 = XXX(s2);
			string ss3 = XXX(s3);

			if(ss2 == "j" && ss3 == "k")
				return true;
			
		}
	}

	return false;
}

void Init()//////////////////////////////////
{
	while(!M.empty())
		M.clear();

	M['1'] = 0;
	M['i'] = 1;
	M['j'] = 2;
	M['k'] = 3;

	Matrix[0][0] = "1";Matrix[0][1] = "i";
	Matrix[0][2] = "j";Matrix[0][3] = "k";
	
	Matrix[1][0] = "i";Matrix[1][1] = "-1";
	Matrix[1][2] = "k";Matrix[1][3] = "-j";

	Matrix[2][0] = "j";Matrix[2][1] = "-k";
	Matrix[2][2] = "-1";Matrix[2][3] = "i";

	Matrix[3][0] = "k";Matrix[3][1] = "j";
	Matrix[3][2] = "-i";Matrix[3][3] = "-1";



}

int main()////////////////////////////////////
{
	freopen("..\\C-small-attempt2.in","r",stdin);
	freopen("..\\C-small-attempt2.out","w",stdout);

//	freopen("..\\C-large.in","r",stdin);
//	freopen("..\\C-large.out","w",stdout);


	Init();

	int d = 1;

	cin >> T;
	while(T--)
	{
		string s;
		Line = "";

		cin >> L >> X;

		cin >>s;


		for(int i=0;i<X;i++)
			Line += s;

		if(L == 1)
		{
			printf("Case #%d: NO\n",d++);
			continue;
		}

		if(s.size() == 2 && s[0] == s[1])
		{
			printf("Case #%d: NO\n",d++);
			continue;
		}

		string tmp = Line;

		if(!XXX0(tmp))
		{
			printf("Case #%d: NO\n",d++);
			continue;
		}

		if(Solve())
			printf("Case #%d: YES\n",d++);
		else
			printf("Case #%d: NO\n",d++);
	}
	return 0;
}