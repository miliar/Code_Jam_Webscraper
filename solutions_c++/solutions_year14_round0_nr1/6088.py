#include <iostream>
#include <cstdio>
#include<string>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <iomanip>
#include <sstream>
#include <vector>
#include <sstream>

using namespace std;
int main()
{   stringstream card;
    char a[5][5],b[5][5];
	freopen("A-small-attempt2.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
    int N;
    scanf("%d",&N);
    string ans;
    int match;
    int count=0;
    for (int cas = 1; cas <= N; ++cas) {

		int Row1;
        scanf("%d",&Row1);

		for(int i=0; i<4;i++)
		for(int j=0; j<4;j++)
		scanf("%d",&a[i][j]);
		int Row2;
		scanf("%d",&Row2);


		for(int i=0; i<4;i++)
		for(int j=0; j<4;j++)
		scanf("%d",&b[i][j]);
        count = 0;
		for(int i=0;i<=4;i++)
		{
		    for(int j=0;j<=4;j++)
		    {
		        if(a[Row1-1][i] == b[Row2-1][j] && a[Row1-1][i]*b[Row2-1][j]!=0)
		        {   match=a[Row1-1][i];
                    count+=1;
		        }
		    }
		}

        stringstream ss;
        ss << match;
        string str = ss.str();
		if(count<1)
		ans = "Volunteer cheated!";
		else if(count>1)
		ans = "Bad magician!";
		else
		ans = str;
		printf("Case #%d: %s\n", cas, ans.c_str());

    }
	return 0;
}
