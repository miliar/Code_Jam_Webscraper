#include<iostream>
using namespace std;
#include<fstream>
int main(){
	
	ifstream ifile("C:/New folder/ip1.txt");
    ofstream ofile("C:/New folder/out1.txt");
	
	int t,i,a[5][5],y,b[5][5],ans1,ans2,j;
	ifile>>t;
	y=t;
	while(t--){
		
		int count=0,val=0;
	    ifile >>ans1;
	 	
		for(i=0;i<4;++i)
		for(j=0;j<4;j++)
		ifile>>a[i][j];
		
	    ifile >>ans2;
		
		for(i=0;i<4;++i)
		for(j=0;j<4;j++)
		ifile>>b[i][j];
		
		
		
		for(i=0;i<4;++i){
			
			for(j=0;j<4;++j){
				
				if(a[ans1-1][i]==b[ans2-1][j]){
					
					if(val!=a[ans1-1][i])
					count++;
					
					val=a[ans1-1][i];
					cout<<a[ans1-1][i]<<" " << y-t <<"\n";
				}
				
			}
			
		}
		
		if(count==0)
        ofile<<"Case #" << y-t <<": "<<"Volunteer cheated!\n";
        
        else if(count>1)
        ofile<<"Case #" << y-t <<": "<<"Bad magician!\n";
        
        else
        ofile<<"Case #" << y-t <<": "<<val<<"\n";
//		ofile<<"Case #1: 7"
		
		
	}
	
	
	return 0;
}
