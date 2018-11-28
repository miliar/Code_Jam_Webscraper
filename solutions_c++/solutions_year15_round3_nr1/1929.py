#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
	int ans,i,j,r,c,w,s,n;
    freopen("abc.in","rt",stdin);
    freopen("abc.out","wt",stdout);
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
    	cin>>r>>c>>w;
    	if(c%w==0)
    		s= ((c/w)*r) + w-1;
    	else
    		s=(((c/w+1))*r) + w-1;
    	cout<<"Case #"<<i+1<<": "<<s<<endl;
    }

   return 0;
}
