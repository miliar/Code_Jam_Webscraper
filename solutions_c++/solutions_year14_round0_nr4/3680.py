#include<iostream>
#include<fstream>

using namespace std;

double find_largest ( double arr[] , int size , int & index )
{
	double largest = arr[0];
	for ( int i = 0 ; i < size ; i++ )
	{
		if ( arr[i] != -99 )
			largest = arr[i];
	}
	for ( int i = 0 ; i < size ; i++ )
	{
		if ( largest < arr[i] && arr[i] != -99 )
		{
			largest = arr[i];
		}
	}

	for ( int i = 0 ; i< size ; i++ )
	{
		if ( largest == arr[i] )
		{
			index = i;
		}
	}
	return largest;
}

double find_smallest ( double arr[] , int size , int & index )
{
	double largest = arr[0];
	for ( int i = 0 ; i < size ; i++ )
	{
		if ( arr[i] != -99 )
			largest = arr[i];
	}
	
	for ( int i = 0 ; i < size ; i++ )
	{
		if ( largest > arr[i] && arr[i] != -99)
		{
			largest = arr[i];
		}
	}

	for ( int i = 0 ; i< size ; i++ )
	{
		if ( largest == arr[i] )
		{
			index = i;
		}
	}
	return largest;
}

void bubbleSort ( double arr[] , int size )
{
	for ( int j = 0 ; j < size - 1 ; j++ )
	{
		for ( int i = 0 ; i < size -1 ; i++ )
		{
			if ( arr[i] > arr[i+1] )
			{
				double temp = arr[i];
				arr[i] = arr[i+1];
				arr[i+1] = temp;
			}
		}
	}
}

int main ()
{
	ifstream fin ( "D-large.in" );
	ofstream fout ( "outD.txt" );

	if ( !fin )
	{
		cout << "Error! File not found." << endl;
		exit(0);
	}

	int cases;
	fin >> cases;

	for ( int p= 0 ; p < cases ; p++ )
	{
		int n;
		fin >> n;
		double * naomi = new double [n];
		double * ken = new double [n];
		double * n1 = new double [n];
		double * k1 = new double [n];

		for ( int i = 0 ; i < n ; i++ )
		{
			fin >> naomi[i];
		}

		for ( int i = 0 ; i < n ; i++ )
		{
			fin >> ken[i];
		}

		bubbleSort ( naomi , n );
		bubbleSort ( ken , n );
		
		for ( int i = 0 ; i < n ;i++)
		{
			//cout << naomi[i] << " " ;
			n1[i] = naomi[i];
			k1[i] = ken[i];
		}
		//cout << endl;

		for ( int i = 0 ; i < n ;i++)
		{
			//cout << ken[i] << " " ;
		}
		//cout << endl;
		//   War............

		int war = 0 , decit_war = 0;
		for ( int i = 0 ; i < n ; i++ )
		{
			int index;
			double chosen_naomi , chosen_ken;
			
			chosen_naomi = find_largest ( naomi , n , index );
			naomi[index] = -99;
			if ( chosen_naomi > find_largest ( ken , n , index ) )
			{
				chosen_ken = find_smallest ( ken , n , index );
				ken[index] = -99;
			}
			else
			{
				int a = 0;
				for ( int j = 0 ; j < n ; j++ )
				{
					if ( ken[j] > chosen_naomi )
					a++;
				}
				double * temp = new double[a];

				int t = 0;
				for ( int i = 0 ; i < n ; i++ )
				{
					if ( ken[i] > chosen_naomi && ken[i] != -99 )
					{
						temp[t] = ken[i];
						t++;
					}
				}

				chosen_ken = find_smallest ( temp , a , index );

				for ( int i = 0 ; i < n ; i++ )
				{
					if ( chosen_ken == ken[i] )
					{
						ken[i] = -99;
					}
				}

			}
			
			if ( chosen_naomi > chosen_ken )
			{
				war ++;
			}
		}
		for ( int p = 0 ; p < n ; p++ )
		{
			int index;
			double ch1 , ch2 , told;
			// decit war......
			double l = find_largest ( k1 , n , index );
			int a = 0;
				for ( int j = 0 ; j < n ; j++ )
				{
					if ( n1[j] > l && n1[j] != -99)
					a++;
				}
				if ( a == 0 )
				{
					told = find_largest ( n1 , n , index );
					ch1 = find_smallest( n1 , n , index );
					n1[index] = -99;
				}
				else
				{
					double * temp = new double[a];

					int t = 0;
					for ( int i = 0 ; i < n ; i++ )
					{
						if ( n1[i] > l && n1[i] != -99 )
						{
							temp[t] = n1[i];
							t++;
						}
					}

					told = find_smallest ( temp , a , index );

					double s = find_smallest ( k1 , n , index );
					for ( int j = 0 ; j < n ; j++ )
					{
						if ( n1[j] > s && n1[j] != -99 )
						{
							ch1 = n1[j];
							n1[j] = -99;
							break;
						}
					}
				}

				if ( told > find_largest ( k1 , n , index ) )
				{
					ch2 = find_smallest ( k1 , n , index );
					k1[index] = -99;
				}
				else
				{
					int a = 0;
					for ( int j = 0 ; j < n ; j++ )
					{
						if ( k1[j] > told  && k1[j] != -99)
						a++;
					}
					double * temp = new double[a];

					int t = 0;
					for ( int i = 0 ; i < n ; i++ )
					{
						if ( k1[i] > told && k1[i] != -99 )
						{
							temp[t] = k1[i];
							t++;
						}
					}

					ch2 = find_smallest ( temp , a , index );

					for ( int i = 0 ; i < n ; i++ )
					{
						if ( ch2 == k1[i] )
						{
							k1[i] = -99;
						}
					}
					

				}
				if ( ch1 > ch2 )
				{
					decit_war++;
				}
				
		}
		fout << "Case #" <<  p + 1 << ": " << decit_war << " " << war << endl;
		
	}
	fin.close();
	fout.close();

	
	return 0;
}