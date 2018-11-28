#include<iostream>
#include<algorithm>
#include<string.h>
using namespace std;
int main()
{
    //freopen("raj1.txt", "r", stdin);
	//freopen("raj1.out", "w", stdout);
	int t;
	cin>>t;
	while(t--)
	{
	
int n,x=0,c,i,j,l,y=0;
char a[10000];
cin>>n;
cin>>a;
l=strlen(a);
for(i=0;i<l;i++)
{
	if(a[i]==0)
	continue;
    if(i<=x)
    x=x+(a[i]-'0');
     else
    {
	y=y+(i-x);
	//x=x+a[i]-'0'+i-x;
	x=x+y+(a[i]-'0');
		//x=x+a[i];
    }  

}
 cout<<y<<endl;
}
return 0;
}
