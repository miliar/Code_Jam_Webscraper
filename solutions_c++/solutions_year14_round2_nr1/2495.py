#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int main()
{
	int tc, t, n, i, j, p, q, f, l1, l2, cnt;
	char str[100][102];

	freopen("inp_repeater.txt","r",stdin);
	freopen("out_repeater.txt","w",stdout);

	scanf("%d",&tc);

	for(t=1; t<=tc; t++)
	{
		scanf("%d",&n);

		for(i=0; i<n; i++)
			scanf("%s",&str[i]);

		cnt=0;
		f=0;
		for(i=0; i<n; i++)
		{
			for(j=i+1; j<n; j++)
			{
				l1=strlen(str[i]);
				l2=strlen(str[j]);
				for(p=0,q=0; p<l1 && q<l2; )
				{
					if(str[i][p]==str[j][q]) {
						p++;
						q++;
						continue;
					}
					else
					{
						if(p!=0 && str[i][p] == str[i][p-1]) {
							p++;
							cnt++;
						}
						else if(q!=0 && str[j][q] == str[j][q-1]) {
							q++;
							cnt++;
						}
						else {
							f=1;
							break;
						}
					}
				}

				
				while(!f && p<l1) {
					if(p!=0 && str[i][p] == str[i][p-1])
						cnt++;
					else {
						f=1;
						break;
					}
					p++;
				}
				while(!f && q<l2) {
					if(q!=0 && str[j][q] == str[j][q-1])
						cnt++;
					else {
						f=1;
						break;
					}
					q++;
				}
			}
		}

		if(!f)
			printf("Case #%d: %d\n",t,cnt);
		else
			printf("Case #%d: Fegla Won\n",t);
	}

	return 0;
}