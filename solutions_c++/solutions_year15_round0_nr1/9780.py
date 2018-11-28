#include <iostream>
#include <stdio.h>
using namespace std;

int main() {
	int t,chk;
	scanf("%d", &t);
	chk=t;
	while(t--)
	{
		int max, arr[10], cnt=0, tot=0;
		char a[10];
		scanf("%d", &max);
		cin>>a;
		for(int i=0; i<max+1; i++)
		{
			arr[i] = int(a[i])-48;
		}
		for(int i=0; i<max+1; i++)
		{
			if(i>tot)
			{	
				while(i!=tot)
				{
					cnt++; tot++;
				}
			}
			tot+=arr[i];
		} 
		printf("Case #%d: %d\n", chk-t, cnt);
	}
	return 0;
}