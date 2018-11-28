#include<iostream>
#include<cstring>
using namespace std;

int Max(int x,int y)
{
	if(x>y) return x;
	else return y;
}

int Min(int x,int y)
{
	if(x>y) return y;
	else return x;
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T,N,M,i,j,ca,mmax,mmin,k;
	int a[105][105];
	bool b[105][105];
	bool ch,th;
	cin>>T;
	for(ca=1;ca<=T;ca++)
	{
		cin>>N>>M;
		mmax=1;
		mmin=100;
		th=true;
		for(i=0;i<N;i++)
		{
			for(j=0;j<M;j++)
			{
				cin>>a[i][j];
				mmax=Max(mmax,a[i][j]);
                mmin=Min(mmin,a[i][j]);
			}
		}
		for(k=mmax;k>mmin;k--)
		{
        for(i=0;i<N;i++)
		{
			for(j=0;j<M;j++)
			{
				b[i][j]=0;
			}
		}
		for(i=0;i<N;i++)
		{
			if(a[i][0]<k)
			{
				ch=true;
				for(j=0;j<M;j++)
				{
					if(a[i][j]>=k)
					{
						ch=false;
						break;
					}
				}
				if(ch)
				{
					for(j=0;j<M;j++)
					{
						b[i][j]=1;
					}
				}
			}
		}
        for(i=0;i<M;i++)
		{
			if(a[0][i]<k)
			{
				ch=true;
				for(j=0;j<N;j++)
				{
					if(a[j][i]>=k)
					{
						ch=false;
						break;
					}
				}
				if(ch)
				{
					for(j=0;j<N;j++)
					{
						b[j][i]=1;
					}
				}
			}
		}
		ch=true;
		for(i=0;i<N;i++)
		{
			for(j=0;j<M;j++)
			{
				if((a[i][j]<k)&&(b[i][j]==0))
				{
					ch=false;
					break;
				}
			}
			if(!ch) break;
		}
		if(!ch) { th=false; break;}
		}
		if(th) cout<<"Case #"<<ca<<": YES"<<endl;
		else cout<<"Case #"<<ca<<": NO"<<endl;
	}
	return 0;
}