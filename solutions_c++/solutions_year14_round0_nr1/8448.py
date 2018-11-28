#include<iostream>
#include<stdlib.h>
using namespace std;

void input (int r, int row[4]){
    int var;
for (int i=0; i<4*(r-1); i++)   {cin>> var;}
for (int j=0; j<4; j++){ cin>> var; row[j]=var;}
for (int k=0; k<4*(4-r); k++)   {cin>> var;}
};

int main()
{
int r1[4],r2[4];
int T=1,rw1,rw2,t,temp,num=0,var1,var2;
cin>>T;
for (t=1; t<=T; t++){
cin>>rw1;
input(rw1,r1);
cin>>rw2;
input(rw2,r2);


for(int i=0; i<4; i++){
        for(int j=0; j<4; j++){
            if(r1[i]==r2[j]) { temp=r1[i];
            num++;

            }
        }
    }

cout<<"Case #"<<t<<": ";
if(num==0){ cout<<"Volunteer cheated!\n";}
else{
if(num==1){ cout<<temp<<"\n";}
else { cout<<"Bad magician!\n";}
}
num=0;
}

return 0;
}
