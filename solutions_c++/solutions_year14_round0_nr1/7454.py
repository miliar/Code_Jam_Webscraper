	#include<iostream>
	#include<fstream>

	using namespace std;

	int one[4][4];
	int tow[4][4];
	int main(){
		ifstream ins;
		ofstream outs;

		ins.open("A-small-attempt0.in");
		outs.open("A-small-attempt0.out");
		int a;
		ins>>a;    
		int temp=1;
		while(a--){
			int v;
			int t,f;
			ins>>t;       
			for(int i=0;i<4;i++){
				for(int j=0;j<4;j++)
				{ins>>one[i][j]; }   }
			ins>>f;
			for(int k=0;k<4;k++){
				for(int h=0;h<4;h++)
				{ins>>tow[k][h];   }  }
		
			int ans=0;
			for(int m=0;m<4;m++)
				for(int n=0;n<4;n++)
				{
					if(one[t-1][m]==tow[f-1][n]){
						v=one[t-1][m];   
						ans++;
					}
				}

				if(ans==0){
					outs<<"Case #"<<temp<<": Volunteer cheated!"<<endl;   
					temp++;
				}
				else if(ans==1){
					outs<<"Case #"<<temp<<": "<<v<<endl;  
					temp++;
				}
				else {
					outs<<"Case #"<<temp<<": Bad magician!"<<endl;  
					temp++;
				}

		}

		ins.close();
		outs.close();

		return 0;
	}