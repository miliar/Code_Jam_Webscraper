//revenge of the pancakes.cpp
#include <bits/stdc++.h>
using namespace std;

#define all(c) c.begin(),c.end()

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int t,nos,y;
	scanf("%d",&t);
	char ch_find;
	string str_temp,s1;
	string::iterator iter,iterf;
	getline(cin,str_temp);
	for(y=1;y<=t;y++)
	{
		nos=0;
		getline(cin,s1);
		iter=s1.begin();
		if(s1.length()!=1)
		{
		    while(find(all(s1),'-')!=s1.end())
		    {
			    iter=s1.begin();
			    if((*iter)=='-')
			        ch_find='+';
			    else ch_find='-';
			    iterf=find(all(s1),ch_find);
			    if(find(all(s1),'+')==s1.end())
			    {
			        nos++;
			        break;
			    }
			    while(iter!=iterf)
                    (*iter++)=(*iterf);
                nos++;
		    }
		}
		else
        {
            if((*iter)=='-')
            {
                nos++;
            }
        }
        cout<<"Case #"<<y<<": "<<nos<<endl;
        s1.clear();
	}

	return 0;
}
