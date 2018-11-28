#include <iostream>
#include <fstream>
#include <sstream>
#include <math.h>
#include <algorithm>
#include <stdlib.h>
#include <string>
#include <cstddef>

using namespace std;

int main()
{
    //string const FichierEntree;
	//cin >> FichierEntree;
    string const FichierEntree("./B-small-practice.in");
    //string const FichierEntree("./test.txt");
    string const FichierSortie("./output.txt");
	ifstream Input(FichierEntree.c_str());
	ofstream Output;
	Output.open(FichierSortie.c_str());//, ios::app);

	if(Input)  //On teste si tout est OK
	{
		int N, J;

		int nbT;
        Input >> nbT;
        
        for (int i=1; i<=nbT; i++)
        {
            string S = "";
        
            Input >> S;
            //cout<<"S = "<<S<<endl;
            int size = 0;
            int pos = S.find_last_of("-");
            size = 0;
            if (pos >= 0)
            {
                string before = S.substr(0,pos+1);
                //cout<<"before = "<<before<<endl;
        
                size = before.size();

                string temp;
                string  fin;
                
                pos = 0;
        
                while (pos < size && pos>=0)
                {
                    temp = before[pos];
                    //cout<<"temp = "<<temp<<endl;
                    fin += temp;
                    //cout<<"fin = "<<fin<<endl;
                    pos = before.find_first_not_of(temp, pos);
                    //cout<<"pos = "<<pos<<endl;
                }
                //cout<<"solution = "<<fin<<endl;
        
                size = fin.size();
                //cout<<"size = "<<size<<endl;
            }
        
            //cout<<endl;
            Output << "Case #" << i<<": "<<size<<endl;
            
        }
		Output.close();
	}
	else
	{
		cout << "ERREUR: Impossible d'ouvrir le fichier." << endl;
	}
    return 0;
}