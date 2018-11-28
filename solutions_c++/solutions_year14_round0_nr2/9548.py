#include <iostream>
#include <string>
#include <fstream>
#include <iomanip>
#include <sstream>
using namespace std;
float farmtime(int n, float c, float f){
	if(n==1)
		return c/((n-1)*f+2);
	else
		return farmtime(n-1,c,f) + c/((n-1)*f+2);
}

void main(){
	float c, f, x, tmp1, tmp2;
	int T, i, j;
	bool cek = false;
	string line;
	ifstream myfile;
	ofstream writefile;
	myfile.open("input.in");
	if (myfile.is_open())
	  {
		  if(myfile.good()){
			  getline(myfile, line);
			  T = stoi(line);
		  }
	  }
	else{
		cout<<"Can't open\n";
	}
	writefile.open("result.out");
	for(i=1;i<=T;i++){
		j=1;
		tmp1 = tmp2 = 0;
		cek = false;
		getline(myfile,line);
		stringstream iss;
		iss << line;
		iss >> c >> f >> x;
		tmp1=farmtime(j,c,f)+x/(j*f+2);
		if(x/2 < tmp1){
			cek = true;
			tmp1 = x/2;
		}
		while(cek == false)
		{
			tmp2=farmtime(j+1,c,f)+x/((j+1)*f+2);
			if(tmp1 <= tmp2)
				cek = true;
			else{
				tmp1=tmp2;
				j++;
			}
		}
		writefile << "Case #"<<i<<": "<<std::fixed << std::setprecision(7)<<tmp1<<endl;
	}
	myfile.close();
	writefile.close();
	system("pause");
}