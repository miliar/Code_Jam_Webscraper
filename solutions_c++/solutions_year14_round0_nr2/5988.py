#include <iostream>
#include <iomanip>
using namespace std;
int main (){
cout.precision(7); 

int t;
cin>>t;

for(int i=1; i<=t; i++){
long double c, f , x, p=2.0;
long double tim=0;

cin>>c;
cin>>f;
cin>>x;


while((tim+(x/p))>=(tim+((c/(p))))+(x/(p+f))){
tim=tim+(c/p);
p=p+f;

}
tim=tim+(x/p);

cout<<"Case #"<<i<<": "<< setiosflags (ios::fixed) <<tim<<endl;

}

return 0;
}
