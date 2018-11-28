#include <cstdio>
#include <vector>

int main()
{
	int T;
	int i,j;
	std::vector<int> ansList;

	freopen("B-large.in","r",stdin);

	scanf("%d%*c",&T);

	for(i=0;i<T;i++)
	{
		std::vector<char> st;

		char tmp;
		int ans;

		while(1)
		{	
			scanf("%1c",&tmp);

			if(tmp !='+' && tmp != '-')
			{
				break;
			}

			if(st.empty() || tmp != st.back())
			{
				st.push_back(tmp);
			}
		}

		ans = st.size();
		if(st.back() == '+') ans--;

		ansList.push_back(ans);
	}

	fclose(stdin);
	freopen("out","w",stdout);

	for(i=0;i<T;i++)
	{
		printf("Case #%d: %d\n",i+1,ansList[i]);
	}	
}