#include<iostream>
#include <sstream>
using namespace std;

int main()
{
	int test;
        cin>>test;
        string output[test];
	
	for(int i=0;i<test;i++)
	{
		
			int reqFri = 0 ; // no of require friends.
			string input;
			int maxLength;
                        cin>>maxLength;
			cin>>input;
                        
                        int totalPeopleYet = 0 ; //store current total audis.
			for(int j=0;j<maxLength+1;j++)
			{
				int needToAdd = 0;
				//System.out.println("to People:"+totalPeopleYet);
                                if(j>0)
				{
					if(totalPeopleYet<j)
					{
						//System.out.println("call");
					       	needToAdd = j - totalPeopleYet;
						reqFri = reqFri + needToAdd;
						
					}
				}
			 int inputNo = input[j] - '0';
			totalPeopleYet = needToAdd + inputNo + totalPeopleYet;
			}
				
			std::ostringstream sstream;
			sstream <<"Case #" << (i+1) << ": "<< reqFri;
			output[i] = sstream.str();
	}
	for(int i=0;i<test;i++)
	{
		cout<<output[i]<<endl;
	}
}
