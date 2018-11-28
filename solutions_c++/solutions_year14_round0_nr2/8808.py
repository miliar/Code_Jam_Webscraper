#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<iomanip>

using namespace std;



int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t,m;double  c, f, x,cookie,rate,time;
	cin >> t;
	for(int i = 1; i <= t; i++)
	{
		cookie = 0; rate = 2; time = 0; m = 2;
		cin >> c >> f >> x;

		if(c < x)
		{
			cookie += c;
			time +=  c/2;
		}

		else if(c>x)
		{
			time += x/2;
			m = 0;
		}


		while(m  !=0 )
		{

			if(((x - cookie) / rate) > ((x-cookie+c) / (rate + f)))
			{
				cookie -= c;
				rate += f;


			}

			
			if( (cookie+c) < x)
			{
				cookie += c;
				time += c/rate;
			}

			else if((cookie + c)>=x)
			{
				time += (x-cookie)/ rate;
				m = 0;
			}
			


		}

		cout << "Case #" << i << ": " << fixed << setprecision(7) << time << endl;








	}
	
	return 0;



}