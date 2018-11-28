// GCJ_2016_R1_C.cpp : Defines the entry point for the console application.
//


#include "stdafx.h"

#include <iostream>
#include <vector>
#include <string>
#include <fstream>


using namespace std;

//string Alph = { 'A','B','C' };

int max = 0;
int premax = 0;

void Percent(vector<int> & v1, vector<float> & v2, int p)
{
	 max = 0;
	 premax = 0;

	// cout << "P  " << p << endl;

	 for (int i = 0;i < v1.size();++i)
	 {
		 v2[i] = (v1[i] * 100) / p;
		//cout << p << "  " << v1[i] << "  " << v2[i] << endl;;
	 }

	 for (int i = 0;i < v1.size();++i)
		if (v2[max] <= v2[i])
		{
			premax = max;
			max = i;
		}
	

}

int main()
{


	//ifstream in("input.txt");
	ifstream in("A-small-attempt1.in");
	ofstream out("result.txt");



	int TestCount = 0;
	in >> TestCount;


	

	for (int TestNumber = 1; TestNumber <= TestCount; ++TestNumber)
	{

		cout << "Test # " << TestNumber << endl;

		int N;

		in >> N;
		vector<int>senator(N);
		//cout <<"N  "<< N << endl;

		int p = 0;

		for (int i = 0;i < N;++i)
		{
			in >> senator[i];
			p += senator[i];
		}



		out << "Case #" << TestNumber << ": ";

		/*while (p > 0)
		{*/
			//cout << "P  " << p << endl;
			
			vector<float>per(N);
			
			Percent(senator, per, p);

			
				cout << "P  " << p << endl;
			while (p > 0)
			{
				cout << "P  " << p << endl;
				int f = -1, s = -1;
				float per1; 
				float per2;
				float per3;




				//for (int i = 0;i < N;++i)
				//	cout << senator[i] << "  ";
				//cout << endl;

				//for (int i = 0;i < N;++i)
				//	cout << per[i] << "  ";
				//cout << endl;

			//	bool b = false;

				senator[max]--;
				--p;
				f = max;
				per1 = per[max];
					

				if (p <= 0)
				{
					cout << "%A% "  << endl;
					out << (char)(65 + f) << " ";
					cout << (char)(65 + f) << endl;;
					break;
				}

				Percent(senator, per, p);

				/*if (per[max] >= 50)
					b = true;*/
				s = max;
				per2 = per[max];
				senator[max]--;
				--p;

				if (p <= 0)
				{
					cout << "%B% " << endl;
					out << (char)(65 + f) << (char)(65 + s) << " ";
					cout << (char)(65 + f) << (char)(65 + s) << endl;
					break;
				}

				Percent(senator, per, p);
				per3 = per[max];

				/*for (int i = 0;i < N;++i)
					cout<<per[i] << "  ";
				cout << endl;*/

				//cout << "f " << f << "  S  " << s <<"   "<<per1<<"  "<<per2<<" "<<per3<< "\n\n"<<endl;

				if (per3 >= 50.0 && per1 < 50.0)
				{
					cout << "%C% " << endl;
					if (per1 < 50.0)
					{
						cout << "%D% " << endl;
						++p;
						senator[s]++;
						out << (char)(65 + f) << " ";
						cout << (char)(65 + f) << " ";

					}
					
				}
				else
				{
					cout << "%E% " << endl;
					//p -= 2;
					out << (char)(65 + f) << (char)(65 + s) << " ";
					cout << (char)(65 + f) << (char)(65 + s) << " ";
				}
				
			}


		

		out << '\n';





	}//


	in.close();
	out.close();


	system("PAUSE");
	return 0;
}

