#include<iostream>
using namespace std;

int main(){
	int tc;
	int a,b,k;
	cin>>tc;
	int sol;
	for(int c=0;c<tc;c++)
	{
		sol=0;
		cin>>a>>b>>k;
		for(int i=0;i<a;i++)
			for(int j=0;j<b;j++)
				if((i&j)<k)	sol++;
		printf("Case #%d: %d\n",(c+1),sol);
	}
	return 0;
};