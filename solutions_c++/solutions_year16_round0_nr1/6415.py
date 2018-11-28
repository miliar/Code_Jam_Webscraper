#include <cstdio>
#include <vector>

int main()
{
	int T;
	int i,j,k;
	int digit[10];
	std::vector<int> ansList;

	freopen("in.in","r",stdin);

	scanf("%d",&T);

	for(i=0;i<T;i++)
	{
		int num,tar,mok,nam,cnt;
		int key=1;
		scanf("%d",&num);

		tar = num;

		for(j=0;j<10;j++)
		{
			digit[j] = 0;
		}

		if(num == 0)
		{
			key = 0;
		}

		while(key)
		{
			mok = tar;
			while(mok != 0)
			{
				nam = mok % 10;
				mok = mok / 10;
	
				digit[nam] = 1;
			}

			cnt = 0;
			for(k=0;k<10;k++)
			{
				cnt += digit[k];
			}
			if(cnt == 10)
			{
				break;
			}
			tar += num;
		}
		ansList.push_back(tar);
	}

	fclose(stdin);
	freopen("out","w",stdout);

	for(i=0;i<T;i++)
	{
		if(ansList[i] == 0)
		{
			printf("Case #%d: INSOMNIA\n",i+1);
		}
		else
		{
			printf("Case #%d: %d\n",i+1,ansList[i]);
		}
	}
}
