#include <iostream>
using namespace std;
int m[4][4],r,i,j,c[17],f;

int solve(int a){
 cin>>r; f=0;
 for(i=0;i<17;i++)c[i]=0;
 for(i=0;i<4;i++)
  for(j=0;j<4;j++){
    cin>>m[i][j];
    if(i==r-1)c[m[i][j]]++;
   }
   cin>>r;
 for(i=0;i<4;i++)
  for(j=0;j<4;j++){
    cin>>m[i][j];
    if(i==r-1)c[m[i][j]]++;
   }
//for(i=1;i<17;i++)cout<<c[i]<<" ";
//cout<<endl;
 cout<<"Case #"<<a<<": ";
 for(i=0;i<17;i++)
  if(c[i]==2)f++;

  if(f>1)cout<<"Bad magician!"<<endl;
else if(f==0)cout<<"Volunteer cheated!"<<endl;
 else{
  for(i=0;i<17;i++)
 if(c[i]==2)cout<<i<<endl;
}

}
int main() { int t;
	cin>>t;
    for(int j=1;j<=t;j++)
solve(j);
	return 0;
}
