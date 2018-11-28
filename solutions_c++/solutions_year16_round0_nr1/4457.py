#include<iostream>
#include<fstream>

using namespace std;

int main(){
	ifstream i("A.txt");
	ofstream o;
	o.open("Aout.txt");
	
	int a[10];
	unsigned int T, N, inc, tmp;
	
	i>>T;
	for(int cnt=0; cnt<T; cnt++){
		i>>N;
		inc = 1;
		
		if(N == 0){
			o<<"Case #"<<cnt+1<<": INSOMNIA"<<endl;
			continue;
		}
		
		for(int ai=0; ai<10; ai++){// initialize seen numbers to zero
			a[ai] = 0;
		}
		
		int done = 0;
		do{
			tmp = inc*N;
			
			while(tmp>0){ //initialize the seen numbers to one
				int r = tmp%10;
				a[r] = 1;
				tmp = tmp/10;
			}
			
			done = 1;
			for(int ai=0; ai<10; ai++){ // confirm whether the job is done
				if(a[ai] == 0)
					done = 0;
			}
			
			if(!done)	// if not done increment the count of multiplier
				inc++;
		}while(!done);
		
		// now all the digits are seen 
		o<<"Case #"<<cnt+1<<": "<<inc*N<<endl;
	}	
	
	i.close();
	o.close();
	return 0;
}
