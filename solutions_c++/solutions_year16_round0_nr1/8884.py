#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
using namespace std;


int main() {
	// your code goes here
	long int T=0;    //Number of test cases
	long int N=0;
	   string line;
	   
	   ofstream Myfile ("Out.txt");
	ifstream myfile ("A-large.in"); //Code that opens and reads the input file starts here
	long int Fn=0;
	  if (myfile.is_open())
	  { //if statement for opening file
		getline(myfile,line);
		T=atoi(line.c_str());
		cout<<T<<endl;
		long int j=1;
		while ( getline (myfile,line) )
		{ //while loop that runs until the end of file
			long int m=2;
		  N=atoi(line.c_str());
		  bool flag=false;
		   bool zero=false;
		   bool one= false;
		   bool two= false;
		   bool three=false;
		   bool four=false;
		   bool five=false;
		   bool six=false;
		   bool seven=false;
		   bool eight=false;
		   bool nine=false;
		  flag=false;
		  Fn=N;
		  if(N!=0)
		  { //if statement that checks number is non zero
				 long int n=N;
				  long int rem=0;
				  do
				  { //while loop that runs until falls sleep starts
					 
					  
					  while(n!=0)
					  { //while loop for getting digitis starts
						  rem=n%10;
						  n=n/10;
						  switch(rem){ //switch starts
						  case 0:
							  zero=true;
							  break;
						  case 1:
							  one=true;
							  break;
						  case 2:
							  two=true;
							  break;
						  case 3:
							  three=true;
							  break;
						  case 4:
							  four=true;
							  break;
						  case 5:
							  five=true;
							  break;
						  case 6:
							  six=true;
							  break;
						  case 7:
							  seven=true;
							  break;
						  case 8:
							  eight=true;
							  break;
						  case 9:
							  nine=true;
							  break;
						  } //switch ends
					  } //while loop for getting digits starts
					  if(zero==true)
						  if(one==true)
							  if(two==true)
								  if(three==true)
									  if(four==true)
										  if(five==true)
											  if(six==true)
												  if(seven==true)
													  if(eight==true)
														  if(nine==true)
															  flag=true; 

					  if(!flag)
					  {
						  Fn=m*N;
					  m=m+1;
					   n=Fn;
					  }
				  } while(!flag);//while loop that runs until falls sleep ends
				   
				  Myfile<<"Case #"<<j<<": "<<Fn<<endl; //output the highest number counted before falling asleep
				// Myfile<<Fn<<endl;

		  } //if statement that checks number is non zero
		  else
			  { 
				  Myfile<<"Case #"<<j<<": "<<"INSOMNIA"<<endl;
			  
		  }
		  j++;
		} //while loop that runs until the end of file
		Myfile.close();
	  } //if statement for opening file
	  else cout << "Unable to open file"; 
	  return 0;
}


   
  /* ofstream Myfile ("example.txt"); //Code for writing output into output file starts here
	  if (Myfile.is_open())
	  {
		Myfile << inv;
		//Myfile << "This is another line.\n";
		Myfile.close();
	  }
	  else cout << "Unable to open file"; //Code for writing output into output file ends here
	  */
	  
 
  