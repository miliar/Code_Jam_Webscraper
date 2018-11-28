#include<iostream>
#include<eigen3/Eigen/Dense>

enum{YES,NO};
std::string r_string[]={"YES","NO"};
std::vector<Eigen::MatrixXf> cases;

void parse_input(std::istream& input){
	int cases_n; 	input>>cases_n; 
	cases.resize(cases_n);
	for(auto& lawn:cases){
		int n,m; input>>n; input>>m;
		lawn.resize(n,m);
		for(int i=0;i<n;i++) for(int j=0;j<m;j++) input>>lawn(i,j);
	}
}

int solve_case(const Eigen::MatrixXf& lawn){
	//Eigen::MatrixXf lawn_ok(lawn.rows(),lawn.cols()); lawn_ok<MatrixXf::Zero(lawn.rows(),lawn.cols());
	Eigen::VectorXf colmax=lawn.colwise().maxCoeff();
	Eigen::VectorXf rowmax=lawn.rowwise().maxCoeff();
	for(int i=0;i<lawn.rows();i++) for(int j=0;j<lawn.cols();j++) if(lawn(i,j)<colmax(j) && lawn(i,j)<rowmax(i)) return NO;
	return YES;
}

int main(){
	parse_input(std::cin);
	for(int i=0;i<cases.size();i++){
		std::cout<<"Case #"<<i+1<<": "<<r_string[solve_case(cases[i])]<<std::endl;
	}

	return 0;
}
