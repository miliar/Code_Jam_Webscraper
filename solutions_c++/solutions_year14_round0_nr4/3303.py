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

#define For(i,n) for (i=0; i<int(n); i++)

int main()
{
int inc=1;
	ifstream file("i1.in");
	ofstream file2("o1.txt",ios::trunc);
	int t,i,j,k;
	file>>t;
	
	
	
	for(int x=1;x<=t;x++)
	{
		int n1; double n[1002],k[1002],temp1;
		file>>n1;
		for(i=1;i<=n1;i++){
			file>>n[i];
		}
		for(i=1;i<=n1;i++){
			file>>k[i];
		}
		
		for(i=1;i<=n1;i++){
			for(j=i+1;j<=n1;j++){
				if(n[i]>n[j]){
					temp1=n[i]; n[i]=n[j]; n[j]=temp1;
				
				}
				if(k[i]>k[j]){
					temp1=k[i]; k[i]=k[j]; k[j]=temp1;
				}
			}
		}
		
		int c1=0;
		int y=1,z=1;
		while(y<=n1){
			if(n[y]<k[z]){
				y++;
			}
			else{
				c1++; y++; z++;
			}
		}
		
		int c2=0;
		y=1,z=1;
		while(z<=n1){
			if(n[y]<k[z]){
				y++; z++;
			}
			else{
				z++; c2++;
			}
		}
		
		
		file2<<"Case #"<<inc++<<": ";
		
	    
		file2<<c1<<" "<<c2;
		
		
		file2<<endl;
	}
}
