#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
#include <vector>
#include <string>
#include <cmath>
#include <map>
using namespace std;

typedef unsigned long long ull;
int T, n;
string s;
string c[10] = {"ZERO","TWO","FOUR","SIX","EIGHT","ONE","THREE","FIVE","SEVEN","NINE"};
string k = "ZWUXGOHFVI";
int d[10] = {0,2,4,6,8,1,3,5,7,9};

int main()
{
    //freopen("A-small-attempt3.in","r",stdin);
    freopen("A-large.in","r",stdin);
    freopen("a.txt","w",stdout);
    scanf("%d", &T);
	for (int cse = 1; cse <= T; cse++)
	{
	    map<char, int> m;
	    int ans[10];
	    memset(ans, 0, sizeof(ans));
	    cin>>s;
	    for (int i = 0; i < s.size(); i++)
            m[s[i]] ++;
        for (int i = 0; i < 10; i++)
        {
            int t = m[k[i]];
            if (t > 0)
            {
                for (int j = 0; j < c[i].size(); j++)
                    m[c[i][j]] -= t;
                ans[d[i]] += t;
            }
        }
        /*sort(s.begin(), s.end());
        //cerr<<s<<endl;
        int q[10] = {0,5,1,6,2,7,3,8,4,9};
        string ss = "";
        for (int i = 0; i < 10; i++)
            for (int j = 0; j < ans[i]; j++)
                ss += c[q[i]];
        sort(ss.begin(), ss.end());
        //cerr<<ss<<endl;
        cerr<<(s==ss);
        //for (auto x: m) cerr<<x.second<<' ';cerr<<endl;*/
	    printf("Case #%d: ", cse);
        for (int i = 0; i < 10; i++)
            for (int j = 0; j < ans[i]; j++)
                printf("%d", i);
        printf("\n");


	}
	return 0;
}
