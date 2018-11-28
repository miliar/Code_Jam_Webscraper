#include <iostream>
using namespace std;

int main() {
	int a1[4][4],a2[4][4],t,i,j,n,m,k=0,f=0,count=0,c=0;
	cin>>t;
	while(t--){
	c++;
	cin>>n;
	for(i=0;i<4;i++){
        for(j=0;j<4;j++)
        {
           cin>>a1[i][j];
        }
      }
    cin>>m;
	for(i=0;i<4;i++){
        for(j=0;j<4;j++)
        {
           cin>>a2[i][j];
        }
      }
    for(i=0;i<4;i++)
    { 
        for(j=0;j<4;j++)
        {
          if(a1[n-1][i]==a2[m-1][j])    
               count++;
          if(a1[n-1][i]==a2[m-1][j]){
                f=1;
                k=a1[n-1][i];
                break;
              }     
           }
       }
        if(count==0)
                  cout<<"Case #"<<c<<":"<<" Volunteer cheated!\n";
        else if(count>1)
                  cout<<"Case #"<<c<<":"<<" Bad magician!\n";
        else if(f==1)
                  cout<<"Case #"<<c<<": "<<k<<"\n";
      count=0;            
	}
	return 0;
}