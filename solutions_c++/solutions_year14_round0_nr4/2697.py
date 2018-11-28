
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	fstream fin("D-large.in");
	fstream fout("out.txt");

	int n, numBlock, pointsLie, pointsNaomi;
	vector<double> ken, ken2, naomi, naomi2;
	double temp;


	fin >> n;

	for(int i = 0; i < n; i++){
		ken.clear();
		naomi.clear();
		pointsNaomi = 0;
		pointsLie = 0;
		fin >> numBlock;
		for(int j = 0; j < numBlock; j++){
			fin >> temp;
			naomi.push_back(temp);
			naomi2.push_back(temp);
		}
		for(int j = 0; j < numBlock; j++){
			fin >> temp;
			ken.push_back(temp);
			ken2.push_back(temp);
		}

		sort(ken.begin(), ken.end());
		sort(naomi.begin(), naomi.end());

		sort(ken2.begin(), ken2.end());
		sort(naomi2.begin(), naomi2.end());

		for(int j = 0; j < numBlock; j++){
			//fout << "j = " << j << " KEN:" << ken[j] << " NAOMI:" << naomi[j] << endl;
		}

		/*for(int j = 0; j < numBlock; j++){
			if(ken[numBlock - 1 - j] < naomi[j])
				pointsLie++;
		}*/
		/*int k = 0;
		for(int j = 0; j < numBlock; j++){

		}*/

		for(int j = 0; j < numBlock; j++){
			if(naomi[naomi.size()-1] > ken[ken.size()-1]){
				ken.erase(find(ken.begin(), ken.end(), ken[0]));
				naomi.erase(find(naomi.begin(), naomi.end(), naomi[naomi.size()-1]));
				pointsNaomi++;
			} else {
				int y;
				for(y = 0; y < ken.size(); y++){
					if(ken[y] > naomi[naomi.size()-1]){
						naomi.erase(find(naomi.begin(), naomi.end(), naomi[naomi.size()-1]));
						ken.erase(find(ken.begin(), ken.end(), ken[y]));
						break;
					}
				}
			}
		}

		for(int j = 0; j < numBlock; j++){
          if((naomi2[naomi2.size()-1] < ken2[ken2.size()-1])||(naomi2[0] < ken2[0])){
        	  ken2.erase(find(ken2.begin(), ken2.end(), ken2[ken2.size()-1]));
        	  naomi2.erase(find(naomi2.begin(), naomi2.end(), naomi2[0]));
          } else {
             /* if(naomi[0] < ken[0]){
            	  //ken.erase(find(ken.begin(), ken.end(), ken[ken.size()-1]));
            	  //naomi.erase(find(naomi.begin(), naomi.end(), naomi[0]));
              } else {*/
            	  ken2.erase(find(ken2.begin(), ken2.end(), ken2[0]));
            	  naomi2.erase(find(naomi2.begin(), naomi2.end(), naomi2[0]));
            	  pointsLie++;

              //}
          }
		}

		/*int y;
		            	  for(y = 0; y <= ken.size(); y++){
		            		  if(ken[ken.size() - 1] > naomi[y]){
		            			  naomi.erase(find(naomi.begin(), naomi.end(), naomi[y+1]));
		            			  ken.erase(find(ken.begin(), ken.end(), ken[y]));
		            			  pointsLie++;
		            			  break;
		            		  }
		            	  }*/

		fout << "Case #" << i+1 << ": " << pointsLie << " " << pointsNaomi << endl;

	}



	fin.close();
	fout.close();
	return 0;
}
