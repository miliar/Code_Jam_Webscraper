#include<bits/stdc++.h>
using namespace std;
int end_plus(char *ch,int l)
{
	int i;
	for(i=l;i>=0;i--)
	{
		//cout<<i;
		if(ch[i]!='+')
		break;
	}
	return i;
}
void minus_first(char *ch,int l)
{
	char x[l+1];
	int i,p=l;
	for(i=0;i<=l;i++)
	x[i]=ch[i];
	for(i=0;i<=l;i++)
	{
		//cout<<p<<" "<<ch[p]<<endl;
		if(x[p]=='+')
		ch[i]='-';
		else
		ch[i]='+';p-=1;
	}
}
void plus_first(char *ch,int l)
{
	int i;
	for(i=0;i<=l;i++)
	{
	if(ch[i]=='+')
	ch[i]='-';
	else
	break;
    }
}
int main()
{
	FILE *fout = freopen("output2.txt", "w", stdout);
	int t,l,i,k,f=1;
	char s[101];
	cin>>t;
	while(t--)
	{
		k=0;
		cin>>s;
		cout<<"Case #"<<f++<<": ";
		l=strlen(s);
		l=end_plus(s,l-1);
		if(l==-1)
		cout<<"0\n";
		else
		{
		while(l!=-1)
		{
		l=end_plus(s,l);
		if((s[0]=='-')&&(l!=-1))
		{
		minus_first(s,l);
		k++;
	    }
		else if((s[0]=='+')&&(l!=-1))
		{
		plus_first(s,l);
		k++;
	    }
	    }
	    cout<<k<<endl;
	    }
	    /*for(i=0;i<k;i++)
		cout<<s[i];
		cout<<endl;*/
	}
	return 0;
}
