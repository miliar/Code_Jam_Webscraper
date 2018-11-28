//This Code was written by Alexandre Boulch

//Stantard Template Library
#include <vector>
#include <iostream>
#include <fstream>
#include <sstream>
#include <queue>
using namespace std;

//This code uses Eigen library
//http://eigen.tuxfamily.org/
#include <Eigen/Dense>
using namespace Eigen;

//this code uses Boost for big integer
#include <boost/multiprecision/cpp_int.hpp>
using namespace boost::multiprecision;
typedef boost::multiprecision::uint1024_t bigint;

pair<bool,Eigen::MatrixXi> add_point(Eigen::MatrixXi mat, int x, int y, int total_m, int R, int C, int M, int level){
	Eigen::MatrixXi m = mat;
	int total_mines = total_m;

	if(m(x,y)==-1){
		total_mines--;
	}
	m(x,y) = 0;
	if(total_mines == M){return pair<bool,Eigen::MatrixXi>(true,m);}
	if(total_mines < M){return pair<bool,Eigen::MatrixXi>(false,Eigen::MatrixXi());}

	//if a case is 0 -> all adjacent cases cases must be 1
	for(int i=x-1; i<x+2; i++){
		for(int j=y-1;j<y+2; j++){
			if(i<0 || j<0 || j>=C || i>=R || (i==x && j==y)){continue;}
			if(m(i,j)!=-1){continue;}
			m(i,j) = level;
			total_mines--;
		}
	}
	if(total_mines == M){return pair<bool,Eigen::MatrixXi>(true,m);}
	if(total_mines < M){return pair<bool,Eigen::MatrixXi>(false,Eigen::MatrixXi());}

	for(int i=x-1; i<x+2; i++){
		for(int j=y-1;j<y+2; j++){
			if(i<0 || j<0 || j>=C || i>=R ||(i==x && j==y)){continue;}
			if(i!=x && j!=y){continue;}
			//if(m(i,j)!=level){continue;}
			if(m(i,j)<=0){continue;}
			m(i,j) = level;
			pair<bool,Eigen::MatrixXi> res =add_point(m,i,j,total_mines,R,C,M,level+1);
			if(res.first){
				return res;
			}
		}
	}

	return pair<bool,Eigen::MatrixXi>(false,Eigen::MatrixXi());
}

int main(){
	
	//Files
	string inputFile="C-small-attempt4.in";
	//string inputFile="input.txt";
	//string inputFile="input.txt";
	string outputFile="output.txt";

	//open input file
	ifstream ifs(inputFile.c_str());
	
	//get number of cases
	string line;
	getline(ifs,line);
	stringstream sstr(line);
	int n_cases;
	sstr >> n_cases;

	//open output file
	ofstream ofs(outputFile.c_str());

	//iterate on the cases
	// !!! case idx starts at 1
	for(int c=1; c<=n_cases; c++){

		getline(ifs, line);
		sstr = stringstream("");
		sstr << line;
		int R,C,M;
		sstr >> R >> C >> M;
		Eigen::MatrixXi mat = Eigen::MatrixXi::Constant(R,C,-1);
	
		int total_mines = R*C;
		pair<bool,Eigen::MatrixXi> res = add_point(mat,0,0,total_mines,R,C,M,1);
		cout << R << " " << C << " " << M << endl;
		cout << res.first << endl;
		cout << res.second << endl;

		mat = res.second;
		
		ofs << "Case #" << c << ": " << endl;
		if(res.first){
			for(int i=0; i<R; i++){
				for(int j=0; j<C; j++){

					if(i==0 && j==0){
						ofs << "c";
						continue;
					}
					if(mat(i,j)>=0){
						ofs<<".";
						continue;
					}
					if(mat(i,j)<0){
						ofs << "*";
					}
				}
				ofs << endl;
			}
		}else{
			ofs << "Impossible" << endl;
		}

#if 0
		int total_mines = R*C;
		queue<pair<int,int> > q;
		q.push(pair<int,int>(0,0));
		while(q.size() != 0){
			//get the front
			int xr = q.front().first;
			int yr = q.front().second;
			q.pop();
			//mark front
			if(mat(xr,yr) == 2){
			total_mines--;
			mat(xr,yr) = 0;
			if(total_mines <= M){break;}

			//mark neighbors
			if(xr+1 < R && mat(xr+1, yr)==2){
				mat(xr+1, yr)=3;
				total_mines--;
			}
			if(yr+1 < C && mat(xr, yr+1)==2){
				mat(xr, yr+1)=3;
				total_mines--;
			}
			if(yr+1 < C && xr+1<R &&  mat(xr+1, yr+1)==2){
				mat(xr+1, yr+1)=3;
				total_mines--;
			}
			if(total_mines <= M){break;}

			//add neighbors to queue
			if(xr+1 < R && mat(xr+1, yr)==3){
				mat(xr+1, yr)=1;
				q.push(pair<int,int>(xr+1,yr));
			}
			if(yr+1 < C && mat(xr, yr+1)==3){
				mat(xr, yr+1)=1;
				q.push(pair<int,int>(xr,yr+1));
			}
			if(yr+1 < C && xr+1<R &&  mat(xr+1, yr+1)==3){
				mat(xr+1, yr+1)=1;
				q.push(pair<int,int>(xr+1,yr+1));
			}
		}

		//cout << mat << endl;


		
		ofs << "Case #" << c << ": " << endl;
		if(total_mines == M){
			for(int i=0; i<R; i++){
				for(int j=0; j<C; j++){

					if(i==0 && j==0){
						ofs << "c";
						continue;
					}

					switch(mat(i,j)){
					case 1:
						ofs << ".";
						break;
					case 0:
						ofs << ".";
						break;
					case 3:
						ofs << ".";
						break;
					case 2:
						ofs << "*";
						break;
					}
				}
				ofs << endl;
			}
		}else{
			ofs << "Impossible" << endl;
		}
#endif
	}
	ofs.close(); //close output file
	return 0;
}