#include <iostream>
using namespace std;

int main() {
	int t, a[4][4],b[4][4],i,j,f1,f2,k,z=1;
	cin>>t;
	while(t--)
	{
		cin>>f1;
		for(i = 0 ; i < 4 ; i++)
			for(j = 0 ; j < 4 ; j++)
				scanf("%d",&a[i][j]);
		cin>>f2;	
		for(i = 0 ; i < 4 ; i++)
			for(j = 0 ; j < 4 ; j++)
				scanf("%d",&b[i][j]);
				
		f1--;
		f2--;
		int count = 0;
		int m;
		i = f1;
		j = f2;
		
		for(k = 0 ; k < 4; k++)
		{
			for(m = 0 ; m < 4 ; m++)
				if( a[i][k] == b[j][m])
				{
					f1 = a[i][k];
					count++;
				}
		}
		
		if(count == 1)
			printf("Case #%d: %d\n",z,f1);
		else if(count < 1)
			printf("Case #%d: Volunteer cheated!\n",z);
		else
			printf("Case #%d: Bad magician!\n",z);
		z++;	
		
	}
	return 0;
}