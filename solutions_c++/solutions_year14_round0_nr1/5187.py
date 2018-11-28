#include<iostream>
#include<cstdio>
#include<fstream>
using namespace std;
int main(){
	ofstream ofs;
	ofs.open ("output.txt");
    int t,n1,n2;
    int a[4][4],b[4][4],c[17],d[17];
    
     scanf("%d",&t);
    for(int i=1;i<=t;i++){
	for(int j=0;j<17;j++){
	c[j]=0;
	d[j]=0;
	}
    scanf("%d",&n1);
    for(int j=0;j<4;j++)
            for(int k=0;k<4;k++)
                    scanf("%d",&a[j][k]);        
     scanf("%d",&n2);
     for(int j=0;j<4;j++)
            for(int k=0;k<4;k++)
                    scanf("%d",&b[j][k]);         
	
       for(int j=n1-1;j<n1;j++) {
               for(int k=0;k<4;k++){
                      c[a[j][k]]=1; 
              }
       }

        for(int j=n2-1;j<n2;j++) {
               for(int k=0;k<4;k++){
                      d[b[j][k]]=1;               

               }             
        }
        int count=0;

        for(int j=0;j<17;j++)
        {
        if(c[j]&d[j])
        count++;
       }
       //cout<<count<<endl;
       if(count==0)
        ofs<<"Case #"<<i<<": "<<"Volunteer cheated!"<<endl;
        if(count==1)
        {
           for(int j=0;j<17;j++)
           {
                   if(c[j]&d[j])
                    ofs<<"Case #"<<i<<": "<<j<<endl;;
           }
        }
      if(count>1)  
	ofs<<"Case #"<<i<<": "<<"Bad magician!"<<endl;
    }
return 0;    
}
