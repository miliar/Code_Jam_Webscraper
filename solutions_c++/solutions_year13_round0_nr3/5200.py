#include<iostream>
#include<cmath>


using namespace std;

int main()
{
	int casos, num[10], cont=1, resps = 0, flag, num2, i, j, k, aux, n1, n2, tam, aux2;
	int tam1, tam2;
	

	cin >> casos;
	
	while(casos--)
	{
		cin >> n1 >> n2;

		resps = 0;
		for(i=n1; i<=n2; i++)
		{
			flag  = 1;
			aux = i;
			j = 0;
			while(aux > 0)
			{
				num[j] = aux%10;
				aux= aux/10;
				j++;
			}

			k = j/2;

			j--;
			for(tam = 0; tam<k; tam++, j--)
			{
				if(num[tam] != num[j])
				{	
					flag = 0;

					break;
				}
			}


			if(flag == 0)
				continue;

			else
			{
				num2 = sqrt(i);
				if((num2*num2) == i)
				{
					j =0;
					aux2 = num2;
					while(aux2 > 0)
					{
						num[j] = aux2%10;
						aux2= aux2/10;
						j++;
					}
					k = j/2;
					j--;
					for(tam = 0; tam<k; tam++, j--)
					{
						if(num[tam] != num[j])
						{
							flag = 0;
							break;
						}
					}

					if(flag == 1)
						resps++;
				}
			}
		}
		
		cout << "Case #" << cont << ": " << resps << endl;
		cont++;
	}
return 0;
}
							
	
