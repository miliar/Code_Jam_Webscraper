#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
	int t;
	cin>>t;	
		for(int k=1;k<=t;k++)
		{
			int smax,i,person_desired=0,total_available=0;
			cin>>smax;
			//fscanf(f1,"%d ",&smax);
			char s[smax+2];
			cin>>s;
			//fscanf(f1,"%s",s);
			for(i=0;s[i];i++)
			{
				if(total_available<i && s[i]!='0')
				{
					person_desired+=(i-total_available);
					total_available+=person_desired+s[i]-'0';
				}
				else
				{
					total_available+=(s[i]-'0');
				}
			}
			cout<<"Case #"<<k<<": "<<person_desired<<endl;
			//fprintf(f2,"Case #%d: %d\n",k,person_desired);
		}
	return 0;
}
