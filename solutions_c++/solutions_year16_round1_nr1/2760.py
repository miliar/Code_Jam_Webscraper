#include <iostream>
#include <cstring>
#include <cstdio>
#include <vector>
#include <string>
#include <cmath>
#include <map>
using namespace std;

typedef unsigned long long ull;
int T, n, j;
string s;

int main()
{
    //freopen("A-small-attempt0.in","r",stdin);
    freopen("A-large.in","r",stdin);
    freopen("a.txt","w",stdout);
    scanf("%d", &T);
	for (int cse = 1; cse <= T; cse++)
	{
        cin>>s;
        string t = "";
        for (auto x: s)
            if (t == "")
                t += x;
            else if (t[0] <= x)
                t.insert(0,1,x);
            else
                t += x;
        printf("Case #%d: ",cse);
        cout<<t<<endl;
	}
	return 0;
}
