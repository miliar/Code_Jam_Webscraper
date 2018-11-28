#include <cstdio>
#include <cstring>

#define min(a,b) ((a)<(b)?(a):(b))

typedef struct BigNum
{
	char nb[200];
	int n;

	BigNum operator=(const BigNum &a)
	{
		n = a.n;
		strcpy(nb,a.nb);
		return (*this);
	}

	BigNum operator+(const BigNum &a)
	{//AQUI	
		BigNum b;
		int vai1 = 0;
		int m = a.n;
		int mi = min(n,m);
		int i;
		for(i=0; i<mi; i++)
		{
			b.nb[i] = nb[i]+a.nb[i]+vai1-'0';
			vai1=0;
			if(b.nb[i]>'9') {b.nb[i]-=10; vai1=1;}
		}
		if(m==n)
		{
			if(vai1)
			{
				b.nb[n] = '1';
				b.nb[n+1] = '\0';
				b.n=n+1;
			}
			else
			{
				b.nb[n] = '\0';
				b.n = n;
			}
			return b;
		}
		if(n>m) 
		{
			b.nb[i] = nb[i] + vai1;
			for(i++; i<n; i++)
				b.nb[i] = nb[i];
		}
		else 
		{
			b.nb[i] = a.nb[i] + vai1;
			for(i++; i<m; i++)
				b.nb[i] = a.nb[i];
		}
		b.nb[i]='\0';
		b.n = i;
		b.nb[b.n]='\0';
		return b;
	}

	void zera()
	{
		for(int i=0; i<200; i++) nb[i] = '0';
		nb[1]='\0';
		n=0;
	}

	BigNum desl(int num)
	{
		BigNum b;
		b.zera();
		b.nb[1]='0';
		if(num == 0) return *this;
		for(int i=n-1+num; i>=num; i--)
			b.nb[i] = nb[i-num];
		b.nb[n+num]='\0';
		b.n = n+num;
		return b;
	}

	BigNum operator*(const BigNum &a)
	{
		BigNum b,c;
		c.zera();
		for(int i=0; i<n; i++)
		{
			b.zera();
			//printf("DEBUGn0 %d %d\n",b.n,i);
			for(int j='0'; j<nb[i]; j++)
				b = b + a;
			b = b.desl(i);
			c = c + b;
		}
		return c;
	}

	bool operator<(const BigNum &a)
	{
		if(n<a.n) return true;
		if(n>a.n) return false;
		for(int i=n-1; i>=0; i--)
			if(nb[i]<a.nb[i]) return true;
			else if(nb[i]>a.nb[i]) return false;
		return false;
	}

	bool operator<=(const BigNum &a)
	{
		if(n<a.n) return true;
		if(n>a.n) return false;
		for(int i=n-1; i>=0; i--)
			if(nb[i]<a.nb[i]) return true;
			else if(nb[i]>a.nb[i]) return false;
		return true;
	}

	bool operator>(const BigNum &a)
	{
		return !((*this)<=a);
	}

	bool palindrome()
	{
		for(int i=0; i<n/2+1; i++)
			if(nb[i]!=nb[n-i-1])
				return false;
		return true;
	}
}Big;

int main()
{
	Big um;
	int t;
	scanf(" %d",&t);
	strcpy(um.nb,"1");
	um.n = 1;
	for(int i=0; i<t; i++)
	{
		Big a,b;
		Big j,k;
		int r=0;
		char auxa[200],auxb[200];
		scanf(" %s %s",auxa,auxb);
		a.n = strlen(auxa);
		b.n = strlen(auxb);
		for(int I=0; I<a.n; I++)
			a.nb[I] = auxa[a.n-I-1];		
		a.nb[a.n]='\0';
		for(int I=0; I<b.n; I++)
			b.nb[I] = auxb[b.n-I-1];	
		b.nb[b.n]='\0';
		for(j=um; (k=j*j) < a; j = j+um);
		//printf("DEBUG %s %s %s\n",j.nb,k.nb,a.nb);
		//printf("DEBUG %s %s %s %d\n",(j+um).nb,((j+um)*(j+um)).nb,a.nb,((j+um)*(j+um))<a);
		//printf("DEBUG(j*j): %s %d %s %d\n",j.nb, j.n,b.nb,b.n);
		//printf("DEBUG BOOL: %d\n",int((k=j*j) <= b));
		for(;;j = j+um)
		{
			//printf("DEBUG ENTROU %s %s\n",j.nb,k.nb);
			if(!j.palindrome()) continue;
			if((k=j*j) > b) break;
			if(k.palindrome())//{
				r++;//printf("%s %s ",j.nb,a.nb);}
		}
		//printf("DEBUG SAIU %s %s\n",j.nb,k.nb);
		//printf("DEBUG3\n");
		printf("Case #%d: %d\n",i+1,r);
	}
	return 0;
}
