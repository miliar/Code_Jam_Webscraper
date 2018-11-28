#include <bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin>>t;
	for(int Case=1;Case<=t;Case++)
	{
		int max;
		cin>>max;
		char s[1009];
		scanf("%s",s);
		int people_standing=(int)s[0]-48;
		// cout<<people_standing;
		int apne_aadmi=0;
		int x=0;
		for(int i=1;s[i]!='\0';i++)
		{
			if(i>people_standing)
			{
				x=i-people_standing;
				// cout<<x<<" ";
				people_standing+=x+(s[i]-48);
				apne_aadmi+=x;
			}
			else
			{
				people_standing+=int(s[i]-48);
			}
			// cout<<people_standing<<" ";
			
			
		}
		cout<<"Case #"<<Case<<": "<<apne_aadmi<<endl;
		
	}
	
	return 0;
}