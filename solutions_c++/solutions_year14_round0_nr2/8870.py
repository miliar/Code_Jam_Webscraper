#include<fstream>
#include<vector>
#include<iomanip>
using namespace std;
bool evaluate(double c, double f,double r, double t);
int main()
{


ifstream fin;
ofstream fout;
int numofcase;
vector<double> v;
fin.open("input.in");
fout.open("output.txt");
fin>>numofcase;

for(int casenum=0; casenum<numofcase;casenum++)
{
	double c,f,t,x,totalf,totalt;
	double r=2;
	fin>>c>>f>>x;
	t=x/r;
	totalf= 0;
	totalt=0;
	while(evaluate(c,f,r,t))
	{	//add a farm
		totalf++;
		totalt+=c/r;
		r=r+f;
		t=x/r;		
	}
	totalt+=x/r;
	
v.push_back(totalt);
}

for(int i=0;i<v.size();i++)
{
	fout<<"Case #"<<i+1<<": ";
	fout<<fixed<<setprecision(7)<<v[i]<<endl;
}
}

bool evaluate(double c, double f,double r, double t)
{
	if(c/r+c/f <t)
		return true;
	else 
		return false;
}