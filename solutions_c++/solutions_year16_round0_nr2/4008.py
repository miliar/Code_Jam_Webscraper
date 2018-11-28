#include<bits/stdc++.h>
using namespace std;

typedef long long int LL;
typedef long long int ULL;

int main()
{
	LL t, c, n;
	scanf("%lld", &t);
	
	c=1;
	while(t--)
	{
		char str[120];
		int cake[120], rp=1;

		cin>>str;
		n = strlen(str);
		
		for(int i=0;i<n;++i)
		{
			cake[i] = (str[i] == '-') ? 0:1;
			rp *= cake[i];
		}
		
//		for(int i=0;i<n;++i)cout<<cake[i];
//		cout<<endl;
		
		printf("Case #%lld: ", c);
		++c;
		
		if(rp == 1)printf("0\n");
		else
		{
			int i, s, e;
			LL moves=0;
			while(1)
			{
				//Step 1: Move till the first + (last -), flip all
				for(i=0;cake[i] == 0 && i<n; ++i);
				//cout<<"Ptr after S1: "<<i<<endl;
				
				if(i<=n && i>0)
				{
					s = 0; e = i-1;
					while(s<=e)
					{
						swap(cake[s], cake[e]);
						if(s!=e)
						{
							cake[s] = (cake[s] == 0)? 1: 0;
							cake[e] = (cake[e] == 0)? 1: 0;
						}
						
						else
						{
							cake[s] = (cake[s] == 0)? 1: 0;
						}
						
						++s;
						--e;
					}
					++moves;
				}
				
				rp =1;
				for(i=0;i<n;++i)rp *= cake[i];
				if(rp == 1)break;
				
				//Step 2: Move till the last + (first -), flip all
				for(i=0; i<n && cake[i] == 1; ++i);
				if(i<=n)
				{
					s = 0; e = i-1;
					while(s<=e)
					{
						swap(cake[s], cake[e]);
						if(s!=e)
						{
							cake[s] = (cake[s] == 0)? 1: 0;
							cake[e] = (cake[e] == 0)? 1: 0;
						}
						
						else
						{
							cake[s] = (cake[s] == 0)? 1: 0;
						}
						
						++s;
						--e;
					}
					++moves;
				}
				
				rp =1;
				for(i=0;i<n;++i)rp *= cake[i];
				if(rp == 1)break;
				
//				//Step 3: Flip everything
//				s = 0; e = n-1;
//				while(s<=e)
//				{
//					swap(cake[s], cake[e]);
//					if(s!=e)
//					{
//						cake[s] = (cake[s] == 0)? 1: 0;
//						cake[e] = (cake[e] == 0)? 1: 0;
//					}
//					
//					else
//					{
//						cake[s] = (cake[s] == 0)? 1: 0;
//					}
//					
//					++s;
//					--e;
//				}
//				++moves;
//				
//				rp =1;
//				for(i=0;i<n;++i)rp *= cake[i];
//				if(rp == 1)break;
			}
			
			printf("%lld\n", moves);
		}
		
	}
	
	return 0;
}
