#include <iostream>
#include <fstream>
#include <math.h>


using namespace std;



bool ispalindrome(int x){

	int y = 0;
	int temp = x;
	while (x > 0){
	
		
		y =y*10 + x%10;	

		x = x/10;
		
	}

	if(temp == y)return true;
	return false;

}


void main (){

	fstream fin;
	fstream fout;


	fin.open("input.in",ios::in || ios::binary);
	fout.open("output.txt",ios::out );

	int n;

	fin>>n;

	for (int i = 0 ; i < n ; i++){
	
		int a,b;


		fin>>a;
		fin>>b;

		int c = ceil(sqrt(a)),
			d = floor(sqrt(b));


		int count= 0 ;

		int temp = 0;

		for (int j = c ; j <= d ; j++){
		
			if (ispalindrome(j)){
			
				if (ispalindrome(j*j)){
				
							count++;

				}

			}


		}

		fout<<"Case #"<<i+1<<": "<<count<<endl;
		

		
		


	
	}

}
