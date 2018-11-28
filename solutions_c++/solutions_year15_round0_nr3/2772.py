#include<iostream>
#include<fstream>
#include<cstdio>
#include<cmath>
using namespace std;
int main ()
{
	int t,l,x,a[4][4];
	bool done=true;
	string g;
//	get the matrix
	ifstream in("matrix.txt");
	for(int i=0;i<4;i++)
	{
		for(int j=0;j<4;j++)
		{
			in>>a[i][j];
		}
	}
	in.close();
	freopen("C-small-attempt0.in","r",stdin);
	freopen("c-small.out","w",stdout);
	cin>>t;
	for(int z=1;z<=t;z++)
	{
		cin>>l>>x;
		cin>>g;
		done=true;
		for(int i=0;i<l;i++)
		{
			g[i]-=103;
		}
		if(x*l<3||l==1)
		{
			done=false;
			goto byebye;
		}
		else if(l*x==3)
		{
			for(int i=0;i<3;i++)
			{
				if(g[i]!=i+2)
				{
					done=false;
					goto byebye;
				}
			}
		}
		else
		{
//			multiply
//			printf("Whohooo\n");
			int count=0,result=2,ans=g[0],k=1,i=1,xx,y,x_sign,y_sign;
			for(;i<l*x;i++,k++)
			{
				k=k%l;
				if(ans==result)
				{
					if(result<4)
					{
						result++;
						ans=g[k];
//						printf("result = %d\n",result);
						continue;
					}
				}
//				ans=mul(ans,g[k]);
				x_sign=ans<0?-1:1;
				xx=abs(ans);
				y_sign=g[k]<0?-1:1;
				y=abs(g[k]);
				ans=a[y-1][xx-1];
				ans*=x_sign;
				ans*=y_sign;
//				printf("xx = %d y = %d ans = %d i=%d where x_sign= %d y_sign=%d\n",xx*x_sign,y*y_sign,ans,i,x_sign,y_sign);
			}
			if(ans==4&&result==4)
			{
				done=true;
//				printf("succes\n");
			}
			else
			{
				done=false;
			}
		}
		byebye:;
		if(done)
		{
			printf("Case #%d: YES\n",z);
		}
		else
		{
			printf("Case #%d: NO\n",z);
		}
	}
	return 0;
}
