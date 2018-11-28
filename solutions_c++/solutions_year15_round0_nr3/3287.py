#include<iostream>
#include<string>
#include<cstdio>

using namespace std;

string s;

enum dim
{
	u,
	i,
	j,
	k
};

struct qtn
{
	enum dim d;
	int sign;
};

void multiply (struct qtn *f, struct qtn *s, struct qtn *p)
{
	if ((f->d == u) && (s->d == u))	
	{
		p->d = u;
		p->sign = 1;
	}				
	if ((f->d == u) && (s->d == i))
	{
		p->d = i;
		p->sign = 1;
	}	
	if ((f->d == u) && (s->d == j))
	{
		p->d = j;
		p->sign = 1;
	}	
	if ((f->d == u) && (s->d == k))
	{
		p->d = k;
		p->sign = 1;
	}	
	if ((f->d == i) && (s->d == u))
	{
		p->d = i;
		p->sign = 1;
	}	
	if ((f->d == i) && (s->d == i))
	{
		p->d = u;
		p->sign = -1;
	}	
	if ((f->d == i) && (s->d == j))
	{
		p->d = k;
		p->sign = 1;
	}	
	if ((f->d == i) && (s->d == k))
	{
		p->d = j;
		p->sign = -1;
	}	
	if ((f->d == j) && (s->d == u))
	{
		p->d = j;
		p->sign = 1;
	}	
	if ((f->d == j) && (s->d == i))
	{
		p->d = k;
		p->sign = -1;
	}	
	if ((f->d == j) && (s->d == j))	
	{
		p->d = u;
		p->sign = -1;
	}
	if ((f->d == j) && (s->d == k))	
	{
		p->d = i;
		p->sign = 1;
	}
	if ((f->d == k) && (s->d == u))	
	{
		p->d = k;
		p->sign = 1;
	}
	if ((f->d == k) && (s->d == i))	
	{
		p->d = j;
		p->sign = 1;
	}
	if ((f->d == k) && (s->d == j))	
	{
		p->d = i;
		p->sign = -1;
	}
	if ((f->d == k) && (s->d == k))	
	{
		p->d = u;
		p->sign = -1;
	}
	p->sign *= ( (f->sign) * (s->sign) );
	return;
}	

void constr_qtn (struct qtn *p, char c)
{
	if ( c == 'i' )
	{
		p->d = i;
	}
	else if ( c == 'j' )
	{
		p->d = j;
	}
	else
	{
		p->d = k;
	}
	p->sign = 1;
	return;
}
 						
bool output ( )
{
	struct qtn first, sec, p;
	bool i_k_exists = false, i_exists = false;
 
	constr_qtn (&first, s[0]);
	for (int m = 1; m < ((int)s.length()); m++)
	{
		if ((first.d == i) && (first.sign == 1))
		{
			i_exists = true;				
		}
		if (((first.d == k) && (first.sign == 1)) && (i_exists == true))
		{
			i_k_exists = true;
		}
		constr_qtn (&sec, s[m]);
		multiply (&first, &sec, &p);
		first = p;
	}

	if (( (first.d == u) && (first.sign == -1) ) && (i_k_exists == true))
	{
		return true;	
	}
	else
	{
		return false;
	}
}
 		
int main()
{
	ios::sync_with_stdio(false);

	int T,L,X;
	string inp;

	cin >> T;
	for (int m=0;m<T;m++)
	{
		cin >> L >> X;

		if (X >= 12)
		{
			X = ( X % 4 ) + 8;
		}
			 
		inp.clear();
		s.clear();

		cin >> inp;	        
		for (int n=0; n < X; n++)
		{
			s += inp;
		}
	
		if ( output () )
		{
			cout << "Case #" << (m+1) << ": YES\n";
		}
		else
		{
			cout << "Case #" << (m+1) <<": NO\n";
		}
	}	
	return 0;
}
