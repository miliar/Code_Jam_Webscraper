#include <iostream>
#include <fstream>
#include <sstream>
#include <math.h>
#include <algorithm>
#include <string>

using namespace std;

int main()
{
    //string const FichierEntree;
	//cin >> FichierEntree;
    string const FichierEntree("./A-large.in");
    //string const FichierEntree("./input.txt");
    string const FichierSortie("./output.txt");
	ifstream Input(FichierEntree.c_str());
	ofstream Output;
	Output.open(FichierSortie.c_str());//, ios::app);

	if(Input)  //On teste si tout est OK
	{
		int a, b, c;

		int nbT;
		Input >> nbT;

		for (int i=1; i<=nbT; i++)
		{
			string N;
            Input >> N;
            //cout<<"N = "<<N<<endl;
            int size = N.size();
            
            string Y = N.substr(0,1);
            //cout<<"Y = "<<Y<<endl;
            for (int j=1; j<size; j++)
            {
                int sizeY = Y.size();
                string temp0 = Y.substr(0,1)+N.substr(j,1);
                //cout<<"temp0 = "<<temp0<<endl;
                sort(temp0.begin(), temp0.end());
                if (temp0[1] == N[j])
                {
                    Y = N.substr(j,1)+Y;
                    //cout<<"Y = "<<Y<<endl;
                }
                else
                {
                    Y+= N.substr(j,1);
                    //cout<<"Y = "<<Y<<endl;
                }
            }
            
            
                Output << "Case #" << i<<": "<<Y<<endl;
            }
		Output.close();
	}
	else
	{
		cout << "ERREUR: Impossible d'ouvrir le fichier." << endl;
	}
    return 0;
}