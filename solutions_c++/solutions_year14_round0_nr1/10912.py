#include<fstream>
#include<iostream>
using namespace std;
int main(){
  fstream f("A-small-attempt1.in",ios::in),g("magic.out",ios::out);
  int t,a1,a2,c,l[16],m,x;
  f>>t;
  for(int n=1;n<=t;n++){
  	m=0;
  	f>>a1;
  	for(int i=0;i<4;i++)
  		for(int j=0;j<4;j++){
  			f>>c;
  			l[c-1]=i+1;
  		}
  	f>>a2;
  	for(int i=0;i<4;i++)
  		for(int j=0;j<4;j++){
  			f>>c;
  			if(a2==i+1&&l[c-1]==a1){
  				m++;
  				x=c;
  			}
  		}
  	g<<"Case #"<<n<<": ";
	if(m==1)g<<x<<endl;
	else if(m<1)g<<"Volunteer cheated!"<<endl;
	else if(m>1)g<<"Bad magician!"<<endl;
  }
  return 0;
}

