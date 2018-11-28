#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
using namespace std;
bool* Reverse(bool* arr, int len){
	int i,j;
	for(i=0,j=len-1;i<len/2;i++,j--)
	{
		bool temp=arr[i];
		arr[i]=arr[j];
		arr[j]=temp;
	}
	/*while(i<j){
	  bool temp=arr[i];
		arr[i]=arr[j];
		arr[j]=temp;
		i++;
		j--;
	}*/
	return arr;
}
bool* Invert(bool* arr, int len){
	for(int i=0; i<len; i++)
	{
		arr[i]=!arr[i];
	}
	return arr;
}
bool* flip(bool* arr, int len)
{
	arr=Invert(arr,len);
	return arr=Reverse(arr,len);
}



int main() {
	// your code goes here
	long int T=0;    //Number of test cases
	long int N=0;
	   string line;
	  
	   
	   ofstream Myfile ("Out.txt");
	ifstream myfile ("B-large.in"); //Code that opens and reads the input file starts here
	  if (myfile.is_open())
	  { //if statement for opening file
		getline(myfile,line);
		T=atoi(line.c_str());
		cout<<T<<endl;
		long int j=1;
		while ( getline (myfile,line) )
		{ //while loop that runs until the end of file
			bool flag=false;
			int cnt=0;
			
			int len=line.length();
			bool* Arr=new bool[len];
			for(int i=0;i<len;i++)
			{  
				if(line[i]=='+')
					Arr[i]=true;
				else
					Arr[i]=false;

			}
	
			while(!flag)

			{ //while loop that runs untill all pancakes are happy
				int len1=0;
				//bool* temp;
				for(int i=len-1; i>=0;i--)
				{ //inverse for loop that checks the array for unhappy pancakes
					if((Arr[i]==false && Arr[0]==false) || (i==1 && Arr[i]==false && Arr[0]==false))
					{ //if statement that checks value at given index of array
						bool* temp=new bool[i+1];
						for(int j=0;j<i+1; j++)
						{ //for loop that saves the values of portion for flipping in temporary array
							temp[j]=Arr[j];

						} //for loop that saves the values of portion for flipping in temporary array
						temp=flip(temp,i+1);
						for(int k=0; k<i+1; k++) //for loop that saves back flipped array into main array
							Arr[k]=temp[k];
						
						cnt++;
						break;
					} //if statement that checks value at given index of array
					else if((i==1 && Arr[i]==false && Arr[0]==true) || (i==0 && Arr[i]==false)){
							Arr[0]=!Arr[0];
							cnt++;
							break;
						}else if(i!=1 && Arr[i]==false && Arr[0]==true){
							int neg=0;
							for(int y=0; y<i; y++){
								if(Arr[y]==false){
								   neg=1;
								   break;
								}
							}
							if(neg==0){
									  bool* temp=new bool[i];
								for(int j=0;j<i; j++)
								{ //for loop that saves the values of portion for flipping in temporary array
									temp[j]=Arr[j];

								} //for loop that saves the values of portion for flipping in temporary array
								temp=flip(temp,i);
								for(int k=0; k<i; k++) //for loop that saves back flipped array into main array
									Arr[k]=temp[k];
									cnt++;
									break;
							}
					}


				} //inverse for loop that checks the array for unhappy pancakes
				int c=0;
				for(int i=0;i<len;i++)
				{ //for loop for checking if all pancakes are happy
					if(Arr[i]==true)
						c++;
				} //for loop for checking if all pancakes are happy
				if(c==len)
					flag=true;
			}//while loop that runs untill all pancakes are happy
			


		  
				  Myfile<<"Case #"<<j<<": "<<cnt<<endl; //output the highest number counted before falling asleep
				// Myfile<<Fn<<endl;

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
	  
 
  