#include<iostream>
#include<algorithm>

using namespace std;

int main()
{
	int no_of_tests;
	int no_of_weights[100];
	float naomi[1000];
	float ken[1000];
	bool present_ken[1000];
	
	cin>>no_of_tests;
	for(int i = 0; i < no_of_tests; i++)
	{
		cin>>no_of_weights[i];
		for(int j = 0; j < no_of_weights[i]; j++)
			cin>>naomi[j];

		for(int j = 0; j < no_of_weights[i]; j++)
		{
			cin>>ken[j];
			present_ken[j] = true;
		}
	
		sort(naomi, naomi + no_of_weights[i]);
		sort(ken, ken + no_of_weights[i]);

		int naomi_pos = 0;
		int ken_pos = 0;	
		int naomi_deceit = 0;
		int flag;
		while(ken_pos < no_of_weights[i])
		{
			flag = 0;
			while(naomi_pos < no_of_weights[i])
			{
				if(naomi[naomi_pos] > ken[ken_pos])
				{
					naomi_deceit++;	
					naomi_pos++;	
					flag++;		
					break;
				}
				naomi_pos++;
			}			

			if(flag == 0)
				 break;
				
			ken_pos++;
		}	

		int ken_war = 0;
		for(naomi_pos = no_of_weights[i] - 1; naomi_pos >= 0; naomi_pos--)
		{
			for(ken_pos = 0; ken_pos < no_of_weights[i]; ken_pos++)
			{
				if((ken[ken_pos] > naomi[naomi_pos]) && (present_ken[ken_pos]))
				{
					ken_war++;
					present_ken[ken_pos] = false;
					break;	
				}	
			}	
		
		}	
		
		cout<<"Case #"<<i+1<<": "<<naomi_deceit<<" "<<no_of_weights[i] - ken_war<<'\n';
	}

	return 0;	

}
