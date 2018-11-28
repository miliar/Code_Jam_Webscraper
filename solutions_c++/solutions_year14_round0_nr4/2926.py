#include<iostream>
#include<conio.h>
#include<cstdio>
#include<algorithm>
#include<vector>

using namespace std;

int main()
{
	freopen("D-large.in","r",stdin);
	//freopen("Inp1.txt","r",stdin);
	freopen("Out.out","w",stdout);
	static long T, N, x, y, W, DW;
    static long double qwert;
    vector <long double> a, b;
	cin>>T;
	for(int i=1;i<=T;i++)
	{
		a.erase(a.begin(),a.end());
		b.erase(b.begin(),b.end());
		W=0; DW=0;
        cin>>N;
		for(int j=0;j<N;j++)
		{
			cin>>qwert;
			a.push_back(qwert);
		}
		for(int j=0;j<N;j++)
		{
			cin>>qwert;
			b.push_back(qwert);
   		}
		sort(a.begin(),a.end());
		sort(b.begin(),b.end());
		x=0; y=0;
		while(x<N && y<N)
		{
			if(a[x]<b[y])
			{
				x++; y++;
			}
			else if(a[x]>b[y])
		   		y++;
		}
		W=N-x;
		x=N-1;
		y=N-1;
		while(x>-1 && y>-1)
		{
			if(a[x]>b[y])
		   	{
					x--;
					y--;
					DW++;
			}
			else if(a[x]<b[y])
				y--;
		}
		cout<<"Case #"<<i<<": "<<DW<<" "<<W<<endl;
	}
	return 0;
}
