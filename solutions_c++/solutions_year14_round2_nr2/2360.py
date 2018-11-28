#include<iostream>
#include<fstream>
#include<vector>
#include<time.h>
#include<algorithm>

#include <sstream> 
#include <string>
using namespace std;


int HowmayFlip(vector<string> &vec,vector<string> &vecDevice)
{
	int count=0;
	vector<string> vecCopy =vec;

	sort(vec.begin(),vec.end());
	sort(vecDevice.begin(),vecDevice.end());

	int strLength=vec[0].length();
	int vecLength=vec.size();
	bool diff[200];
	 int ans = 10000;
	
	for(int m=0;m<vecLength;m++)
	{
	   memset(diff, 0, sizeof(bool)*200);
	   int temp=0;
      for(int j=0;j<strLength;j++)
	  {
		  if(vec[0][j]!=vecDevice[m][j])
		  {
			  temp++;
			  diff[j]=true;
		  }
	  }
		
		  vector<string> X;
          for (int k = 0; k < vecLength; ++k) {
                string Q;
                for (int j = 0; j < strLength; ++j) {
                    if (!diff[j]) {
                        Q = Q + vec[k][j];
                    } else {
                        if (vec[k][j] == '1') Q = Q + '0'; else Q = Q + '1';
                    }
                }
                X.push_back(Q);
            }
            sort(X.begin(), X.end());
            if (X == vecDevice) {
                if (temp < ans) ans = temp;
            }
	}
	
      if (ans == 10000) {
            return -1;
        } else {
           return ans;
        }

}

int main()
{
	int start=clock();
 
	fstream input;
	input.open("B-small-practice.in");
	//input.open("3.txt");
    ofstream out("b-small.txt"); 
	
	int n;//number of test case n
	input>>n;

	for(int i=0;i<n;i++)
	{
	
		int oldnum=0;
		int newnum=0;
		int k=0;
		input>>oldnum;
		input>>newnum;
		input>>k;
		int count=0;

	 
		for(int m=0;m<oldnum;m++)
		{
			for(int n=0;n<newnum;n++)
			{
				int temp=m&n;
				if(temp<k)
					count++;
			}
			
		}

		 

	
		out<<"Case #"<<i+1<<": "<<count<<endl;

	}
	input.close();
	out.close();
    int end=clock();
	cout<<"the total time of running is :"<<end-start<<endl;
	return 0;
}