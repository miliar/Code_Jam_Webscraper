#include <iostream>
#include <fstream>
#include <iomanip>
#include <algorithm>
#include <vector>


int main() {


	
	std::ifstream read;
	read.open("D-large.in");

	std::ofstream write;
	write.open("output.txt");

	int x;

	read >>  x;

	for (int i = 0; i < x; i++) {
		int n;
		read >> n;

		std::vector<double>naomi;
		std::vector<double>ken;

		for (int k = 0; k < n; k++){
			double t;
			read >> t;
			naomi.push_back(t);
		}

		for (int k = 0; k < n; k++){
			double t;
			read >> t;
			ken.push_back(t);
		}


		std::sort(naomi.begin(), naomi.end());
		std::sort(ken.begin(), ken.end());

		std::vector<double> naomi2;
		std::vector<double> ken2;

		for (int k = 0; k < naomi.size(); k++){
			naomi2.push_back(naomi[k]);
			ken2.push_back(ken[k]);


		}

		int naominormal = 0;


		while (naomi.size() > 0){

			if (naomi[naomi.size()-1] > ken[ken.size() - 1]) {
				naomi.pop_back();
				ken.erase(ken.begin());
				naominormal++;
			}

			else {
				for (int l = ken.size() - 1; l >= 0; l--) {
					if (ken[l] < naomi[naomi.size()-1]){
						naomi.pop_back();
						//std::vector<double>::iterator i = ken.begin();
						ken.erase(ken.begin()  + l + 1);
						break;
					}
					if (l == 0){
						naomi.pop_back();
						ken.erase(ken.begin());

					}
				}
			}
		}

		
		int naomidecieve = 0;
		
		
		while (naomi2.size() > 0) {
			if (ken2[ken2.size()-1] > naomi2[naomi2.size()-1]) {
				//std::cout << "Ken dele " << ken2[ken2.size() - 1] << std::endl;
				ken2.pop_back();
				
				//std::vector<double>::iterator i = naomi2.begin();
				//std::cout << "Naomi dele " << naomi2[0] << std::endl;
				naomi2.erase(naomi2.begin());
			}

			else {
				
				for (int l = 0; l < naomi2.size(); l++){
					if (naomi2[l] > ken2[0]){
						//std::cout << "Naomi dele " << naomi2[l] << std::endl;
						naomi2.erase(naomi2.begin() + l);
						break;
					}
				}


				//std::vector<double>::iterator i = ken2.begin();
				//std::cout << "Ken dele " << ken2[0] << std::endl;
				ken2.erase(ken2.begin());
				
				naomidecieve++;

			}




		}

		write << "Case #" << i + 1 << ": " << naomidecieve << " " << naominormal << "" << std::endl;



	}



	



	write.close();




	//system("PAUSE");






}