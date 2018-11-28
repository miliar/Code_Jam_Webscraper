#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

int main()
{
	ofstream output;
	ifstream input;
	input.open("input.txt");
	output.open("output.txt");


	int T;
	input >> T;
	int n;
	double* a, *b, *aa, *bb;

	int x1, x2;
	int y1, y2;
	int ans2 = 0, ans1=0;

	for (unsigned t = 0; t<T; ++t)
	{
		input >> n;
		a = new double[n];
		b = new double[n];
		for (int i = 0; i < n; i++)
		{
			input >> a[i];
		}
		for (int i = 0; i < n; i++)
		{
			input >> b[i];
		}
		sort(a, a + n);
		sort(b, b + n);
		
		/*
	for (int i = 0; i < n; i++)
		{
			cout<< a[i]<<' ';
		}cout << endl;
		for (int i = 0; i < n; i++)
		{
			cout << b[i] << ' ';
		}cout << endl<<endl;
		*/
//		aa = new double[n];
//		bb = new double[n];
//		memcpy(aa, a, sizeof(double)*n);
//		memcpy(bb, b, sizeof(double)*n);


		x1 = 0, x2 = n - 1;
		y1 = 0, y2 = n - 1;
		ans1 = 0;

/*		while (x1 < x2)
		{
			if (a[x2]>b[y2])
			{
				ans1++;
				x2--;
				y1++;
			}
			else
			{
				y2--;
				x1++;
			}
		}
*/
		while ((x2 >= x1) && (y2>=y1))
		{
			if (a[x1] < b[y1])
			{
	
//				ans1 += 1;
//				x2--;
				x1++;
				y2--;
			}
			else
			{
				y1++;
				x1++;
				ans1++;
			}
		}



		x1 = 0, x2 = n - 1;
		y1 = 0, y2 = n - 1;
		ans2 = 0;
		while ((x1 <= x2) && (y1<=y2))
		{
			if (a[x2] > b[y2])
			{
				ans2 += 1;
				x2--;
				y1++;
			}
			else
			{
				x2--;
				y2--;
			}
			
		}


		output << "Case #" << t + 1 << ": "<<ans1<<" "<<ans2;
		output << "\n";
		delete[] a;
		delete[] b;
	}




	input.close();
	output.close();
	//	system("pause");
	return 0;
}
