#include<iostream>
#include<fstream>
#include<sstream>
#include<stdlib.h>
#include<math.h>
#include<iomanip>
#include<algorithm> 
#include<string>
#include<vector>
using namespace std;



int main()
{
int inc=1;
	ifstream file("i1.in");
	ofstream file2("o1.txt",ios::trunc);
	int t,i,j,k;
	file>>t;
	
	
	
	for(int x=1;x<=t;x++)
	{
		
		int a1,c1[5][5], a2,c2[5][5];
		
		file>>a1; 
		for(i=1;i<=4;i++){
			for(j=1;j<=4;j++){
				file>>c1[i][j];
				
			}
		}
		
		file>>a2;
		for(i=1;i<=4;i++){
			for(j=1;j<=4;j++){
				file>>c2[i][j];
			}
		}
	    
	    int count=0,ans;
	    
	    for(i=1;i<=4;i++){
			for(j=1;j<=4;j++){
	    		if(c1[a1][i]==c2[a2][j]){
	    			count++;
	    			ans=c1[a1][i];
	    			
	    		}
	    	}
	    }
		
		file2<<"Case #"<<inc++<<": ";
		
	    if(count==1)
		file2<<ans;
		else if(count>1)
		file2<<"Bad magician!";
		else if(count==0)
		file2<<"Volunteer cheated!";
		
		file2<<endl;
	}
}
