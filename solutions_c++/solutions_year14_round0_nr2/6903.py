#include<fstream>
#include<iostream>

using namespace std;

int T;
double C;
double F;
double X;

fstream fin("in.in");


int main(){

fin>>T;

for(int t=1;t<=T;t++)
{

fin>>C>>F>>X;
double current  =0;
double previous =0;
double total    =0;
cout.precision(13);

for(int i=0;;i++){

//cout<<"rate:"   <<2+i*F    <<"     ";
//cout<<"C/(2+iF)"<<C/(2+i*F)<<"     ";
//cout<<"X/(2+nF)"<<X/(2+i*F)<<"     ";
//cout<<"taotal  "<<total<<endl;
current=total+X/(2+i*F);

if(current>=previous && i!=0){

 cout<<"Case #"<<t<<": "<<previous<<endl;

  break;
}
 
total+=C/(2+i*F);

previous=current;
}



}


return 0;
}

