#include<iostream>
#include<cstdio>
#include<cstring>

using namespace std;

char arr[101];

bool vowel(char ch)
{
	return (ch=='a'||ch=='e'||ch=='i'||ch=='o'||ch=='u');
}

int chk(int n)
{
	int i,j,k,res=0,cnt;
	
	for(i=0;arr[i];++i){
		for(j=i;arr[j];++j){
			cnt = 0;
			for(k=i;k<=j;++k){
				if(vowel(arr[k])) cnt = 0;
				else cnt++;
				if(cnt==n){
					res++;
					break;
				}
			}
			
		}
	}

	return res;
}

int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("Aout.txt","w",stdout);

	int T,N,CS=0;

	scanf("%d",&T);

	while( T-- )
	{
		scanf("%s %d",arr,&N);
		printf("Case #%d: %d\n",++CS,chk(N));
	}
	
	return 0;
}