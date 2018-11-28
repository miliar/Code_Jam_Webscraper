#include <iostream>
#include <algorithm>

int tab[100000009];
int INF=100000009;
int odp(int i);
int reve(int i);
int highest=0;

using namespace std;
int main()
{
	int ilez;
	cin>>ilez;
	int i;
	for(int aa=0; aa<ilez; aa++)
	{
		cin>>i;
		highest=0;
		cout<<"Case #"<<aa+1<<": "<<odp(i)<<endl;
		for(int i=0; i<=highest; i++)
		{
			tab[i]=0;
		}
	}
}
int odp(int i)
{

	highest=max(highest, reve(i));
	highest=max(highest, i);

	
	if(i==1) return 1;
	if(tab[i]!=0) return tab[i];
	tab[i]=i;
	tab[i]=min(odp(reve(i))+1, odp(i-1)+1);
	return tab[i];
}
int reve(int i)
{
	string s=to_string(i);
	if(s.back()=='0') return i;
	reverse(s.begin(), s.end());
	return atoi(s.c_str());
}
