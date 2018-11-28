
#include<iostream>
#include<fstream>
#include<vector>
#include<time.h>
#include<algorithm>

#include <sstream> 
#include <string>
using namespace std;


int minEatArray[1001];

int separate(int number){
  int count = 0;
  if(number <=3 ){
	  return 0;
  }
  if(number % 2 == 0){
	  return 2*separate(number/2) + 1;
  } else {
	  return separate(number/2) + separate(number / 2 + 1)  + 1;
  }
}

void initArray(){
	for(int i = 0; i <= 1000; i++){
		minEatArray[i] = separate(i);
	}
}
bool isFinish(vector<int> &vec, int result){
    int size = vec.size();
	int direct = vec[size - 1];
	int sep = 0;
	bool isadd = false;
	for(int i = size - 1; i >=0 ; i--){
	    sep += minEatArray[vec[i]];
		if((vec[i] & (vec[i]-1))!=0 && !isadd){
			isadd = true;
			sep++;
		}
	}
	if(sep + 2 > direct){
		return true;
	}
	return false;

}
int minEat(vector<int> & vec, int maxP, int size)
{
    if(maxP <=3 ){
		return maxP;
	}
	sort(vec.begin(),vec.end());
	int result = 0;
	bool isAdd = false;
	int i = size - 1;
	
	int minResult = vec[i];
	while(i >= 0){
		if(vec[i] > 3){
			result++;
			int temp = vec[i];
			vec.pop_back();
			vec.push_back(temp / 2);
			if(temp % 2 == 0){
				vec.push_back(temp / 2);
			}else{
				vec.push_back(temp / 2  + 1);
			}
			sort(vec.begin(),vec.end());
			i = vec.size() - 1;
			if(isFinish(vec, result)){
				if(result + vec[i] < minResult){
				   minResult = result + vec[i];
				}
			}
		   
		} else {
			break;
		}
	
	}
	if(vec[i]+ result > minResult){
		return minResult;
	}
	return vec[i]+ result;
}


int minEat2(vector<int> & vec, int maxP, int size)
{
	int min1 = maxP ;
	int sum = 0;
    for(int i = 1 ; i <= maxP ; i++) {  
           sum = i ;  
           for(int j = 0 ; j < size ; j++) {  
                if( vec[j] > i ) {  
                    if( vec[j]%i == 0 )  
                        sum += (vec[j]/i-1) ;  
                    else  
                        sum += (vec[j]/i) ;  
                }  
            }  
		   if(min1 > sum){
             min1 = sum ; 
		   }
        }  
	return min1;
}
int main()
{

	int start=clock();
 
	fstream input;
	input.open("B-large.in");
	//input.open("3.txt");
    ofstream out("b-large.txt"); 
	
	int n;//number of test case n
	input>>n;
	initArray();

	for(int i=0;i<n;i++)
	{
	
		int iPlate =0;

		input>>iPlate;
        vector<int> array;
		int maxP = 0;
	
		for(int m=0;m < iPlate; m++)
		{
		   int temp= 0;
		   input>> temp;
		   if(temp > maxP){
			   maxP = temp;
		   }
		   array.push_back(temp);
		}


		//second answer
		 int count=minEat2(array, maxP, iPlate);
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