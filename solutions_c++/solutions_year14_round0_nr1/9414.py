#include<stdio.h>
#include<iostream>

using namespace std;
int main(){

int t,ans1,ans2;
cin>>t;
int casecount=1;
while(t--){

cin>>ans1;
int a[4][4]={0},b[4][4]={0};

for(int i=0;i<4;i++)
for(int j=0;j<4;j++)
cin>>a[i][j];

cin>>ans2;
for(int i=0;i<4;i++)
for(int j=0;j<4;j++)
cin>>b[i][j];

/*
for(int i=0;i<4;i++)
{cout<<endl;
    for(int j=0;j<4;j++)
cout<<a[i][j]<<" ";
}
cout<<endl;

for(int i=0;i<4;i++)
{cout<<endl;
    for(int j=0;j<4;j++)
cout<<b[i][j]<<" ";
}
*/
int val;
int c=0;

int sol[17]={0};

for(int i=0;i<4;i++)
for(int j=0;j<4;j++)
{
    if(a[ans1-1][i]==b[ans2-1][j]){
          sol[a[ans1-1][i]]++;
          c++;
         // cout<<"equality detected "<<i<<" "<<j<<" "<<a[ans1-1][i]<<endl;
          break;

    }
}
//cout<<endl<<"c val "<<c<<endl;
if(c==0){
    cout<<"Case #"<<casecount<<": "<<"Volunteer cheated!"<<endl;
 //   continue;
}
else {
c=0;
int i;
for(i=1;i<17;i++){
    if(sol[i]==1){
        c++;
        val = i;
        //break;
    }
}

if(c==1){
    cout<<"Case #"<<casecount<<": "<<val<<endl;
}

else {
    cout<<"Case #"<<casecount<<": "<<"Bad magician!"<<endl;
}
}
casecount++;




}

return 0;
}
