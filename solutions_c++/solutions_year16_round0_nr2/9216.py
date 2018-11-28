#include <bits/stdc++.h>
using namespace std;

#define fr(a, n) for(a = 0; a < n; a++)

int main()
{
	int t, i, k;
	string s;
	int lm, cont, lim;
	char aux;
	bool f = 0;
	
	scanf("%d\n", &t);
	
	fr(k, t)
	{
		getline(cin, s);
		
		
		lm = s.size() - 1;
		
		f = 0;
		cont = 0;
		//cout<<"S: "<< s <<'\n';
		while(lm > 0 && s[lm] == '+') lm--;
		//printf("lm: %d\n", lm);
		
		while(lm > 0)
		{
			for(i = 0; i < s.size() && s[i] == '+'; i++)
			{
				s[i] = '-';
				f = 1;
			}
			
			if(f == 1)
			{
				cont++;
				//cout<<"p1: "<< s <<'\n';
			}
			f = 0;
			
			
			while(lm > 0 && s[lm] == '+') lm--;
			
			//printf("lm: %d\n", lm);
			
			if(lm > 0)
			{
				cont++;
			
				lim = (lm) >> 1;
				//printf("lm %d\nlim %d\n", lm, lim);
			
				fr(i, lim+1)
				{
					aux = s[i];
				
					if(s[lm-i] == '+') s[i] = '-';
					else s[i] = '+';
				
					if(aux == '+') s[lm-i] = '-';
					else s[lm-i] = '+';
				}
				
				//cout<<"p2: "<< s <<'\n';
			}
			while(lm > 0 && s[lm] == '+') lm--;
			
		}
		
		if(f == 1)cont++;
		f = 0;
		
		if(s[0] == '-'){
		 cont++;
		 s[0] = '+';
		}
		//cout<<"S: "<< s <<'\n';
		
		printf("Case #%d: %d\n", k+1, cont);
	}
}
