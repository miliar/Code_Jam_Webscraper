#include <iostream>
#include <string>
using namespace std;
int main()
{
	char ch[1005];
	int t, sm, i, t1=1, tot,ans;
	cin>>t;
	while(t1<=t)
	{
		ans=0;
		cin>>sm;
		cin>>ch[0];
		tot=ch[0]-'0';
		for(i=1;i<=sm;i++)
			{
				cin>>ch[i];
				if (ch[i]!='0')
				{
					if(tot>=i)
						tot+=(ch[i])-('0');
					else
						{
							ans+=(i-tot);
							tot=i+(ch[i])-('0');
						}
						//cout<<endl<<endl<<ans<<" "<<tot;
				}
			}
		

//cout<<sm<<" "<<ch[0]<<" "<<ch[1]<<endl;
		cout<<"Case #"<<t1<<": "<<ans<<endl;
		t1++;
	}
	

	return 0;
}
