#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <vector>
#include <algorithm>


using namespace std; 


int D_War(vector<double> &Naomi, vector<double> &Ken);
int War(vector<double> &Naomi, vector<double> &Ken);


int main(int argc, char **argv)
{
	ifstream file("D-large.in", ifstream::in);
	ofstream out("output.in", ofstream::out);

	int T; 

	file >> T; 


	for(int i=0; i<T; i++)
	{

		int S; 
		file >> S; 

		vector<double> Naomi(S); 
		vector<double> Ken(S);

		for(int j=0; j<S; j++)
		{
			file >> Naomi[j]; 
		}
		for(int j=0; j<S; j++)
		{
			file >> Ken[j]; 
		}


/*
		double qwert[] = {0.186, 0.389, 0.907, 0.832, 0.959, 0.557, 0.300, 0.992, 0.899};
		vector<double> Naomi;
		for(int j=0; j<9; j++)
			Naomi.push_back(qwert[j]);

			double asdf[] = {0.916, 0.728, 0.271, 0.520, 0.700, 0.521, 0.215 ,0.341 ,0.458};
		vector<double> Ken; 
			for(int j=0; j<9; j++)
			Ken.push_back(asdf[j]);
*/
		sort(Naomi.begin(), Naomi.end());  // ascending order
		sort(Ken.begin(), Ken.end());   

		vector<double> Naomi_cpy(Naomi.begin(), Naomi.end());
		vector<double> Ken_cpy(Ken.begin(), Ken.end());

		int pointsA = D_War(Naomi, Ken);

		int pointsB = War(Naomi_cpy, Ken_cpy);



			out << "Case #" << i+1 << ": " << pointsA << " " << pointsB << endl;


	}




return 0; 
}


int War(vector<double> &Naomi, vector<double> &Ken)
{

	int points =0;

	while(!Naomi.empty())
	{
	 
		while((!Naomi.empty()) && (Naomi.front() >= Ken.back()))
		{

			if(Naomi.front() == Ken.back())
			{
				Naomi.erase(Naomi.begin());
				Ken.pop_back();
			}
			else
			{
				Naomi.erase(Naomi.begin());
				Ken.erase(Ken.begin());
				points++;
			}
		}

		for(unsigned i=0; i<Ken.size(); i++)
		{
			if(Ken[i] > Naomi[0])
			{
				Naomi.erase(Naomi.begin());
				Ken.erase(Ken.begin() + i);
				break;
			}
		}

	}



return points;
}





int D_War(vector<double> &Naomi, vector<double> &Ken)
{

	int points = 0; 
	



	while(!Naomi.empty())
	{

		//step 1
		//paikse ta mikrotera an exeis ksodeuontas tou ta megalytera
		while((!Naomi.empty()) && (Naomi.front() <= Ken.front()))
		{

			Naomi.erase(Naomi.begin());
			Ken.pop_back();

		}

		//step 2
		// paikse ta mikrotera sou legontas oti einai megala ksodeuontas ta mikrotera tou 
		while((!Naomi.empty()) && (Naomi.front() > Ken.front()) ) 
		{
			Naomi.erase(Naomi.begin());
			Ken.erase(Ken.begin());
			points++;
		}

	}

	return points; 
}
