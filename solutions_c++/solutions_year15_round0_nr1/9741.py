#include <iostream>
#include<fstream>
using namespace std;

int main() {
  freopen("in", "r", stdin);
  freopen("out3", "w", stdout);
  int tt;
  scanf("%d", &tt);
  for (int qq=1;qq<=tt;qq++) {
    printf("Case #%d: ", qq);
    int smax; 	 
	scanf("%d",&smax);
	int frnd=0;double a;
	int am[smax];
	cin>>a;
	//cout<<a<<endl;
	int i=smax;
	while(a>0 && i>=0)
	{
		int rem = (int)a%10;
		am[i]=rem;
		 //cout<<rem;
		a=a/10;		
	--i;
	}
	int stand=0,khade=0;
	for(i=0;i<=smax;i++)
	{
		stand=stand+am[i]+frnd;
if(stand<i+1 && am[i+1]!=0)
{
	frnd=i+1-stand;
		khade+=frnd;
	}}
  printf("%d\n",khade);
}
  return 0;
}
