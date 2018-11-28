#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main() {
    // your code goes here
	int T,N,need,sum_here,num,len,cases=1;
	ifstream inf("A-small-attempt0.in");
	ofstream outf("output.txt");
	inf>>T;
	while(T--)
	{
		inf>>N;
		int arr[N+1];
        inf>>num;
		for(int n=N;n>=0;n--) { arr[n] = num%10; num /= 10;}
		sum_here = arr[0];
		need=0;
		for(int n=1;n<=N;n++)
		{
			if(sum_here < n && arr[n]!=0)
			{
				need += (n-sum_here);
                sum_here += need + arr[n];
			}
			else
			{sum_here += arr[n]; }
		}
        cout<<"Case #"<<cases<<": "<<need<<endl;
        outf<<"Case #"<<cases<<": "<<need<<endl;
        cases++;
	}
	return 0;
}
