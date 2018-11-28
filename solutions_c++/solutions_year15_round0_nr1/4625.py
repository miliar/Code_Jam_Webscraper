#include <iostream.h>
#include <stdio.h>
int main()
{freopen("A-large.in","r",stdin);
freopen("ol.out","w",stdout);
int t,j;
cin>>t;
for(j=0;j<t;j++)
{int n;char s[1001];int i; int count=0;int total;
 cin>>n;
 n+=1;
 cin>>s;
 total=(int)s[0]-48;
 for(i=1;i<n;i++)
     {
      if(i>total)
	 {count+=(i-total);
	 total+=(i-total);}
     total+=((int)s[i]-48);
 }
 cout<<"Case #"<<j+1<<": "<<count<<"\n";
}
return 0;
}
