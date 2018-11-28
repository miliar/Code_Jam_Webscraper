#include <bits/stdc++.h>
using namespace std;

int main() {
	int t;
	//scanf("%d",&t);
	int x=1;
	ifstream f1;
    ofstream f2;
    f1.open("A-large.in");
    f2.open("output.out");
	f1>>t;
	while(t--)
	{
		int smax;
		string s;
		//scanf("%d",&smax);
		f1>>smax;
		f1>>s;
		int n=smax+1;int count=0,c=0;
		for(int i=0;i<n;i++)
		{

			if(count < i)
			{
				int r=i-count;
				c+=r;
				count+=r;
			}
			count+=(s[i]-'0');

		}
		f2<<"Case #"<<x<<": "<<c<<endl;
		x++;
	}
	f1.close();
    f2.close();
	return 0;
}
