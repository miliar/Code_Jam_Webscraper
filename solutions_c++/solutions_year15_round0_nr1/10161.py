#include <iostream>
#include<stdio.h>
//#include<math.h>

using namespace std;

#define SIZE 1004
/* run this program using the console pauser or add your own getch, system("pause") or input loop */
int T,N,M;
int Arr[SIZE];
int main(int argc, char** argv) {
	
	int i,j,k,l,t;
	
	freopen("input.txt","r",stdin);
	freopen ("myfile.txt","w",stdout);
	
	//Read No of test cases
	cin >> T;
	
	//Loop for no of test cases
	for(t=1;t<=T;t++)
	{
		cin >> N; //Read max number of Shylevels
		cin >> M;
		
		//loop for reading no of ppl at each level
		for(i=N;i>=0;i--)
		{
			Arr[i]=M%10;
			M=M/10;			
		}//i
		
		int val =Arr[0];
		int ppl =0;
		for(i=1;i<=N;i++)
		{
			if(val < i){
				ppl += i-val;
				val += i-val;
			}
			
			val += Arr[i];
		}//i
		
		cout<<"Case #"<<t<<": "<<ppl<<"\n";
	}//t
	//fclose(stdout);
	return 0;
}

