#include<fstream>
#include<string>
using namespace std;
ifstream cin("input.txt");
ofstream cout("output.txt");
char currans,currz;
void multiply_q(char a,char b)
{
	if (a==b)
	{
		if (a!=1) 
		{
			if (currz=='-')
			    currz='+';
			else 
		    	currz='-';
		}
		currans='1';
	}
	else
	{
		if (a=='i')
		{
			if (b=='j')
			{
				currans='k';
			}
			if (b=='k')
			{
				currans='j';
				if (currz=='-')
			      currz='+';
			    else 
		    	  currz='-';
			}
		}
		if (a=='j')
		{
			if (b=='i')
			{
			    if (currz=='-')
			      currz='+';
			    else 
		    	  currz='-';
		    	currans='k';
			}
			if (b=='k')
			{
				currans='i';
			}
		}
		if (a=='k')
		{
			if (b=='i')
			{
				currans='j';
			}
			if (b=='j')
			{
				currans='i';
				if (currz=='-')
			      currz='+';
			    else 
		    	  currz='-';
			}
		}
		if (a=='1')
		{
			currans=b;
		}
	 }
}
int main()
{
	int t,q,x,l,i,e,k,n;
	string st,st0,res;
	char c;
	cin >> t;
	for (q=1;q<=t;q++)
	{
		cin >> l >> x;
		st0.clear();
		st.clear();
		res.clear();
		cin >> st0;
		st=st0;
		for(i=2;i<=x;i++)
		{
			st=st+st0;
		}
		n=st.length();
		currans='1';
		currz='+';
		i=0;
		e=0;
		while(e==0 && i<n)
		{
			c=currans;
			multiply_q(c,st[i]);
			if (currans=='i' && currz=='+') 
			{
				e=1;
			}
			i++;
		}
		currans='1';
		currz='+';
		while(e==1 && i<n)
		{
			c=currans;
		    multiply_q(c,st[i]);
			if (currans=='j' && currz=='+') 
			{
				e=2;
			}	
			i++;
		}
		currans='1';
		currz='+';
		while(e==2 && i<n)
		{
			c=currans;
		    multiply_q(c,st[i]);
			if (currans=='k' && currz=='+') 
			{
				e=3;
			}
			i++;	
		}
		k=0;
		res="NO";
		currans='1';
		currz='+';
		while(e==3 && i<n)
		{
			c=currans;
			multiply_q(c,st[i]);
			i++;
			k=1;
		}
		if (i==n && e==3)
		{
			if (k=0) 
			{
				res="YES";
			}
			else 
			{
				if (currans=='1' && currz=='+')
				{
					res="YES";
				}
			}
		}
		cout << "Case #" << q << ": " << res << "\n";
	}
	return 0;
}
