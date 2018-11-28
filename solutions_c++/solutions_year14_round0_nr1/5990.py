#include <iostream>
using namespace std;
int main (){

int t;
cin>>t;

for(int i=1; i<=t; i++){
int flag =0, r1, r2, id;
int f[4][4];
int s[4][4];
cin>>r1;
r1--;
for(int j=0; j<4; j++){
for(int k=0; k<4; k++){
cin>>f[j][k];

}
}



cin>>r2;
r2--;
for(int j=0; j<4; j++){
for(int k=0; k<4; k++){
cin>>s[j][k];

}
}


for(int j=0; j<4; j++){
for(int k=0; k<4; k++){
if(f[r1][j]==s[r2][k]){
flag++;
id=f[r1][j];
}

}
}

if(flag==0){
cout<<"Case #"<<i<<": Volunteer cheated!"<<endl;
}
else if (flag==1){

cout<<"Case #"<<i<<": "<<id<<endl;

}
else {

cout<<"Case #"<<i<<": Bad magician!"<<endl;
}



}


}
