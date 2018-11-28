#include<iostream.h>
#include<fstream>
#include<sstream>
#include<string>
#include<math.h>
#include<vector>

using namespace std;
int main()
{
	ifstream in("A-small-attempt1.in");
	ofstream out("output.txt");
	int testcase;
	in>>testcase;
	for(long t=1;t<=testcase;t++)
	{
		string s;
		int arr1[4],arr2[4];
		int firstrow,secondrow;
		in>>firstrow;
		getline(in,s);
		for(int i=1;i<firstrow;i++)
		    getline(in,s);
		for(int i=0;i<4;i++)
	       in>>arr1[i];
        for(int i=0;i<=4-firstrow;i++)
	        getline(in,s);
        in>>secondrow;

          getline(in,s);
        for(int i=1;i<secondrow;i++)
		    getline(in,s);
		for(int i=0;i<4;i++)
	       in>>arr2[i];
        for(int i=0;i<=4-secondrow;i++)
	        getline(in,s);
	        
	        
	        
	        
	        
        int count [2];
        count [0]=0;
        count [1]=0;
        int index=0;
        for(int i=0;i<4;i++)
            {
			for(int j=0;j<4;j++)
                if(arr1[i]==arr2[j])
                {
                	count [index]=arr1[i];
                	index++;
                	break;
                }
                if(index==2)
                   break;
            }
        if(index==0){
        	out<<"Case #"<<t<<": Volunteer cheated!\n";
        }
        else if(index==1){
        	out<<"Case #"<<t<<": "<<count[0]<<endl;
        }else if(index==2){
        	out<<"Case #"<<t<<": Bad magician!\n";
        }
                
        
	}
}