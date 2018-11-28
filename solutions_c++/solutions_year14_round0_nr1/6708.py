#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <set>


using namespace std;


int a[5][5];
set<int> st;
vector<int> del;


void solve(int t)
{
    for(int i = 1; i <= 16; i++)
        st.insert(i);
    for(int i = 0; i < 2; i++)
    {
        int x;
        scanf("%d", &x);
        for(int j = 0; j < 4; j++)
            for(int k = 0; k < 4; k++)
                scanf("%d", &a[j][k]);
        del.clear();
        for(set<int>::iterator it = st.begin(); it != st.end(); it++)
        {
        	bool f = false;
        	for(int i = 0; i < 4; i++)
        		if(*it == a[x - 1][i])
        			f = true;
       		if(!f)
       			del.push_back(*it);
        }
        for(int i = 0; i < del.size(); i++)
        	st.erase(del[i]);
    }
    if(st.size() == 1)
    	printf("Case #%d: %d\n", t, *st.begin());
    else if(st.size() > 1)
    	printf("Case #%d: Bad magician!\n", t);
	else
		printf("Case #%d: Volunteer cheated!\n", t);
}


int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int t;
    scanf("%d", &t);
    for(int i = 0; i < t; i++)
        solve(i + 1);
    return 0;
}
