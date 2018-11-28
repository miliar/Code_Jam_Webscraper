#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <map>
#include <string>

using namespace std;

typedef map<string,int> Dirs;

bool calc(string in,vector<int> &res)
{
	const char *strings[] = {"ZERO", "ONE", "TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"};
	bool nonefound=true;
    for (int i=0;i<10;i++)
	{
		int len=strlen(strings[i]);
		bool found=true;
	    string tmp=in;
		for (int j=0;j<len;j++)
		{
			const char *foundptr=strchr(tmp.c_str(),strings[i][j]);
			if (foundptr==NULL)
			{
				found=false;
				break;
			}
			else
			{
				*((char*)foundptr)='-';
			}
		}

		if (found)
		{
			nonefound=false;
			vector<int> newvec=res;
			newvec.push_back(i);
			bool good=calc(tmp,newvec);
			if (good)
			{
				res=newvec;
				return true;
				break;
			}		
		}
	}

	if (nonefound)
	{
		int cnt=0;
		for (int i=0;i<in.length();i++)
		{
			if (*(in.c_str()+i)=='-')
				cnt++;
		}
		if (cnt==in.length())
		{
			return true;
		}
		else
		{
			return false;
		}
	}

	return false;
}

int main(int argc, char* argv[])
{
  int iCases=0;
 
  if (argc > 1) 
     freopen(argv[1], "rt", stdin);

  if (argc > 2) 
     freopen(argv[2], "wt", stdout);

  cin >> iCases;

  for (int i=1;i<=iCases;i++)
  {
	string in;
    cin >> in;
   
	cout<< "Case #" << i << ": ";

	vector<int> result;
	calc(in,result);
	
	std::sort (result.begin(), result.end()); 

	for (int i=0;i<result.size();i++)
	{
	  cout<< result[i];
	}
	cout<< endl;
  }
  return 0;
}
