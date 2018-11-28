#include<iostream>
#include<sstream>
#include<fstream>
using namespace std;
int main(){
	int testcases;
	int row1;
	int row2;
	ifstream in("A-small-attempt0.in");
	ofstream out("out.txt");
		//enter number of test cases
	in>>testcases;
	//cout<<testcases<<endl;
for(int f=1;f<=testcases;f++)
	{
	
	//enter row number befor 5arba$ 
	in>>row1;
	//cout<<row1<<endl;
	string a;
	int arr1[4];
	int arr2[4];
	getline(in,a);
	for(int e=0;e<4;e++){
		getline(in,a);
		if(e == row1 -1){
			stringstream iss(a);
			int nu1,qq=0;
			while(iss>>nu1){
				arr1[qq]=nu1;
				qq++;
			}
			
		}
		
	}
	
	in>>row2;
	getline(in,a);
	//cout<<row2<<endl;
	for(int e=0;e<4;e++){
		getline(in,a);
		if(e == row2-1){
			stringstream iss(a);
			int nu1,qq=0;
			while(iss>>nu1){
				arr2[qq]=nu1;
				qq++;
			}
			
		}
		
	}
	
/*	cout<<"arr2"<<endl;
	for(int e=0;e<4;e++){
		cout<<arr2[e];
	}
	cout<<"arr2 end"<<endl;
*/	
	int count=0;
	int temp;
	for(int i1=0;i1<4;i1++){
		for(int j1=0;j1<4;j1++){
		if(arr1[i1]==arr2[j1])
		{
		++count;
		temp=arr1[i1];
		}
		}
		}
		if (count==0)
		out<<"Case #"<<f<<": Volunteer cheated!\n";
		else
		if(count==1)
		out<<"Case #"<<f<<": "<<temp<<endl;
		else
		if (count>1)
		out<<"Case #"<<f<<": Bad magician!\n";
		
}
}
