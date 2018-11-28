#include <iostream>
using namespace std;

int t,n,r,p,s,a[3],b[3],c[3];
char d[3];
bool f;
string S,T,A,B;

void sort(int,int);

int main()
{	
	cin >> t;
	
	for (int i = 1; i <= t; ++i)
	{
		cin >> n >> r >> p >> s;
		cout << "Case #" << i << ": ";
		f = false;
		
		c[0] = min(min(p,r),s);
		c[2] = max(max(p,r),s);
		c[1] = (1<<n)-c[0]-c[2];
		
		if (c[0] == p)
		{
			d[0] = 'P';
		}
		else if (c[0] == r)
		{
			d[0] = 'R';
		}
		else if (c[0] == s)
		{
			d[0] = 'S';
		}
		
		if (c[1] == p && d[0] != 'P')
		{
			d[1] = 'P';
		}
		else if (c[1] == r && d[0] != 'R')
		{
			d[1] = 'R';
		}
		else if (c[1] == s && d[0] != 'S')
		{
			d[1] = 'S';
		}
		
		if (c[2] == p && d[0] != 'P' && d[1] != 'P')
		{
			d[2] = 'P';
		}
		else if (c[2] == r && d[0] != 'R' && d[1] != 'R')
		{
			d[2] = 'R';
		}
		else if (c[2] == s && d[0] != 'S' && d[1] != 'S')
		{
			d[2] = 'S';
		}
		
		for (int j = 0; j < 3; ++j)
		{
			a[0] = 0;
			a[1] = 0;
			a[2] = 0;
			
			a[j] = 1;
			
			S = '0'+j;
			
			for (int k = 0; k < n; ++k)
			{
				T = "";
				
				for (int l = 0; l < S.size(); ++l)
				{	
				switch (S[l])
				{
					case '0':
						T += "12";
						break;
					case '1':
						T += "02";
						break;
					case '2':
						T += "01"; 
						break;
				}
				}
				
				S = T;
				
				b[0] = a[1]+a[2];
				b[1] = a[2]+a[0];
				b[2] = a[0]+a[1];
				
				a[0] = b[0];
				a[1] = b[1];
				a[2] = b[2];
			}
			
			b[0] = min(min(a[0],a[1]),a[2]);
			b[2] = max(max(a[0],a[1]),a[2]);
			b[1] = a[0]+a[1]+a[2]-b[0]-b[2];
		
			if (b[0] == c[0] && b[1] == c[1] && b[2] == c[2])
			{
				f = true;
				
				b[0] = 0;
				b[1] = 0;
				b[2] = 0;
				
				T = "";
				
				for (int i = 0; i < S.size(); ++i)
				{
					T += d[S[i]-'0'];
				}
				
				int p1 = 0;
				int r1 = 0;
				int s1 = 0;
				
				for (int i = 0; i < T.size(); ++i)
				{
					if (T[i] == 'P')
						p1++;
						if (T[i] == 'R')
						r1++;
						if (T[i] == 'S')
						s1++;
				}
				
				if (p1==p && r1 == r && s1 == s)
				{
					sort(0,(1<<n)-1);
					cout << T << endl;
					
					break;
				}
			}
		}
		
		if (!f)
		{
			cout << "IMPOSSIBLE" << endl;
		}
	}
	
}

void sort(int i, int j)
{	
	if (j-i == 1)
	{
		if (T[i] > T[j])
		{
			char c = T[i];
			T[i] = T[j];
			T[j] = c;
		}
	}
	else
	{
		sort(i,(i+j)/2);
		sort((i+j)/2+1,j);
	
	
		A = T.substr(i,1<<(j-i));
		B = T.substr((i+j)/2+1,1<<(j-i));
	
		if (A>B)
		{
			for (int k = i; k <= (i+j)/2; ++k)
			{
				T[k] = T[(i+j)/2+k-i+1];
			}
			
			for (int k = (i+j)/2+1; k <= j; ++k)
			{
				T[k] = A[k-(i+j)/2-1];
			}
		}
	}
}
