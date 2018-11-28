#include <iostream>

using namespace std;

int main()
{
	int num;
	int originalnum;
	int test_times;
	int complete_times = 1;
	int output_num;

	cin >> test_times;

	while (0 < test_times) {
		int tenpower6 = 10;
		int tenpower5 = 10;
		int tenpower4 = 10;
		int tenpower3 = 10;
		int tenpower2 = 10;
		int tenpower1 = 10;
		int tenpower0 = 10;
		bool sexy_array[11] = { 0,0,0,0,0,0,0,0,0,0,0};
		while (true) {

			cin >> originalnum;
			if (!(originalnum <= 1000000 && originalnum >= 0))
				continue;
			else
				break;
		};

		num = originalnum;
		
		for (int i=1; i<=100; i++) {

			num= i*originalnum;
			output_num = num;

			
			if (num >= 1000000)
			{
				tenpower6 = num / 1000000;
				num -= 1000000 * tenpower6;
			}
// 1번째
			else if (num >= 100000)
				{
					tenpower5 = num / 100000;
					num -= 100000 * tenpower5;

					if (num >= 10000)
					{
						tenpower4 = num / 10000;
						num -= 10000 * tenpower4;

						if (num >= 1000)
						{
							tenpower3 = num / 1000;
							num -= 1000 * tenpower3;
							if (num >= 100)
							{
								tenpower2 = num / 100;
								num -= 100 * tenpower2;
								if (num >= 10)
								{
									tenpower1 = num / 10;
									num -= 10 * tenpower1;
									tenpower0 = num;
								}
							}
						}
					}
					else if (num >= 1000)
					{
						tenpower3 = num / 1000;
						num -= 1000 * tenpower3;
						if (num >= 100)
						{
							tenpower2 = num / 100;
							num -= 100 * tenpower2;
							if (num >= 10)
							{
								tenpower1 = num / 10;
								num -= 10 * tenpower1;
								tenpower0 = num;
							}
						}
					}
					else if (num >= 100)
					{
						tenpower2 = num / 100;
						num -= 100 * tenpower2;
						if (num >= 10)
						{
							tenpower1 = num / 10;
							num -= 10 * tenpower1;
							tenpower0 = num;
						}
					}
					else if (num >= 10)
					{
						tenpower1 = num / 10;
						num -= 10 * tenpower1;
						tenpower0 = num;
					}
					else
						tenpower0 = num;
				}

// 2번째
			else if (num >= 10000)
			{
				tenpower4 = num / 10000;
				num -= 10000 * tenpower4;
			if (num >= 1000)
			{
				tenpower3 = num / 1000;
				num -= 1000 * tenpower3;
				if (num >= 100)
				{
					tenpower2 = num / 100;
					num -= 100 * tenpower2;
					if (num >= 10)
					{
						tenpower1 = num / 10;
						num -= 10 * tenpower1;
						tenpower0 = num;
					}
				}
			}
			else if (num >= 100)
			{
				tenpower3 = 0;
				tenpower2 = num / 100;
				num -= 100 * tenpower2;
				if (num >= 10)
				{
					tenpower1 = num / 10;
					num -= 10 * tenpower1;
					tenpower0 = num;
				}
			}
			else if (num >= 10)
			{
				tenpower3 = 0;
				tenpower2 = 0;
				tenpower1 = num / 10;
				num -= 10 * tenpower1;
				tenpower0 = num;
			}
			else
				tenpower0 = num;
			}
// 3번째
			else if (num >= 1000)
			{
				tenpower3 = num / 1000;
				num -= 1000 * tenpower3;
				if (num >= 100)
				{
					tenpower2 = num / 100;
					num -= 100 * tenpower2;
					if (num >= 10)
					{
						tenpower1 = num / 10;
						num -= 10 * tenpower1;
						tenpower0 = num;
					}
					else {
						tenpower1 = 0;
						tenpower0 = num;
					}
				}
				else if (num >= 10)
				{
					tenpower2 = 0;
					tenpower1 = num / 10;
					num -= 10 * tenpower1;
					tenpower0 = num;
				}
				else
				{
					tenpower2 = 0;
					tenpower1 = 0;
					tenpower0 = num;
				}
			}
//4번째
			else if (num >= 100) {
				tenpower2 = num / 100;
				num -= 100 * tenpower2;
				if (num >= 10)
				{
					tenpower1 = num / 10;
					num -= 10 * tenpower1;
					tenpower0 = num;
				}
				else
				{
					tenpower1 = 0;
					tenpower0 = num;
				}
			}
			else if (num >= 10)
			{
				tenpower1 = num / 10;
				num -= 10 * tenpower1;
				tenpower0 = num;
			}
			else
				tenpower0 = num;

			sexy_array[tenpower6] = true;
			sexy_array[tenpower5] = true;
			sexy_array[tenpower4] = true;
			sexy_array[tenpower3] = true;
			sexy_array[tenpower2] = true;
			sexy_array[tenpower1] = true;
			sexy_array[tenpower0] = true;

			if (sexy_array[0] && sexy_array[1] && sexy_array[2] && sexy_array[3] && sexy_array[4] && sexy_array[5] && sexy_array[6] && sexy_array[7] && sexy_array[8] && sexy_array[9])
			{
				cout << "Case #" << complete_times << ": "<< output_num<<endl;
				break;
			}
			else if((i==100) && !(sexy_array[0] && sexy_array[1] && sexy_array[2] && sexy_array[3] && sexy_array[4] && sexy_array[5] && sexy_array[6] && sexy_array[7] && sexy_array[8] && sexy_array[9]))
			{
				cout << "Case #" << complete_times << ": " << "INSOMNIA" << endl;
				break;
			}
		}
		test_times--;
		complete_times++;
	};
}