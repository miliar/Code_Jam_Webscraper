#include<fstream>
#include<iomanip>
using namespace std;
int main()
{
ifstream i ;
i.open("input.txt");
ofstream o;
o.open("output.txt");
 int p=1,a;
 i>>a;
 while(a>0)
 {
 double t=0;
 double c,x,f,g=2;
 i>>c>>f>>x;
while((x/g>(c/g)+x/(g+f)))
 {
 t=t+c/g;
g=g+f;
}
 t=t+x/g;
 o<<setprecision(7);
o<<fixed;
 o<<"Case #"<<p<<": "<<t<<"\n";
p++;
   a--;
 }

return 0;
}
