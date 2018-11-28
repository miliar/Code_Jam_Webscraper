#include <bits/stdc++.h>

using namespace std;

int main()
{
	int n1;
	cin >> n1;
	for (int k = 0; k < n1; k++)
	{
		string s1;
		cin >> s1;
		
		list<char> v1;
		list<char>::iterator it;
		
		int tam = s1.size(), sum = 0, aux = 0;
		char c;
		int f = (int)s1[0];
		v1.push_front(s1[0]);
		for (int i = 1; i < tam; i++)
		{
			c = s1[i];
			aux = (int) c;
			f= v1.front();
			if(aux >= f)
			{
				v1.push_front(c);
				
			}
			else v1.push_back(c);
			
			sum += aux;
		}
		
		printf("Case #%d: ", k+1);
		
		for (it = v1.begin(); it != v1.end(); it++)
		{
			printf("%c",*it);
			
			
		}
		printf("\n");
		
		
		
		
		
	}
	
return 0;	
}
