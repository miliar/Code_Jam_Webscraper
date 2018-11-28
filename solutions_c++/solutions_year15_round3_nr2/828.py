#include <cstdio>
#include <iostream>
typedef unsigned int uint;
double A[128][128][128]={1.0};

main()
{
	uint T=0;
	scanf("%u",&T);
	for(uint t=1; t<=T; ++t)
	{
		uint K=0,L=0,S=0;
		char kbd[128];
		char tgt[128];
		scanf("%u%u%u%s%s",&K,&L,&S,kbd,tgt);
		uint kc[26]={};
		for(uint i=0; i<K; ++i)
			++kc[kbd[i]-'A'];
		uint tc[26]={};
		for(uint i=0; i<L; ++i)
			++tc[tgt[i]-'A'];

		uint next[128][26]={};
		for(uint l=0; l<L; ++l)
		{
			for(uint k=0; k<26; ++k)
			{
				if(tgt[l]=='A'+k && l+1<L)
					next[l][k]=l+1;
				else
				{
					uint n=l;
					for(; n; --n)
					{
						bool ok=tgt[n-1]=='A'+k;
						for(uint i=0; ok && i<n-1; ++i)
							ok=tgt[i]==tgt[l+1-n+i];
						if(ok)
							break;
					}
					next[l][k]=n;
				}
			}
		}
		uint l0=next[L-1][tgt[L-1]-'A'];
		//std::cerr << l0 << std::endl;
		uint N=0;
		if(L<=S)
			N=1+(S-L)/(L-l0);
		for(uint k=0; k<26; ++k)
			if(tc[k]!=0 && kc[k]==0)
				N=0;

		for(uint s=0; s<128; ++s)
			for(uint l=0; l<128; ++l)
				for(uint n=0; n<128; ++n)
					A[s][l][n]=0.0;
		A[0][0][0]=1.0;

		for(uint s=0; s<S; ++s)
		{
			for(uint k=0; k<26; ++k)
			{
				if(!kc[k])
					continue;
				double p=double(kc[k])/K;
				for(uint l=0; l<L; ++l)
				{
					uint a=next[l][k];
					// continues word
					if(tgt[l]=='A'+k)
					{
						// ends here
						if(l+1==L)
						{
							for(uint n=0; n<=N; ++n)
								A[s+1][a][n+1]+=p*A[s][l][n];
						}
						// not ended
						else
						{
							for(uint n=0; n<=N; ++n)
								A[s+1][a][n]+=p*A[s][l][n];
						}
					}
					// wrong key
					else
					{
						for(uint n=0; n<=N; ++n)
							A[s+1][a][n]+=p*A[s][l][n];
					}
				}
			}
		}
		//std::cerr << N << " " << S << " " << L << " " << N << " " << std::endl;
		double e=0;
		for(uint l=0; l<S; ++l)
			for(uint n=1; n<=N; ++n)
				e+=n*A[S][l][n];
		double r=N-e;
		printf("Case #%u: %.9f\n",t,r);
	}
}
