#include<iostream>

using namespace std;

int main()
{
	int a, v[1010], n, m, cont = 1, contador, i, j, pos1, pos2, max, casos=1, flag;
	
	cin >> casos;
	while(casos--)
	{
		cin >> n >> m;
		for(i=0; i<n; i++)
			cin >> v[i];
			        	contador = 0;
		while(1)
        {  
        	flag = 0;

		    for(i=0; i<n; i++)
		    {
		    	if(v[i] != 0)
		    	{
		    		flag = 1;
		    		break;
		   		}
		   	}
		   	
		   	if(flag == 1)
		   	{
		   		max = 0;
		   		pos1 = -1;
		   		pos2 = -1;
		   		for(i=0; i<n; i++)
		   		{
		   			for(j=0; j<n; j++)
		   			{
		   				if(v[i] + v[j] > max && v[i] + v[j] <= m && i!=j)
		   				{
		   					pos1 =i;
		   					pos2 = j;
		   					max = v[i] + v[j];
		   				}
		   			}
		   		}
		   		
		   		if(pos1 == -1)
		   		{
		   			max = 0;
		   			for(i=0; i<n; i++)
		   			{
		   				if(v[i] > max)
		   				{
		   					max = v[i];
		   					pos1 = i;
		   				}
		   			}
		   			v[pos1] = 0;
		   			contador++;
		   		}
		   		else
		   		{
		   				
		   		
		   		//cout << "Peguei: " << pos1 << " " << pos2 << endl;
		   		
		   			v[pos1] = 0;
		   			v[pos2] = 0;
		   			contador++;
		   		}
		   	}
		   	else
		   		break;
		}	
			cout << "Case #" << cont << ": " << contador << endl;
			cont++;
	}
	
	return 0;
}	
		   		
		   		
		   		
		   		
		   					
		   		
		   		
		   		
		   		
		   		
