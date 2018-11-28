#include<fstream>
#include<string>
#include<iomanip>
using namespace std;
ifstream f("input.in");
ofstream g("output.out"); 
int main(){
int n,z;
double t,F,c,x,r;
	f>>n;
for(z=1; z<=n; z++)
{
t=0; r=2.0;	
	f>>c;
	f>>F;
	f>>x;
int	cod=0;
	while(cod!=1){
	if((x/r)>(x/(r+F)+c/r))
	{t=t+c/r;
	r=r+F;}
	else{ t=t+x/r; cod=1;}}
g<<"Case #"<<z<<": ";
g << std::fixed << std::setprecision(7) << t;
g<<"\n";
}
f.close();
g.close();
return 0;
}
