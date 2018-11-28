#include <iostream>
#include <fstream>
#include <stdlib.h>
using namespace std;

int manageCase(int *t,int n){
	int T=0;
	int k=0;
for(int i=0;i<n;i++){
	T=T+t[i];
	if((i==0)&&(T==0)){
		T++;
		k++;
	}
	else if(T<i+1){
		while(T<=i){
			T=T+1;
			k++;
		}
	}
}
return k;

}

int main()
{
	ifstream input;
	ofstream output;
	input.open("input1.in");
	output.open("output.in");
	int i=0;
	int T=0;
	 if (input.is_open())
    {
      char c='k';
      while(!input.eof())
	  {

		//reading the first line
		if(i==0){
		int k =0;
	    int t[3];
			while(c!='\n'){
			
			input.get(c);
			t[k]=(c - '0');
	    
			k++;
			
			 }
			int cal =1;
					 for(int j = k-2; j>=0;j--){
						T=T+(t[j]*cal);
						cal=cal*10;
						 }
			
			i++;
		}
		
		//reading the rest 
		for(int j=0;j<T;j++){
			int Smax=0;
			int Kth[1001];
			int s[5];
			int k=0;
			while(c!=' '){
			
					input.get(c);
					s[k]=(c - '0');
	    
					k++;
			
					 }
					int cal =1;
							 for(int j = k-2; j>=0;j--){
								Smax=Smax+(s[j]*cal);
								cal=cal*10;
								//cout<<Smax;
								 }
			 k=0;
			 
			while((c!='\n')){
					input.get(c);
					Kth[k]=(c - '0');
					//cout<<Kth[k];
					k++;
					if(input.eof())
						break;
			
					 }
			//cout <<k;
			int finale;
			finale=manageCase(Kth,k-1);
			output<<"Case #"<<j+1<<": "<<finale<<endl;

			
	  }
	  
	  }
	 
	 }
	 input.close();
	 output.close();



	 getchar();
	 getchar();
	return 0;

}

