# include <iostream>
# include <cstdio>
# include <iomanip>
using namespace std;
int K,L,S;
int w,v,y;
double ans;
string s1,s2;
void check(string s3)
{
	int i,j,k=0;
	bool flag=0;w++;
	if (s2.size()>s3.size())return;
	for (i=0;i<s3.size()-s2.size()+1;i++)
	{
		flag=1;
	    for (j=0;j<s2.size();j++)
	        if (s3[i+j]!=s2[j]){flag=0;break;
	        }
	    if (flag)k++;
	}
	v+=k;
	if (k>y)y=k;
//cout<<s3<<' '<<s2<<' '<<v<<endl;
}
void dfs(int x,string s3)
{
	if (x>S){
		check(s3);
		return;
	}
	int i;
	for (i=0;i<s1.size();i++)dfs(x+1,s3+s1[i]);
}
int main()
{
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	int i,q,t;
	cin>>q;
	for (i=1;i<=q;i++)
	{
		cin>>K>>L>>S>>s1>>s2;
		ans=w=v=y=0;
		dfs(1,"");
		ans=(double)(v)/(double)(w);
		ans=(double)(y)-ans;
		cout<<"Case #"<<i<<": "<<fixed<<setprecision(8)<<ans<<endl;
	}
	return 0;
} 
