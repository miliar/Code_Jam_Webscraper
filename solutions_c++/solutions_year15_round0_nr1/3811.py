
#include<iostream>
#include<fstream>
#include<vector>
#include<time.h>
#include<algorithm>

#include <sstream> 
#include <string>
using namespace std;



int minFriend(vector<int> &vec, int size)
{
	if(size <= 1){
		return 0;
	}
	int sum = vec[0];
	int count = 0;
	for(int i = 1; i < size; i++){
		if(sum >= i){
		   sum += vec[i];
		} else if(vec[i] > 0){
			while(sum < i) {
		       //count= i - sum;
			   //sum = sum + count;
				count++;
				sum++;
			}
			sum += vec[i];
		}
	}
	return count;
}

int main()
{

	int start=clock();
 
	fstream input;
	input.open("A-large.in");
	//input.open("3.txt");
    ofstream out("a-large.txt"); 
	
	int n;//number of test case n
	input>>n;

	for(int i=0;i<n;i++)
	{
	
		int sMax =0;

		input>>sMax;
        vector<int> array;
		char ch;
		input.get(ch);
		for(int m=0;m <= sMax; m++)
		{
			//char ch;
			input.get(ch);
			int temp = ch -'0';
		
			array.push_back(temp);
		}


		//second answer
		 int count=minFriend(array, sMax + 1);
		 out<<"Case #"<<i+1<<": "<<count<<endl;
	
		/*if(count!=-1)
		{
			out<<"Case #"<<i+1<<": "<<count<<endl;
		}
		else
		{
		    out<<"Case #"<<i+1<<": NOT POSSIBLE"<<endl;
		}*/

	}
	input.close();
	out.close();
    int end=clock();
	cout<<"the total time of running is :"<<end-start<<endl;
	return 0;
}