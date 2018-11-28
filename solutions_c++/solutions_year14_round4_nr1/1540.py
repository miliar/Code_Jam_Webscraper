#include <cstdio>
#include <cstdlib>
#include <string>
#include <sstream>
#include <set>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;


void solve_case()
{
	int n, c;
	scanf("%d %d", &n, &c);
	int tmp;
	vector<int> files;
	while(n-->0)
	{
		scanf("%d", &tmp);
		files.push_back(tmp);
	}
	sort(files.begin(), files.end());
	
	int z = 0;
	while(files.size()>0)
	{
		int last = files.back();
		files.pop_back();
		
		int withid=-1;
		for(int i=0;i<files.size();i++)
		{
			if(files[i]+last <=c)
				withid = i;
			else
				break;
		}
		
		z++;
		if(withid!=-1)
		{
			files.erase(files.begin()+withid);
		}
	}
	
	printf("%d", z);
	return;
}


int main()
{
	int t;
	scanf("%d", &t);
	for(int cn=1;cn<=t;cn++)
	{
		printf("Case #%d: ", cn);
		solve_case();
		printf("\n");
	}
}
