#include<bits/stdc++.h>
using namespace std;
struct party{
	int mem;
	char c;
};
bool cmp(party a,party b)
{
	return a.mem>b.mem;
}
int main()
{
	int t,cs=0,i,n,left;

	scanf("%d",&t);
	while(t--)
	{
		cs++;
		scanf("%d",&n);
		
	vector<party> p;
	party m;
		
		for(i=0;i<n;i++)
		{
			scanf("%d",&m.mem);
			m.c = 'A'+i;
			p.push_back(m);
		}
		printf("Case #%d: ",cs);
		sort(p.begin(),p.end(),cmp);
		/*
		for(i=0;i<n;i++)
		{
			printf("%c%d  ",p[i].c,p[i].mem);
		}
		printf("\n");
		*/
		left = n;
		if(n%2==0)
		{
			vector<party>::iterator f,s;
		while(left!=0)
		{
			sort(p.begin(),p.end(),cmp);
			f = p.begin();
			s = f+1;
			if(f->mem==s->mem)
			{
					f->mem--;
					s->mem--;
					printf("%c%c ",f->c,s->c);
					if(f->mem==0)
						left--;
					if(s->mem==0)
						left--;				
			}
			else
			{
				if(f->mem%2!=0)
				{
					f->mem--;				
					printf("%c ",f->c);
				
				}
				else
				{
					f->mem-=2;				
					printf("%c%c ",f->c,f->c);
				}
					if(f->mem<=0)
						left--;
			}
		}
		}
		else
		{
			vector<party>::iterator f,s;
		while(left>=3)
		{
			sort(p.begin(),p.end(),cmp);
			f = p.begin();
			s = f+1;
			if((f->mem==1&&s->mem==1&&(s+1)->mem==1))
				break;
			if(f->mem==s->mem)
			{
					f->mem--;
					s->mem--;
					printf("%c%c ",f->c,s->c);
					if(f->mem==0)
						left--;
					if(s->mem==0)
						left--;				
			}
			else
			{
				if(f->mem%2!=0||f->mem==1+(f+1)->mem)
				{
					f->mem--;				
					printf("%c ",f->c);
				
				}
				else
				{
					f->mem-=2;				
					printf("%c%c ",f->c,f->c);
				}
					if(f->mem<=0)
						left--;
			}
		}
		/*
			int d = 0;
		while(d==0)
		{
			sort(p.begin(),p.end(),cmp);
			f = p.begin();
			if(f->mem%2!=0)
				{
					f->mem--;				
					printf("%c ",f->c);
				
				}
				else
				{
					f->mem-=2;				
					printf("%c%c ",f->c,f->c);

				}
					if(f->mem<=0)
					{
						left--;
						d=1;
						//cout<<" loner removed "<<left;
						break;

					}
			
		}
		*/
		sort(p.begin(),p.end(),cmp);
			f = p.begin();
			f->mem--;				
			printf("%c ",f->c);
			if(f->mem==0)
			left--;
		while(left!=0)
		{
			sort(p.begin(),p.end(),cmp);
			f = p.begin();
			s = f+1;
			if(f->mem==s->mem)
			{
					f->mem--;
					s->mem--;
					printf("%c%c ",f->c,s->c);
					if(f->mem==0)
						left--;
					if(s->mem==0)
						left--;				
			}
			else
			{
				if(f->mem%2!=0||f->mem == s->mem+1)
				{
					f->mem--;				
					printf("%c ",f->c);
				
				}
				else
				{
					f->mem-=2;				
					printf("%c%c ",f->c,f->c);
				}
					if(f->mem<=0)
						left--;
			}
		}

		}

		printf("\n");	


	}
}