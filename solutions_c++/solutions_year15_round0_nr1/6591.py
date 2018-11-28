#include <bits/stdc++.h>
using namespace std;
void doit(){
    int t=0;
	cin>>t;
	int p=1;
	for(int i=1;i<=t;i++){
		int max=0,a,b,c,d=0,e=0;
		getchar();
		cin>>max;
		getchar();
		a=getchar()-'0';
		
		if(max==0&&a==0)
			cout<<"Case #"<<i<<": 0-"<<endl;
		b=a;d+=b;
		for (int i = 1; i <= max; ++i)
		{
			a=getchar()-'0';
			c=a;
			if(d>=i)
			{
				b=c;
				d+=b;
			}
			else {
				e++;
				b=c;
				d++;
				d+=b;
			}
		}
		cout<<"Case #"<<i<<": "<<e<<endl;
	}
}
int main()
{
	doit();
	return 0;
}
