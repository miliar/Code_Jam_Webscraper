#include<cstdio>
#include<cstring>
#define Mod 1000000007

int TestCase,Case,
	c[110000][30],Sum[110000],Peo[110000],T,
	Ans,Choice,A[110],F[110],
	N,M,
	Pow[110],_Pow[110];
	
char Str[110];

int CalcC(int n,int m){return ((1ll*Pow[n]*_Pow[m])%Mod*_Pow[n-m])%Mod;}

int CalcP(int n,int m){return (1ll*Pow[n]*_Pow[n-m])%Mod;}

void Insert()
{
	int L(strlen(Str)),i,k;
	Str[L]='Z'+1;
	L++;
	for(k=1,i=0;i<L;k=c[k][Str[i++]-'A'])
	{
		Peo[k]++;
		Sum[k]+=L-i+1;
		if(!c[k][Str[i]-'A'])
			c[k][Str[i]-'A']=++T;
	}
	Peo[k]++;
	Sum[k]+=L-i+1;
}

void Count(int l)
{
	if(Peo[l]<=M)
	{
		Ans+=Sum[l];
		Choice=(1ll*Choice*CalcP(M,Peo[l]))%Mod;
	}
	else
	{
		int MaxP(0);
		Ans+=M;
		for(int k=0;k<=26;k++)
			if(c[l][k]&&Peo[c[l][k]]>=MaxP)
				MaxP=Peo[c[l][k]];
		if(MaxP<M)
		{
			int i,k;
			for(k=0;k<=26;k++)
				if(c[l][k])
					Ans+=Sum[c[l][k]];
			for(i=1;i<=M;i++)
			{
				A[i]=1;
				for(k=0;k<=26;k++)
					if(c[l][k])
						A[i]=(1ll*A[i]*CalcP(i,Peo[c[l][k]]))%Mod;
			}
			for(i=1;i<=M;i++)
			{
				F[i]=A[i];
				for(k=1;k<i;k++)
					F[i]=(1ll*F[i]-1ll*F[k]*CalcC(i,k))%Mod;
				F[i]=(F[i]+Mod)%Mod;
			}
			Choice=(1ll*Choice*F[M])%Mod;
		}
		else for(int k=0;k<=26;k++)
			if(c[l][k])
				Count(c[l][k]);
	}
}

int POW(int x,int k)
{
	int S(1);
	for(;k;k>>=1)
	{
		if(k&1)S=(1ll*S*x)%Mod;
		x=(1ll*x*x)%Mod;
	}
	return S;
}

int main()
{
	int i;
	//freopen("d.in","rb",stdin);
	//freopen("d.out","wb",stdout);
	scanf("%d",&TestCase);
	Pow[0]=_Pow[0]=1;
	for(i=1;i<=100;i++)
	{
		Pow[i]=(1ll*Pow[i-1]*i)%Mod;
		_Pow[i]=POW(Pow[i],Mod-2);
	}
	for(Case=1;Case<=TestCase;Case++)
	{
		memset(c,0,sizeof c);
		memset(Peo,0,sizeof Peo);
		memset(Sum,0,sizeof Sum);
		Ans=0;
		Choice=1;
	    T=1;
		scanf("%d%d",&N,&M);
		for(i=0;i<N;i++)
		{
			scanf("%s",Str);
			Insert();
		}
		Count(1);
		Ans-=N;
		printf("Case #%d: %d %d\n",Case,Ans,Choice);
	}
	return 0;
}
