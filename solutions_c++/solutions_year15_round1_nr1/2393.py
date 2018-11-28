#include<iostream>
#include<fstream>
using namespace std;

int main()
{
	ifstream input;
	input.open("A-large.in");
	ofstream output;
	output.open("outL.txt");
	int t, j=1;
	input>>t;
	while(j<=t){
		int n, temp, max=0;
		input>>n;
		int mush[n];
		for(int i=0;i<n;i++){
			input>>mush[i];
			if(i!=0){
				temp = mush[i-1] - mush[i];
				if(temp>max){
					max = temp;
				}
			}
		}
		long long int min1=0, min2=0; int temp1=0, temp2=0;
		for(int i=0;i<n-1;i++){
			temp1 = mush[i] - mush[i+1];
			temp2 = mush[i] - max;
			if(temp1>0){
				min1 += temp1;
			}
			if(temp2>=0){
				min2 += max;
			}else if(temp2<0){
				min2 += mush[i];
			}
		}
		output<<"Case #"<<j<<": "<<min1<<" "<<min2<<endl;
		j++;
	}
	return 0;
}
