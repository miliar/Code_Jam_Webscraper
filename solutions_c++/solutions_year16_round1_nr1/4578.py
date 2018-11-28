#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define pf push_front
deque <char> q;
deque <char> :: iterator it;
int main()
{
	string s;
	int i,t,j,k;
	int maxi;
	scanf ("%d",&t);
	int e=1;
	while (t--)
	{
		cin>>s;
		q.clear();
		j=s.length();
		//for (i=0;i<30;i++)
		//[i]=0;
		maxi=INT_MIN;
		for (i=0;i<j;i++)
		   {
		   	k=s[i];
		   	maxi=max (maxi,k);
		   	if (k==maxi)
		   	q.pf(s[i]);
		   	else
		   	q.pb(s[i]);
		   }
		   printf ("Case #%d: ",e++);
		   for (it=q.begin();it!=q.end();it++)
		   printf ("%c",*it);
		   printf ("\n");
		/*or (i=25;i>=0;i--)
		{
			if (!a[i])
			continue;
			while (a[i]--)
			printf ("%c",(char)i+65);
		}*/
		//printf ("\n");
	}
	return 0;
}
	