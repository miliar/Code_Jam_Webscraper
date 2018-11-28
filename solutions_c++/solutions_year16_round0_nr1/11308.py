#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<sstream>
#include<cmath>
#include<cstring>
#include<cctype>
#include<string>
#include<iostream>
#include<vector>
#include<queue>

using namespace std;

int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	int t, n, temp, r;
	bool marked[10];
	string str;
	while(~scanf("%d", &t))
	{
		for (int i = 0; i < t; i++)
		{
            memset(marked, false, sizeof(marked));
            scanf("%d", &n);
            if (n == 0)
            {
            	printf("Case #%d: INSOMNIA\n", i + 1);
            }
            else
            {
                r = n;
                for (int j = 1;;j++, r += n)
                {
                	str.clear();
                	stringstream ss;
                	ss << r;
                	str = ss.str();
                	//if (j < 50)cout << str << endl;
                	for (int k = 0; k < str.size(); k++)
                	{
                        marked[(int)(str[k] - '0')] = true;
                	}
                	temp = 0;
                	for (int k = 0; k < 10; k++)
                	{
                        if (marked[k])
                        	temp++;
                       //cout << temp;
                	}
                	//if (j < 50) cout << temp << endl;
                	if (temp == 10)
                	{
                        printf("Case #%d: %d\n", i + 1, r);
                        break;
                	}
                }
            }
		}
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
