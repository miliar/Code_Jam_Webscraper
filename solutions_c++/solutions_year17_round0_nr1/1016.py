#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int T;
    scanf("%d",&T);
    for(int t=1;t<=T;t++)
    {
        printf("Case #%d: ",t);
        char str[1005];
        scanf(" %s", str+1);
        int k;
        scanf("%d",&k);
        int len = strlen(str+1);
        int cnt = 0;
        for(int i=1; i<=len-k+1; i++)
        {
        	if(str[i] == '+')
        		continue;
        	cnt++;
        	for(int j=i; j<i+k; j++)
        	{
        		if(str[j] == '+')
        			str[j] = '-';
        		else
        			str[j] = '+';
        	}
        }
        int flag = 0;
        for(int i = len-k+2; i<=len; i++)
        	if(str[i] == '-')
        	{
        		flag = 1;
        		break;
        	}
        if(flag == 1)
        	printf("IMPOSSIBLE\n");
        else
        	printf("%d\n", cnt );
    }
    return 0;
}
