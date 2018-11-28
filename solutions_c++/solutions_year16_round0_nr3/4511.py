#include <iostream>
#include <string>
#include <math.h>

using namespace std;

long long make_num(string num,int base)
{
	long long res=0;
	for(int s=0;s<num.size();s++)
	{
		int temp = num[s]-48;
		//cout << temp << "\n";
		res = res+temp*pow(base,num.size()-s-1);
	}

	return res;
}

int main()
{
	int t;
	cin >> t;
	for(int i=1;i<=t; i++)
	{

		int n,j;
		cin >> n >> j;
		int checker = 0;
		long long li_num[9];
		string num;

		cout << "Case #" << i << ":\n";

		for(int m=0; m<pow(2,n-2);m++)
		{
			string lich_num = "000000000";
			int temp = m;
			num = "1";
			for(int a=n-3;a>=0;a--)
			{
				int dvd = temp / pow(2,a);
				if(dvd == 1)
				{
					num = num + "1";
					temp = temp - pow(2,a);
				}
				else
					num = num + "0";
			}
			num = num + "1";

			//cout << m << " " << num << "\n";

			for(int g=2; g<=10; g++)
			{
				
				long long ch_num = make_num(num,g);

				//cout << ch_num << "\n";
				for(long long h=2; h<sqrt(ch_num); h++)
				{
					if(ch_num%h==0)
					{
						li_num[g-2] = h;
						lich_num[g-2] = '1';
						break;
					}
				}
			}

			//cout << lich_num << "\n";

			if(lich_num == "111111111")
			{
				checker = checker + 1;
				cout << num << " " << li_num[0] << " " << li_num[1] << " "
				 << li_num[2] << " "  << li_num[3] << " " << li_num[4] << " "
				 << li_num[5] << " " << li_num[6] << " " << li_num[7] <<  " " << li_num[8] << "\n";
			}

			if(checker == j)
				break;

			
		}
	}
}