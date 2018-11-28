#include <iostream>
using namespace std;
int main()
{
	int t, dig[10]={0}, allv=0, count=0;
	unsigned long long no[101], tmp, j=1, n[101];
	cin >> t ;
	for(int i=0; i<t; i++)
    {    cin >> no[i];
         n[i] = no[i]; 
	}
	
	for(int v=0 ; v<t; v++) 
	{ allv=0; j=1;
	  for(int x=0; x<10; x++) dig[x]=0;
	  while(allv!=1)
	  {	if(no[v]==0){ cout << "Case #" << v+1 << ": " "INSOMNIA" ; break; }
		no[v]=n[v]*j;
		j++;
		tmp = no[v];
		while(tmp!=0)
		{
			dig[tmp%10]=1;
			tmp = tmp/10;
		}
		for(int i=0; i<10; i++)
		{	if(dig[i]==1){ count++; }
		}
		if(count==10) allv=1;
		count =0;
	  }
	 if(no[v]!=0) cout << endl << "Case #" << v+1 << ": "  << no[v] ;
	}
	cin >> j ;
	return 0;
}
