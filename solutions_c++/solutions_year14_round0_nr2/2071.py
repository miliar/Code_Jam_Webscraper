#include<fstream >
#include <iomanip>
using namespace std;
 int main()
 {
 	ifstream fin("B-large.in");
 	ofstream fout("B-small-attempt0.out");
 	fout<<setiosflags(ios::fixed)<<setprecision(7);
 	 int t;
 	 double c,f,x,cost,rate;
 	 fin>>t;
 	 int tt=t;
 	 while (t)
 	 {
 	 	rate=2;
 	 	fin>>c>>f>>x;
 	 	while (x/rate>(x/(rate+f)+c/rate))
 	 	{
 	 		cost+=c/rate;
 	 		rate+=f;
 	 		
 	 	}
 	 	
 	 	cost+=x/rate;
 	 	fout<<"Case #"<<tt-t+1<<": "<<cost<<endl;
 	 	cost=0;
 	 	t--;
 	 }
 	 fin.close();
 	 fout.close();
 	 return 0;
 } 
