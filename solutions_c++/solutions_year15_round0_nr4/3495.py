#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstring>
#include<stack>
#include<deque>
#include<queue>
#include<vector>
#include<list>
#include<set>
#include<map>
#include<cmath>
#include<climits>

using namespace std;


int main()
{
	freopen("D-small-attempt1.in", "r", stdin);
	freopen("output.out", "w", stdout);

	int t, counter;

	scanf("%d", &t);

	for(counter=1; counter<=t; counter++)
	{
	    int X, R, C, i, j;
	    bool flag = false;

	    cin>>X>>R>>C;

	    if(R>C)
            swap(R,C);

        if(X==1)
            flag= true;
        else if(X == 2 && R*C%2==0)
            flag = true;
        else if(X==3)
        {
            if((R==2 && C==3) || R==3)
                flag = true;
        }
        else if(X==4)
        {
            if((R==3 && C==4) || R==4)
                flag = true;
        }

		printf("Case #%d: ", counter);

		if(!flag)
            cout<<"RICHARD\n";
        else
            cout<<"GABRIEL\n";
	}

	return 0;
}
