#include<iostream>
#include<stdio.h>
using namespace std;

int main(){
	int T;
	cin>>T;
	int itr;
	for(itr=0;itr<T;itr++){
		int M,N;
		cin>>N;
		cin>>M;
		int *rmax = new int[N];
		int *cmax = new int[M];
		
		int **arr = new int*[N];
		for (int i = 0 ; i < N ; i++ ){
    	 	arr[i] = new int[M];
		}
		for(int i=0;i<N;i++){
			int s=0;
			for(int j=0;j<M;j++){
				cin>>arr[i][j];
				if(s < arr[i][j]){
					s = arr[i][j];	
				}
			}
			rmax[i]=s;
		}
		    
		for(int i=0;i<M;i++){
			int max=0;
			for(int j=0;j<N;j++){
				if(max < arr[j][i]){
					max = arr[j][i];	
				}
			}
			cmax[i]=max;
		}
/*		cout<<"rowmax"<<endl;
		
		for(int i=0;i<N;i++){
		    cout<<rmax[i]<<"\t";
		}
		cout<<endl;    
		cout<<"colmax"<<endl;
		
		for(int i=0;i<M;i++){
		    cout<<cmax[i]<<"\t";
		}
		cout<<endl;
*/		 		
		bool flag1 = false;
		for(int i=0;i<N;i++){
			for(int j=0;j<M;j++){
			if(!(arr[i][j] == cmax[j] || arr[i][j] == rmax[i] )){					
					flag1 = true;
					break; 		
				}		
			}
			if(flag1 == true){
				break;
			}
		}
	
		if(flag1 == true){
			cout<<"Case #"<<itr+1<<": NO"<<endl;	
		}
		else{
			cout<<"Case #"<<itr+1<<": YES"<<endl;	
		}
		for (int i = 0 ; i < N ; i++ ){
    	 	delete [] arr[i];
		}
		delete [] arr;
		delete [] rmax;
		delete [] cmax;				
	}	
	return 0;
}
