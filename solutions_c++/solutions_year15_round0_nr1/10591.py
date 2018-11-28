
#include<iostream>
#include<utility>
#include<math.h>
#include<fstream>
using namespace std;
int main(){
    int arr,j,people,n=0,t,smax,s[8],i,fr=0,k;
    ifstream in("A-small-attempt9.in");
    ofstream ot;
    string line;
      ot.open ("g1.txt");
//in.open();
in>>t;



for(n=1;n<=t;n++){

in>>smax;

fr=0;
in>>arr;

for(k=smax;k>=0;k--){
		s[k]=arr%10;
		arr= arr/10;
}


for(k=0;k<=smax;k++){
people=0;
for(j=0;j<k;j++){

people += s[j];


}

if(s[k]!=0){
	if(k>(people+fr)){

while(k!=(people+fr)){

fr++;
}}

}}
	ot<<"Case #"<<n<<": "<< fr;

if(n!=t){
    ot<<endl;
}







}



  ot.close();

}
