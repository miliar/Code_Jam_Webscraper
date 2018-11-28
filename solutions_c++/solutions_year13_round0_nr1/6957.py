#include<iostream>
#include<vector>
#include<cstdlib>
#include<algorithm>
using namespace std;


int cas = 1;
bool who(vector<string>& v,char c)
{

	vector<string>target1;
	if(c == 'X')
	{
		string target[] = {"XXXX","XXXT","XXTX","XTXX","TXXX"};
		for(int i=0;i<5;i++) target1.push_back(target[i]);	
	}
	else
	{
	   string target[] = {"OOOO","OOOT","OOTO","OTOO","TOOO"};		
	   for(int i=0;i<5;i++) target1.push_back(target[i]);
	}

	for(int i=0;i<v.size();i++)
	{
		int cnt =0;
		for(int j=0;j<5;j++)
		if(strstr(&v[i][0],&target1[j][0]) != NULL)
		{
			//cout << target1[j] <<" "<< v[i]<<"\n";
			return 1;
		}
	}
	return 0;
}
bool is_complete(vector<string>&v)
{
	for(int i=0;i<v.size();i++)
	{
		for(int j=0;j<4;j++)
		{
			if('.' == v[i][j] )
				return 1;
		}
	}
	return 0;

}
int main()
{
	freopen("in.in","r",stdin);
	//freopen("out.out","rw",stdout);
	
	int n;
	cin >> n;

	while(n--)
	{
		std::vector<string> v(4);
		std::vector<string> s;
		for(int i=0;i<4;i++)
		{
			cin >> v[i];
			s.push_back(v[i]);
		}
		for(int i=0;i<4;i++)
		{
			string s1="";
			for(int j=0;j<4;j++)
			{
				s1+=v[j][i];
			}
			s.push_back(s1);
		}
		string s1= "";
		s1+=v[0][0];s1+=v[1][1];s1+=v[2][2];s1+=v[3][3];
		s.push_back(s1);
		s1="";
		s1+=v[0][3];s1+=v[1][2];s1+=v[2][1];s1+=v[3][0];
		s.push_back(s1);
		if(who(s,'X'))
			printf("Case #%d: X won\n", cas);
		else if(who(s,'O'))
			printf("Case #%d: O won\n", cas );
		else if(is_complete(s))
		    printf("Case #%d: Game has not completed\n",cas);
		else
			printf("Case #%d: Draw\n", cas);
		
		cas++;
	}
}
