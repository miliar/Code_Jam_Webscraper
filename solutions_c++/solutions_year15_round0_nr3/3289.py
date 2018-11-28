#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <set>
#include <memory>
#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <memory>
#include <iostream>
#include <sstream>

// ? * x = y
std::pair<int,int> inverse(
	const std::vector<std::vector<int>> &map,
	const std::vector<std::vector<int>> &map_sign,
	int x,int y,
	int x_sign,int y_sign)
{
	for(int i = 0; i < 4; ++i){
		if(map[i][x] == y){
			int sign = map_sign[i][x]*x_sign;
			int m_s = -1;
			if(sign == y_sign)
				m_s = 1;
			return std::make_pair(i,m_s);
		}
	}

	throw std::logic_error("42");
	return std::make_pair(42,42);
}

std::pair<int,int> back_value(
	const std::vector<std::vector<int>> &map,
	const std::vector<std::vector<int>> &map_sign,
	unsigned long long idx,
	const std::vector<int>& back_mult,const std::vector<int>& back_mult_sign,
	const std::vector<int>& repetitions,const std::vector<int>& repetitions_sign
	){

	unsigned long long L = back_mult.size();
	unsigned long long X = repetitions.size();

	unsigned long long my_rep = idx / L;
	unsigned long long my_position = idx % L;


	if(my_rep == X-1){
		return std::make_pair(back_mult[my_position],back_mult_sign[my_position]);
	}

	int val = map[back_mult[my_position]][repetitions[my_rep + 1]];
	int sign = map_sign[back_mult[my_position]][repetitions[my_rep + 1]] * back_mult_sign[my_position] * repetitions_sign[my_rep + 1];
	return std::make_pair(val,sign);
	
}

std::pair<int,int> sub_value(
	const std::vector<std::vector<int>> &map,
	const std::vector<std::vector<int>> &map_sign,
	unsigned long long s,unsigned long long e,
	const std::vector<int>& back_mult,const std::vector<int>& back_mult_sign,
	const std::vector<int>& repetitions,const std::vector<int>& repetitions_sign
	){

	unsigned long long L = back_mult.size();
	unsigned long long X = repetitions.size();

	if(e == L*X){
		return back_value(map,map_sign,s,back_mult,back_mult_sign,repetitions,repetitions_sign);
	}

	auto v_s = back_value(map,map_sign,s,back_mult,back_mult_sign,repetitions,repetitions_sign);
	auto v_e = back_value(map,map_sign,e,back_mult,back_mult_sign,repetitions,repetitions_sign);

	auto v = inverse(map,map_sign,std::get<0>(v_e),std::get<0>(v_s),std::get<1>(v_e),std::get<1>(v_s));

	return v;
}


