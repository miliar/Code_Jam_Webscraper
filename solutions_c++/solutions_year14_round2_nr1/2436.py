#include<iostream>
#include<cstring>
#include<cstdio>

using namespace std;

int func(string a, string b)
{
	int count = 0, i, j, len1, len2;
	
	len1 = a.length();
	len2 = b.length();
	
	i = j = 0;
	
	while(i<len1 && j<len2)
	{
		if(a[i] == b[j])
		{
			i++;
			j++;
		}
		else if(i>0 && a[i-1] == a[i])
		{
			count++;
			i++;
		}
		else if(j>0 && b[j-1] == b[j])
		{
			count++;
			j++;
		}
		else
			return -1;
	}
	
	while(i<len1 && j>0 && a[i] == b[j-1])
	{
		i++;
		count++;
	}
	
	while(j<len2 && i>0 && b[j] == a[i-1])
	{
		j++;
		count++;
	}
	
	if(i!=len1 || j!=len2)
		return -1;
	
	return count;
}


int main()
{
	freopen("A-small-attempt2.in", "r", stdin);
	freopen("output.out", "w", stdout);
	
	int t, counter = 1, N, i, res;
	string word[105];
	
	scanf("%d", &t);
	
	while(t--)
	{
		scanf("%d", &N);
		
		for(i=0; i<N; i++)
			cin>>word[i];
			
		res = func(word[0], word[1]);
			
		
		printf("Case #%d: ", counter++);
		if(res==-1)
			printf("Fegla Won\n");
		else
			printf("%d\n", res);				
	}
	
	
	return 0;
}
