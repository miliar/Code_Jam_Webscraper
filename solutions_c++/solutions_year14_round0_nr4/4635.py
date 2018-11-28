#include <iostream>

using namespace std;

class Blocks
{
	public:
	int N;
	double *mass_blocks;
	bool *is_blocks;
	
	int truth_win, deceitful_win;
	
	double blocks_current;
	
	Blocks (int N)
	{
		this->N = N; 
		mass_blocks = new double [N];		
		is_blocks = new bool [N];
		truth_win = 0;
		deceitful_win = 0;
	}
	~Blocks ()
	{
		delete mass_blocks;
		delete is_blocks;
	}
	
	void Block_Reading ()
	{
		for (int n = 0; n < N; n ++)
		{
			cin >> mass_blocks [n];
			for (int i = 0; i < N; i ++)
				is_blocks [i] = true;
		}
			
		for (int i=N-1; i>=0; i--)
		{
			for (int j=0; j<i; j++)
			{
				if (mass_blocks[j] > mass_blocks[j+1])
				{
					double tmp = mass_blocks[j];
					mass_blocks[j] = mass_blocks[j+1];
					mass_blocks[j+1] = tmp;
				}
			}	
		}
		
	}
	
	void Block_Writing ()
	{
		for (int n = 0; n < N; n ++)
		{
			cout << mass_blocks [n] << " ";
		}
		cout << endl;
	}
	
	double Blocks_take (int i)
	{
		if ( is_blocks [i] == false )
			return 0;
		else
		{
			is_blocks[i] = false;
			blocks_current = mass_blocks [i];
			return mass_blocks [i]; 
		}
	}
	
	int Blocks_Min ()
	{
		/*int min = 0;
		double min_mass = 2.0;
		for (int i = 0; i < N; i ++)
		{
			if ( mass_blocks[i] <= min_mass && is_blocks[i] == true )
			{
				min_mass = mass_blocks[i];
				min = i;
			}
		}*/
		for (int i = 0; i < N; i ++)
		{
			if ( is_blocks[i] == true )
				return i;
		}

	}
	
	
};