void solve(int num, std::ifstream& input, std::ofstream& output){
	int L,X;


	std::vector<std::vector<int>> map(4,std::vector<int>(4));
	map[0][0] = 0; map[0][1] = 1; map[0][2] = 2; map[0][3] = 3;
	map[1][0] = 1; map[1][1] = 0; map[1][2] = 3; map[1][3] = 2;
	map[2][0] = 2; map[2][1] = 3; map[2][2] = 0; map[2][3] = 1;
	map[3][0] = 3; map[3][1] = 2; map[3][2] = 1; map[3][3] = 0;

	std::vector<std::vector<int>> map_sign(4,std::vector<int>(4));
	map_sign[0][0] =  1; map_sign[0][1] =  1; map_sign[0][2] =  1; map_sign[0][3] =  1;
	map_sign[1][0] =  1; map_sign[1][1] = -1; map_sign[1][2] =  1; map_sign[1][3] = -1;
	map_sign[2][0] =  1; map_sign[2][1] = -1; map_sign[2][2] = -1; map_sign[2][3] =  1;
	map_sign[3][0] =  1; map_sign[3][1] =  1; map_sign[3][2] = -1; map_sign[3][3] = -1;

	input >> L;
	input >> X;

	std::string line;
	std::getline(input,line);
	std::getline(input,line);

	std::vector<int> string_num;
	for(int i = 0; i < L; ++i){
		int v = 0;
		switch(line[i])
		{
		case 'i': v = 1; break;
		case 'j': v = 2; break;
		case 'k': v = 3; break;
		default: break;
		}
		string_num.push_back(v);
	}

	std::vector<int> back_mult(L);
	std::vector<int> back_mult_sign(L);
	back_mult[L - 1] = string_num[L - 1];
	back_mult_sign[L - 1] = 1;
	for(int i = L-2; i >= 0; --i){
		back_mult[i] = map[string_num[i]][back_mult[i+1]];
		back_mult_sign[i] = map_sign[string_num[i]][back_mult[i + 1]] * back_mult_sign[i + 1];
	}

	std::vector<int> repetitions(X);
	std::vector<int> repetitions_sign(X);

	repetitions[X - 1] = back_mult[0];
	repetitions_sign[X - 1] = back_mult_sign[0];
	for(int i = X-2; i >= 0; --i){
		repetitions[i] = map[back_mult[0]][repetitions[i+1]];
		repetitions_sign[i] = map_sign[back_mult[0]][repetitions[i + 1]] * back_mult_sign[0] * repetitions_sign[i+1];
	}
	/*

	for(int i = 0; i < L*X; ++i){
		auto v = back_value(map,map_sign,i,back_mult,back_mult_sign,repetitions,repetitions_sign);
		std::cout << (std::get<1>(v) == 1 ? "+" : "-") << std::get<0>(v) << " ";
	}

	std::cout << std::endl;
	{
		auto v = sub_value(map,map_sign,0,3,back_mult,back_mult_sign,repetitions,repetitions_sign);
		std::cout << (std::get<1>(v) == 1 ? "+" : "-") << std::get<0>(v) << " ";
	}
	{
		auto v = sub_value(map,map_sign,3,6,back_mult,back_mult_sign,repetitions,repetitions_sign);
		std::cout << (std::get<1>(v) == 1 ? "+" : "-") << std::get<0>(v) << " ";
	}
	{
		auto v = sub_value(map,map_sign,6,12,back_mult,back_mult_sign,repetitions,repetitions_sign);
		std::cout << (std::get<1>(v) == 1 ? "+" : "-") << std::get<0>(v) << " ";
	}
	{
		auto v = sub_value(map,map_sign,0,1,back_mult,back_mult_sign,repetitions,repetitions_sign);
		std::cout << (std::get<1>(v) == 1 ? "+" : "-") << std::get<0>(v) << " ";
	}
	int idx_0,idx_1;
	*/
	//searching for a valid 
	bool found = false;
	unsigned long long XL = unsigned long long (X)*unsigned long long(L);
	for(unsigned long long i = 0; i < XL-2 && !found; ++i){
		auto i_v = sub_value(map,map_sign,0,i+1,back_mult,back_mult_sign,repetitions,repetitions_sign);
		if(std::get<0>(i_v) == 1 && std::get<1>(i_v) == 1){
			for(unsigned long long j = i+1; j < XL-1 && !found; ++j){
				auto j_v = sub_value(map,map_sign,i+1,j+1,back_mult,back_mult_sign,repetitions,repetitions_sign);
				if(std::get<0>(j_v) == 2 && std::get<1>(j_v) == 1){
				//	for(unsigned long long k = j+1; k < XL; ++k){
						auto k_v = sub_value(map,map_sign,j+1,XL,back_mult,back_mult_sign,repetitions,repetitions_sign);
						if(std::get<0>(k_v) == 3 && std::get<1>(k_v) == 1){
							found = true;
							//std::cout << i << " " << j << " "  << std::endl;
						}
					}
				//}
			}
		}
	}

	output << "Case #" << num << ": " << (found?"YES":"NO") << std::endl;
	std::cout << "Case #" << num << ": " << (found ? "YES" : "NO") << std::endl;
}


int main(int argc, char *argv[]){
	if(argc!=3){
		std::cout << "wrong number of arguments";
		return 1;
	}

	std::ifstream file_input (argv[1]);
	if (!file_input.is_open()){
		std::cout << "unable to open the input file";
		return 1;
	}

	std::ofstream file_output (argv[2]);
	if (!file_output.is_open()){
		std::cout << "unable to open the input file";
		return 1;
	}

	int n_tests = 0;
	file_input >> n_tests;

	std::cout << "#tests: " << n_tests << std::endl;

	for(int i = 0; i < n_tests; ++i){
		solve(i+1,file_input,file_output);
	}

}