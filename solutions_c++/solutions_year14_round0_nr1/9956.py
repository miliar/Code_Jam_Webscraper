#include <iostream>

using namespace std;

int main()
{
   int a[4][4];
   int b[4][4];
   int i,j,k=1;
   int r[2],c,count=0;
   int a1,a2;
   int n;
  
   cin>>n;
   for(k=0;k<n;k++){
       count=0;
       cin>>a1;
       a1-=1;
    for(i=0;i<4;i++){
        for(j=0;j<4;j++){
            cin>>a[i][j];   
        }
    }
    
       cin>>a2;
       a2-=1;
    for(i=0;i<4;i++){
        for(j=0;j<4;j++){
            cin>>b[i][j];   
        }
    }
    for(i=0;i<4;i++)
    {
        for(j=0;j<4;j++){
        if(a[a1][i] == b[a2][j]){
        c=a[a1][i];count++;
        }
    }
    }
    if(count>1){
        cout<<"Case #"<<k+1<<": Bad magician!";
        
    }
    else if(count == 0){
        cout<<"Case #"<<k+1<<": Volunteer cheated!";
        
    }
    else if(count == 1)
    {
        cout<<"Case #"<<k+1<<": "<<c;
        
    }
    cout<<"\n";
    
    }
  
   return 0;
}