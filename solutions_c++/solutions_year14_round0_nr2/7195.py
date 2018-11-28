#include <iostream>
#include <stdio.h>
using namespace std;
int main ()
{
	int t,tt=1;
	FILE *fp;
	fp=fopen("output.txt","w");
	cin>>t;
	while(t--)
	{
		double c,f,x,v=2,t=0;
        cin>>c>>f>>x;
        while(x/v>c/v+x/(v+f))
		{
			t+=c/v;
			v+=f;
		}
		t+=x/v;
		fprintf(fp,"Case #%d: %.7lf\n",tt,t);
		/*if(n==1) cout<<"Case #"<<tt<<": "<<ans<<endl;
		else if(n>1) cout<<"Case #"<<tt<<": Bad magician!"<<endl;
		else cout<<"Case #"<<tt<<": Volunteer cheated!"<<endl;*/
		tt++;
	}
	fclose(fp);
	return 0;
}
