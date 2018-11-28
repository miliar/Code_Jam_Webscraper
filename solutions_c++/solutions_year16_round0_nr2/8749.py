#include<bits/stdc++.h>
#define ll long long
using namespace std;
string str;
int solve()
{
    int len=str.size();
    stack<char> st;
    char top;
    for(int i=0;i<len;i++)
    {
        if(st.empty())
            st.push(str[i]);
        else
        {
            top=st.top();
            if(str[i]!=top)
            st.push(str[i]);
        }
    }
    top=st.top();
    if(top=='+')
        st.pop();
    return st.size();
}

int main()
{
	int t;
	scanf("%d",&t);
	int i;
	for(i=1;i<=t;i++)
	{
		cin>>str;
		printf("Case #%d: %d\n",i,solve());
	}
return 0;
}