int main ()
{
	int T, N;
	cin >> T;
	//cout << "T = " << T << endl;
	
	for (int t = 0; t < T; t ++)
	{
		cin >> N;
		Blocks Blocks_Naomi (N), Blocks_Ken (N);
		Blocks_Naomi.Block_Reading ();
		Blocks_Ken.Block_Reading ();
		
		//cout << N << endl;
		//Blocks_Naomi.Block_Writing ();
		//Blocks_Ken.Block_Writing ();
		
		// Truth War
		//cout << "=====================Truth War" << endl;
		for (int i = 0; i < N; i ++)
		{
			bool flag = false;
			Blocks_Naomi.Blocks_take (Blocks_Naomi.Blocks_Min ());
			//cout << "Naomi = " << Blocks_Naomi.Blocks_take (Blocks_Naomi.Blocks_Min ()) << "\t";
			for (int i = 0; i < N; i ++)
			{
				if ( Blocks_Ken.mass_blocks[i] > Blocks_Naomi.blocks_current && Blocks_Ken.is_blocks[i] == true )
				{
					Blocks_Ken.Blocks_take (i);
					//cout << "Ken = " << Blocks_Ken.Blocks_take (i) << "\t";
					//cout << "Ken Win!" << endl;
					Blocks_Ken.truth_win ++;
					flag = true;
					break;
				}
			}
			if ( flag == false )
			{
				Blocks_Ken.Blocks_take (Blocks_Ken.Blocks_Min ());
				//cout << "Ken = " << Blocks_Ken.Blocks_take (Blocks_Ken.Blocks_Min ()) << "\t";
				//cout << "Naomi Win!" << endl;
				Blocks_Naomi.truth_win ++;
			}
		}
		
		// Recovery is_blocks
		for (int i = 0; i < N; i ++)
		{
			Blocks_Ken.is_blocks[i] = true;
			Blocks_Naomi.is_blocks[i] = true;
		}
		// Deceitful War
		//cout << "=====================Deceitful War" << endl;
		if ( Blocks_Ken.mass_blocks[0] == 0.0 )
		{
			Blocks_Ken.Blocks_take (0);
			Blocks_Naomi.Blocks_take (0);
			//cout << "Ken = " << Blocks_Ken.Blocks_take (0) << "\t";
			//cout << "Naomi = " << Blocks_Naomi.Blocks_take (0) << "\t";
			//cout << "Naomi Win!" << endl;
			Blocks_Naomi.deceitful_win ++;
			
			
			for (int i = 1; i < N; i ++)
			{
				bool flag = false;
				// Ken min mass
				if ( Blocks_Ken.is_blocks[i] == true )
				{
					Blocks_Ken.Blocks_take (i);
					//cout << "Ken = " << Blocks_Ken.Blocks_take (i) << "\t";
				}
				
				// Naomi min mass > Ken min mass
				for (int i = 1; i < N; i ++)
				{
					if ( Blocks_Naomi.mass_blocks[i] > Blocks_Ken.blocks_current && Blocks_Naomi.is_blocks[i] == true )
					{
						Blocks_Naomi.Blocks_take (i);
						//cout << "Naomi = " << Blocks_Naomi.Blocks_take (i) << "\t";
						//cout << "Naomi Win!" << endl;
						Blocks_Naomi.deceitful_win ++;
						flag = true;
						break;
					}
				}
				if ( flag == false )
				{
					Blocks_Naomi.Blocks_take (Blocks_Naomi.Blocks_Min ());
					//cout << "Naomi = " << Blocks_Naomi.Blocks_take (Blocks_Naomi.Blocks_Min ()) << "\t";
					//cout << "Ken Win!" << endl;
					Blocks_Ken.deceitful_win ++;
				}
			}
		}
		else
		{
			for (int i = 0; i < N; i ++)
			{
				bool flag = false;
				// Ken min mass
				if ( Blocks_Ken.is_blocks[i] == true )
				{
					Blocks_Ken.Blocks_take (i);
					//cout << "Ken = " << Blocks_Ken.Blocks_take (i) << "\t";
				}
				
				// Naomi min mass > Ken min mass
				for (int i = 0; i < N; i ++)
				{
					if ( Blocks_Naomi.mass_blocks[i] > Blocks_Ken.blocks_current && Blocks_Naomi.is_blocks[i] == true )
					{
						Blocks_Naomi.Blocks_take (i);
						//cout << "Naomi = " << Blocks_Naomi.Blocks_take (i) << "\t";
						//cout << "Naomi Win!" << endl;
						Blocks_Naomi.deceitful_win ++;
						flag = true;
						break;
					}
				}
				if ( flag == false )
				{
					Blocks_Naomi.Blocks_take (Blocks_Naomi.Blocks_Min ());
					//cout << "Naomi = " << Blocks_Naomi.Blocks_take (Blocks_Naomi.Blocks_Min ()) << "\t";
					//cout << "Ken Win!" << endl;
					Blocks_Ken.deceitful_win ++;
				}
			}
		}
		
		
		
		cout << "Case #"<< t+1 <<": " << Blocks_Naomi.deceitful_win << " " << Blocks_Naomi.truth_win << endl;
		
		
		
		/*for (int i = 0; i < N; i ++)
		{
			bool flag = false;
			if ( Blocks_Ken.mass_blocks[i] > 0.0 && Blocks_Ken.is_blocks[i] == true )
			{
				cout << "Ken = " << Blocks_Ken.Blocks_take (i) << "\t";
				flag = true;
				break;
			}
			if ( flag == false )
			{
				cout << "Ken = " << Blocks_Ken.Blocks_take (Blocks_Ken.Blocks_Min ()) << "\t";
			}
			
			flag = false;
			for (int i = 0; i < N; i ++)
			{
				if ( Blocks_Naomi.mass_blocks[i] > Blocks_Ken.blocks_current && Blocks_Naomi.is_blocks[i] == true )
				{
					cout << "Naomi = " << Blocks_Naomi.Blocks_take (i) << "\t";
					cout << "Naomi Win!" << endl;
					flag = true;
					break;
				}
			}
			if ( flag == false )
			{
				cout << "Naomi = " << Blocks_Naomi.Blocks_take (Blocks_KenZ.Blocks_Min ()) << "\t";
				cout << "Ken Win!" << endl;
			}
		}*/
		
		
		
		
		
		/*
		for (int i = 0; i < N; i ++)
		{
			cout << "Naomi Min = " << Blocks_Naomi.Blocks_take (Blocks_Naomi.Blocks_Min ()) << "\t";
			cout << "Ken Min = " << Blocks_Ken.Blocks_take (Blocks_Ken.Blocks_Min ()) << "\t";
			if ( Blocks_Naomi.blocks_current > Blocks_Ken.blocks_current )
				cout << "Naomi Win!" << endl;
			else
			{
				cout << "Ken Win!" << endl;
			}
		}
		*/
		
	}
	
	
	return 0;
}
