#include<iostream>
#include<cmath>
#include<cstdio>
#include<fstream>
using namespace std;
int main(){
	 ifstream myfile;
	 myfile.open("data.txt");
	FILE *fp = freopen ("myfile.txt","w",stdout);
	int tc;
	myfile>>tc;
	for (int cc=0;cc<tc;cc++){
	
		double c, f, x;
		double mint=10000000.0;
		myfile>>c>>f>>x;
		double time[((int)x)+5];
		time[0]=0;
		time[1]=c/2;
	//	cout<<time[1];
		
		for(int i=2;i<x;i++){
			time[i]=time[i-1]+(c/(2+f*(i-1)));	
		}
		mint=min((x/2),mint);
		for(int j=1;j<x;j++){
			
			double y=time[j]+(x/(2+f*(j)));
			//cout<<j<<" "<<time[j]<<" "<<" "<<(2+(f*j))<<" "<<x<<endl;
			mint=min(mint,y);
		}
		
		printf("Case #%d: %.7f\n", cc+1, mint);
	}
	  fclose (stdout);
}
