#include <bits/stdc++.h>
using namespace std;
int main ()
{
freopen("input.txt","r", stdin);
freopen("out.txt", "w", stdout);
    int t,n,x,i,p=1;
    scanf("%d",&t);
    while(t--)
    {
    vector <pair <int,int> >v;
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
    	scanf("%d",&x);
    	v.push_back(make_pair(x,i));
    }	
    cout<< "Case #"<<p<<": ";
    p++;
while(1)
{
	sort(v.begin(),v.end());
	reverse(v.begin(),v.end());
	if(v[0].first>1&&v[1].first>1)
	{
		v[0].first=v[0].first-1;
		v[1].first=v[1].first-1;
		cout<<char('A'+v[0].second)<<char('A'+v[1].second)<<" ";
	}
	else if(v[0].first > 1)
		{v[0].first=v[0].first-1;
			cout<<char('A'+v[0].second)<<" ";}
    else if((v[0].first==1)&&(v[1].first==1)&&(v.size())==2)
    {
    	v[0].first=v[0].first-1;v[1].first=v[1].first-1;
    cout<<char('A'+v[0].second)<<char('A'+v[1].second)<<" ";	
    }  
    else
    {
    	v[0].first=v[0].first-1;
			cout<<char('A'+v[0].second)<<" ";
    } 

    if(v[0].first==0)
	v.erase(v.begin());
 if(v[0].first==0)
	v.erase(v.begin());
if(v.size()==0)
	break;
 }
cout<<"\n";
}
    return 0;
}