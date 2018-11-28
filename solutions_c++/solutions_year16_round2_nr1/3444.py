#include<bits/stdc++.h>
using namespace std;
int hx[1000];
string s1[10]={"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };
vector<int> ans;
int fx=0;
void solve(int h[],vector<int> an)
{
	if(fx)
	return ;
	vector<int> v1=an;
	
	int f1=0;
	for(int i=0;i<100;i++)
	{
		if(h[i])
		f1=1;
	}
	if(f1==0)
	{
		fx=1;
		ans=an;
		return;
		
	
	}
	
		string s;
		int h1[126];
		for(int i=0;i<100;i++)
		h1[i]=h[i];
		int k;
		for(int i=0;i<10;i++)
		{
			if(fx)
			return;
			int f=0;
		s=s1[i];
		int l1=s.size();
			for(k=0;k<l1;k++)
			{
				if(!h1[s[k]])
				f=1;
			
			}
	if(!f)
		for(k=0;k<l1;k++)
		{
			h1[s[k]]--;
		
			
		}
		if(!f)
		{
		
			v1.push_back(i);
		//	cout<<i<<endl;
			solve(h1,v1);
			for(k=0;k<l1;k++)
		{
			h1[s[k]]++;
			
			
		}
		v1.pop_back();
		}
	}
	
	return;
}

int main()
{
	freopen("ins.in","r",stdin);
	freopen("out.out","w",stdout);
int t,cs=0;
cin>>t;
while(t--)
{
printf("Case #%d: ",++cs);
string s,s2;
int i,j,k,l;
cin>>s;

l=s.size();

for(i=0;i<l;i++)
{
	hx[s[i]]++;
}
solve(hx,ans);

/*
j=0;
for(i=0;i<l;i++)
{
	if(j<10)
	s2=s1[j++];
	
	int l1=s2.size();

	while(1)
	{
		int f=0;
		for(k=0;k<l1;k++)
		{
			if(!hx[s2[k]])
			f=1;
			
		}
		if(f)
		break;
		
		for(k=0;k<l1;k++)
		{
			hx[s2[k]]--;
			
			
		}
		ans.push_back(j-1);
		
	}
		
}
*/
sort(ans.begin(),ans.end());
for(i=0;i<ans.size();i++)
cout<<ans[i];
cout<<endl;

for(i=0;i<156;i++)
hx[i]=0;
fx=0;
ans.clear();
}
	return 0;
}
