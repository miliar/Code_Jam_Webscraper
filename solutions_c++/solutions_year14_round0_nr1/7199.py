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
		int a,b,aa[5][5],bb[5][5],n=0,ans;
		cin>>a;
		for(int i=1;i<=4;i++)
			for(int j=1;j<=4;j++) cin>>aa[i][j];
        cin>>b;
        for(int i=1;i<=4;i++)
			for(int j=1;j<=4;j++) cin>>bb[i][j];
		for(int i=1;i<=4;i++)
            for(int j=1;j<=4;j++)
				if(aa[a][i]==bb[b][j])
				{
					n++;
                    ans=aa[a][i];
				}
		if(n==1) fprintf(fp,"Case #%d: %d\n",tt,ans);
		else if(n>1) fprintf(fp,"Case #%d: Bad magician!\n",tt);
		else fprintf(fp,"Case #%d: Volunteer cheated!\n",tt);
		/*if(n==1) cout<<"Case #"<<tt<<": "<<ans<<endl;
		else if(n>1) cout<<"Case #"<<tt<<": Bad magician!"<<endl;
		else cout<<"Case #"<<tt<<": Volunteer cheated!"<<endl;*/
		tt++;
	}
	fclose(fp);
	return 0;
}
