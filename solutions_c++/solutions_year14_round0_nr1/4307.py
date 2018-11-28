#include <iostream>
#include <string>
#include <fstream>
using namespace std;
int main()
{
	getline(jhoom,num);
	int total=atoi(num.c_str());
	for(int temp=0;temp<total;temp++)
	{

		jhoom>>sel1;
		sel1--;
		for(int t=0;t<4;t++){
			for(int te=0;te<4;te++){
			jhoom>>arr1[t][te];
			}
		}
		cout<<endl;
		jhoom>>sel2;
		sel2--;
		for(int t=0;t<4;t++){
			for(int te=0;te<4;te++){
			jhoom>>arr2[t][te];
			}
		}


		for(int tem=0;tem<4;tem++){
			for(counter=0;counter<4;counter++){
				if(arr1[sel1][tem]==arr2[sel2][counter])
			{
			match++;
			number=arr1[sel1][tem];
			}
			}
		}




		if(match==0){
			yo<<"Case #"<<temp+1<<": Volunteer cheated!"<<endl;
		}
		else if(match>1){
			yo<<"Case #"<<temp+1<<": Bad magician!"<<endl;		
		}
		else if(match==1){
			yo<<"Case #"<<temp+1<<": "<<number<<endl;				
		}



			match=0;
			number=-1;
	}
	
	
	
		system("pause");
	
}




