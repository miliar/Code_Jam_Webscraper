#include<bits/stdc++.h>
using namespace std;
int t,i;
double c,f,x,u,res;
int main()
{
	ifstream iff("B-large.in");
	ofstream off("lol.txt");
	iff >>t;
	for(i=1;i<=t;i++)
	{
		res=0.0;
		u=2.0;
	//	scanf("%lf %lf %lf",&c,&f,&x);
	iff >> c>>f>>x;	
		while(1)
		{
			if((c/u)+(x/(u+f))>=x/u)
			{
	//			printf("%lf %lf %lf\n",u,res,c);
				res+=x/u;
				break;
			}
			
			res=res+c/u;
			u=u+f;
		}
		
		off << "Case #"<<i<<": " <<setprecision(7)<<fixed<<res<<endl;
		
	}
	return 0;
}
