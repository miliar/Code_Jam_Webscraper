#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<map>

#define INF 1000000000
#define endl '\n'
#define ll long long

using namespace std;

typedef map<string,string> M1;
map<string,M1> form;

void Init()
{	
	form["1"]["i"] = "i";
	form["1"]["j"] = "j";
	form["1"]["k"] = "k";
	
	form["i"]["i"] = "-1";
	form["i"]["j"] = "k";
	form["i"]["k"] = "-j";
	
	form["j"]["i"] = "-k";
	form["j"]["j"] = "-1";
	form["j"]["k"] = "i";
	
	form["k"]["i"] = "j";
	form["k"]["j"] = "-i";
	form["k"]["k"] = "-1";
	
	
	form["-1"]["i"] = "-i";
	form["-1"]["j"] = "-j";
	form["-1"]["k"] = "-k";
	
	form["-i"]["i"] = "1";
	form["-i"]["j"] = "-k";
	form["-i"]["k"] = "j";
	
	form["-j"]["i"] = "k";
	form["-j"]["j"] = "1";
	form["-j"]["k"] = "-i";
	
	form["-k"]["i"] = "-j";
	form["-k"]["j"] = "i";
	form["-k"]["k"] = "1";
}

inline string operator * (const string &a, const string &b)
{
	return form[a][b];
}
inline string operator * (const string &a, const char &b)
{
	string c;
	c+=b;
	return form[a][c];
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	
	Init();
	
	int t;
	cin >> t;
	for(int time = 1 ; time <= t ; time++)
	{
		int n,m;
		string str;
		cin >> n >> m;
		cin >> str;
		
		string s;
		s = "1";
		int state = 0;
		for(int i = 0 ; i < m ; i++)
		{
			for(int j = 0 ; j < str.size() ; j++)
			{
				s = s*str[j];
//				cout << "s = " << s << endl;
				if(state==0 && s=="i")
				{
					state++;
					s="1";
				}
				else if(state==1 && s=="j")
				{
					state++;
					s="1";
				}
				else if(state==2 && s=="k")
				{
					state++;
				}
			}
			
			if(i > str.size()*20 && state < 1)
				break;
			if(i > str.size()*40 && state < 2)
				break;
		}
		
//		cout << "state = " << state << endl;
		
		if(state==3 && s=="k")
			cout << "Case #" << time << ": YES" << endl;
		else
			cout << "Case #" << time << ": NO" << endl;
		
	}	
	
	return 0;
}

