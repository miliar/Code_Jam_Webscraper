#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;

static int cntAll=0;
static int _n_=0;
void cntRescure(string str,int num)
{
	int rec=num;
	if(str=="")return ;
	if(str[0]=='0')
	{
		rec++;
	}else
	{
		if(rec<_n_)rec=0;
	}
	if(rec>=_n_)cntAll++;
	cntRescure(str.substr(1),rec);
	//cntRescure(str.substr(1),0);
}

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
	
    int t2;
    cin >> t2;
	string str;
	int n;
	int result=0;
    for (int t1 = 1; t1 <= t2; ++t1) {
        printf("Case #%d: ", t1);
        long long r, t;
        cin >> str>> n;
		for(int i=0;i<str.length();++i)
		{
			if(str[i]=='a'||str[i]=='e'||str[i]=='i'||str[i]=='o'||str[i]=='u')
				str[i]='1';
			else str[i]='0';
		}
		cntAll=0;
		 _n_=n;
		for(int i=0;i<str.length();++i)
			cntRescure(str.substr(i),0);
        cout << cntAll;
        printf("\n");
    }
    
    return 0;
}
