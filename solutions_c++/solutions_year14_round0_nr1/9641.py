#include<iostream>
#include<string>
using namespace std;

int data[4][4];
int Mdata[4];

int main(){ 
int n;
cin>>n;
int now=1;

while(now!=n+1){
int m;
cin>>m; //first answer
for(int i=0;i<4;i++){
for(int j=0;j<4;j++){
cin>>data[i][j];
}
}
for(int i=0;i<4;i++)Mdata[i]=data[m-1][i];
cin>>m;
for(int i=0;i<4;i++){
for(int j=0;j<4;j++){
cin>>data[i][j];
}
}
int count=0;
int ans=0;
for(int i=0;i<4;i++){
for(int j=0;j<4;j++){
if(Mdata[i]==data[m-1][j]){
count++;
ans=Mdata[i];
}
}
}
cout<<"Case #"<<now<<": ";
switch(count){
case 0:cout<<"Volunteer cheated!"<<endl;break;
case 1:cout<<ans<<endl;break;
default :cout<<"Bad magician!"<<endl;break;
}



now++;
}


	return 0;
}
