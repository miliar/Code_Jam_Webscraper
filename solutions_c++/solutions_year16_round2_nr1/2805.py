#include <iostream>
using namespace std;

string a[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
int tchar[10][128];
int count[10],cchar[128],mcount[10];

bool isValid()
{
	int ccount[128];
	for(int j='A';j<='Z';j++)
		ccount[j]=0;

	for(int i=0;i<10;i++)
		for(int j='A';j<='Z';j++)
			ccount[j]+=count[i]*tchar[i][j];

	for(int i='A';i<='Z';i++)
		if(ccount[i]!=cchar[i])
		{
			return false;
		}
	return true;
}

int main()
{
	for(int i=0;i<10;i++)
		for(int j=0;j<a[i].size();j++)
			tchar[i][a[i][j]]++;
	string s;
	int T;
	cin >> T;
	for(int t=1;t<=T;t++)
	{
		for(int i=0;i<10;i++)
		{
			count[i]=0;
			mcount[i]=2001;
		}
		for(int i=0;i<128;i++)
			cchar[i]=0;
		cin >> s;

		for(int i=0;i<s.size();i++)
		{
			if(s[i]=='Z')
				count[0]++;
			else if(s[i]=='W')
				count[2]++;
			else if(s[i]=='U')
				count[4]++;
			else if(s[i]=='X')
				count[6]++;
			else if(s[i]=='G')
				count[8]++;
			cchar[s[i]]++;
		}

		for(int i=0;i<10;i++)
		{
			for(int j=0;j<a[i].size();j++)
				mcount[i]=min(cchar[a[i][j]], mcount[i]);
		}
		int r=0;
		for(int i=0;i<10;i+=2)
			r+=count[i]*a[i].size();
		cout << "Case #" << t << ": ";
		for(count[1]=0;count[1]<=mcount[1]&&count[1]*3<=s.size();count[1]++)
			for(count[3]=0;count[3]<=mcount[3]&&count[1]*3+count[3]*5<=s.size();count[3]++)
				for(count[5]=0;count[5]<=mcount[5]&&count[1]*3+count[3]*5+count[5]*4<=s.size();count[5]++)
					for(count[7]=0;count[7]<=mcount[7]&&count[1]*3+count[3]*5+count[5]*4+count[7]*5<=s.size();count[7]++)
					{
						count[9]=s.size()-(count[1]*3+count[3]*5+count[5]*4+count[7]*5+r);
						if(count[9]%4!=0)
							continue;
						count[9]/=4;
						if(count[9]>mcount[9])
							continue;
						if(isValid())
						{
							for(int i=0;i<10;i++)
								for(int j=0;j<count[i];j++)
									cout << i;
							for(int i=0;i<10;i++)
								count[i]=s.size();
						}
					}
		cout << endl;
	}
}
