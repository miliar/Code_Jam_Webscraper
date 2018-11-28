#if 1
#include<iostream>
using namespace std;

int main(void){
	freopen("B-large.in", "r", stdin);
	//freopen("smallOutput.txt", "w", stdout);
	freopen("largeOutput.txt", "w", stdout);
	int T; cin>>T;
	for(int tc=1;tc<=T;tc++){
		cout<<"case #"<<tc<<": ";
		//double C = 30.5 , F = 3.14159,X= 1999.19990;
		double C = 0.0 , F = 0.0,X= 0.0;
		cin>>C>>F>>X;
		double currTime=0 , div = 2.0;
		
		if(X < C) currTime = X /2 ;
		else
		{	int N =1;
			double lastTime = X / div; double startTime =0.0 , totalTime =0 , prevSecs = 0.0;
			totalTime = startTime + lastTime ;  
			prevSecs = totalTime; 
			while (true){
				currTime = totalTime ;
				startTime = startTime + (lastTime * C / X) ;
				lastTime = X / (div + F * N ) ;
				totalTime = startTime + lastTime ;
				
				if(totalTime > currTime) break;
				N++;
			}
		}
		printf("%0.7f",currTime);
		
		cout<<'\n';
	}
	fclose(stdin); fclose(stdout);
	
}
#endif