#include<iostream>
#include<iomanip>
#include<fstream>
#include<set>
int main(){
	std::ifstream input_file("c:\\project\\D-small-attempt0.in");
	std::ofstream output_file("c:\\project\\D-small-attempt0.out");
	std::istream &input = input_file;
	std::ostream &output = output_file;
	int number_of_test_cases, number_of_weights, count_war = 0, count_deceitful=0;
	double temp_weight;

	input >> number_of_test_cases;
	for (int t = 1; t <= number_of_test_cases; t++){
		std::set<double> weight_set_naomi;
		std::set<double> weight_set_ken;
		input >> number_of_weights;
		for (int i = 0; i < number_of_weights; i++){
			input >> temp_weight;
			weight_set_naomi.emplace(temp_weight);
		}
		for (int i = 0; i < number_of_weights; i++){
			input >> temp_weight;
			weight_set_ken.emplace(temp_weight);
		}
		std::set<double>temp_naomi = weight_set_naomi;
		std::set<double>temp_ken = weight_set_ken;
		//count_war = 0;
		

		/*for (std::set<double>::iterator it = temp_naomi.begin(); it != temp_naomi.end(); it++){
			std::set<double>::iterator ft = temp_ken.upper_bound(*it);
			if (ft != temp_ken.end()){
				count_war++;
			}
		}
		for (std::set<double>::iterator it = temp_ken.begin(); it != temp_ken.end(); it++){
			std::set<double>::iterator ft = temp_naomi.upper_bound(*it);
			if (ft != temp_naomi.end()){
				count_deceitful++;
			}
		}*/
		std::set<double>::reverse_iterator it;
		std::set<double>::iterator ft;
		count_war = 0;
		do{
			it = temp_naomi.rbegin();
			//it++;
			//--it;
			//double k = *it;
			ft = temp_ken.upper_bound(*it);
			if (ft != temp_ken.end()){
				//if ((*ft)>(*it)){
				count_war++;
			}
			else{
				ft = temp_ken.begin();
			}
			//else break;
			it++;
			//k = *it;
			//k = *it.base();
			temp_naomi.erase(it.base());
			temp_ken.erase(ft);
		} while (!temp_naomi.empty());
		count_deceitful = 0;

		temp_naomi = weight_set_naomi;
		temp_ken = weight_set_ken;
		do{
			it = temp_ken.rbegin();
			//it++;
			//--it;
			//double k = *it;
			ft = temp_naomi.upper_bound(*it);
			if (ft != temp_naomi.end()){
				//if ((*ft)>(*it)){
				count_deceitful++;
			}
			else{
				ft = temp_naomi.begin();
			}
			//else break;
			it++;
			//k = *it;
			//k = *it.base();
			temp_ken.erase(it.base());
			temp_naomi.erase(ft);
		} while (!temp_ken.empty());

		count_war = number_of_weights - count_war;
		output << "Case #" << t << ": " << count_deceitful<<" "<<count_war << std::endl;

	}
	input_file.close();
	output_file.close();
}