#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

int main()
{
	int t;
	freopen("D-small-attempt2.in","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>t;
    for(int tc=1;tc<=t;tc++)
    {
    	int n;

    	cin>>n;
    	double na[10],ke[10];
		bool v[10];
        for(int i=0;i<n;v[i++]=0);
        for(int i=0;i<n;i++)
            cin>>na[i];
        for(int i=0;i<n;i++)
            cin>>ke[i];
        sort(na,na+n);
        sort(ke,ke+n);
        int ans1=0,ans2=0;
        int s1=n-1,s2=n-1,e=0;
        while(s1>=e)
        {
            if(na[s1]>ke[s2])
            {
            	ans1++;
            	s1--;
            }
            else
            {
                e++;
            }
            s2--;
        }
        for(int i=0;i<n;i++)
            for(int j=0;j<n;j++)
                if((na[i]<ke[j])&&!v[j])
                {
                	v[j]=1;
                	ans2++;
                	break;
                }
        ans2=n-ans2;
        cout<<"Case #"<<tc<<": "<<ans1<<" "<<ans2<<"\n";
    }
	return 0;
}
