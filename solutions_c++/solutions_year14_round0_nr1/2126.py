#include "cstdio"
int n,k1,k2,x,z[5],tab1[20],tab2[20];
bool ok;
int main()
{
	scanf ("%d", &n);
	for (int i=0; i<n; i++)
	{
		scanf ("%d", &k1);
		for (int j=0; j<16; j++) scanf ("%d", &tab1[j]);
		scanf ("%d", &k2);
		for (int j=0; j<16; j++) scanf ("%d", &tab2[j]);
		
		x=0;
		for (int j=(k1-1)*4; j<((k1-1)*4)+4; j++) z[x]=tab1[j],x++;
		
		x=0,ok=false;
		for (int j=(k2-1)*4; j<((k2-1)*4)+4; j++)
		{
			if (tab2[j]==z[0] || tab2[j]==z[1] || tab2[j]==z[2] || tab2[j]==z[3])
			{
				if (x!=0)
				{
					ok=true;
					break;
				}
				x=tab2[j];
			}
		}
		if (ok) printf ("Case #%d: Bad magician!\n", i+1);
		else if (x==0) printf ("Case #%d: Volunteer cheated!\n", i+1);
		else printf ("Case #%d: %d\n", i+1, x);
	}
	
	return 0;
}