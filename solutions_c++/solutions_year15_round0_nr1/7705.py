#include<iostream>
#include<fstream>


#define SIZE 1002

using namespace std;

int main() {
	long T;
	int S, r, sum;
	char arr[SIZE];
	ifstream fin;
	ofstream fout("outputA.out");
	fin.open("A-large.in");
	fin>>T;
    for (long t=0; t<T; ++t) {
        fin >> S;
		fin >> arr;
		r=0;
		sum=arr[0]-48;
        for (int i=1; i<=S; ++i)	{
			arr[i]-=48;
			if (sum<i)     {
				r+=(i-sum);
				sum+=(i-sum);
				}
			sum+=arr[i];
            }   
        fout<<"\nCase #"<<t+1<<": "<<r;
    }
}




    
