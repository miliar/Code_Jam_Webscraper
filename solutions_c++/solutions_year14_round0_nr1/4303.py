#include <iostream>

using namespace std;

int main()
{
	int k,i;
	cin >> k;
	for(i=1;i<=k;i++)
	{
		int a,key,j,vet1[4],vet2[4];
		cin >> key;
		for(a=1;a<=4;a++)
		{
			if(a==key)
				cin >> vet1[0]>>vet1[1]>>vet1[2]>>vet1[3];
			else
			cin >> j >> j >> j >> j;	
		}
		cin >> key;
		for(a=1;a<=4;a++)
		{
			if(a==key)
				cin >> vet2[0] >> vet2[1] >> vet2[2] >> vet2[3];
			else
				cin >> j >> j >> j >> j;
		}
		int max=0,value;
		for(a=0;a<4;a++)
		{
			for(j=0;j<4;j++)
			{
				if(vet1[a]==vet2[j])
				{
					value = vet1[a];
					max++;
				}
			}
		}
		if(max==1)
			cout << "Case #" << i << ": " << value << endl;
		else if(max==0)
			cout << "Case #" << i << ": " << "Volunteer cheated!" << endl;
		else 
			cout << "Case #" << i << ": " << "Bad magician!" << endl; 				
	}
	return 0;
}
