#include <iostream>
#include <fstream>
using namespace std;
int arr[10];
static int caseNum;

void countSheep(long long number, int count, int i){
	
	int index;
	long long temp;
	ofstream outfile;
  	outfile.open("output.txt", std::ios_base::app);
	if(number==0){
		outfile << "Case #"<<caseNum<<": "<<"INSOMNIA"<<endl;
		return;
	}
	temp=number*i;
	while(temp!=0)
  	{
     	index=temp%10;
     	if(arr[index]!=1){
     		arr[index]=1;
     		count++;
     	}
     	temp /= 10;
  	}	
  	if(count==10){
     	outfile << "Case #"<<caseNum<<": "<<number*i << endl;
     	outfile.close();
     	return;
     }  
     else{
     	countSheep(number,count,i+1);
     }
}
int main()
{
	int t,count=0;
	long number;
	ifstream myfile ("b.txt");
	if (myfile.is_open())
  	{
  		myfile >> t;
	    while(myfile>>number){
	    	caseNum++;
	    	for(int i=0;i<10;i++)
	    		arr[i] = 0;
	   		countSheep(number,count,1);
	   		count=0;
		}
		myfile.close();
  	}
	return 0;
}