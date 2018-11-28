#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>

using namespace std;
typedef vector<int> Tab;

void affich_tab(vector<int> T){
    for(unsigned int i(0); i < T.size(); ++i)
        cout<<T[i]<<" ";
    cout<<endl;
}

string int_to_string(int i){
	ostringstream flux_convert;
	flux_convert << i;
	return flux_convert.str();
}


void magician(string input,string output){
	 ifstream f(input.c_str(),ios::in);
	 if(f){
		int nbfois(0);
         f>>nbfois;
        // cout<<nbfois<<endl;
         ofstream fout(output.c_str(),ios::out);
         if(fout){
			 for(int c(0); c < nbfois ; ++c){
				Tab ligne;
				Tab compare_ligne;
				int compare_result(0);
				for(int k(0); k< 2; k++){  // pour les 2 melanges
					int num_lign(0);
				f>>num_lign;
				//cout<<num_lign<<endl;				
					for(int i (0); i < 4 ; i++){ // pour chak ligne du melange
						ligne.clear();
						affich_tab(ligne);
						for(int j(0); j < 4 ; j++){ // pour chak case
							int temp;
							f>>temp;
							ligne.push_back(temp);
							
						}
						
						if(k ==1 && i == (num_lign -1)){ // au second melange si on a la ligne choisi
							// on compare
							//affich_tab(ligne);
							//affich_tab(compare_ligne);
							for(int c1(0); c1 < 4 ; ++c1){
								for(int c2(0); c2 < 4 ; c2 ++){
									//cout<<compare_ligne[c1]<<" "<< ligne[c2]<<" rslt "<<compare_result <<endl;
									if(compare_result != 0 && compare_ligne[c1] == ligne[c2]){ // plus d'une carte trouvée
										compare_result = -1;
										break;
									}
									else if(compare_ligne[c1] == ligne[c2])
										compare_result = compare_ligne[c1];
								}
							}
						}
							
						else if(i == (num_lign -1))
								compare_ligne = ligne;
						else ;
						
					}
				}
				// ici on analyse le resultat de la comparaison
				string out;
				if( compare_result == 0)
					out = "Volunteer cheated!";
				else if( compare_result == -1)
					out ="Bad magician!";
				else
					out = int_to_string(compare_result);
				 fout<<"Case #"<<c+1<<": ";
				 fout<<out;
				 if(c != nbfois -1)
					fout<<endl;					
			}
			fout.close();
		}
		else
			 cerr<<"Ouverture imposible du fichier de sortie"<<endl;
        f.close();
	}
	else
		 cerr<<"Ouverture imposible du fichier d'entrée"<<endl;
	}

int main(){
   magician("input.txt","output.out");

	return 0;
}
