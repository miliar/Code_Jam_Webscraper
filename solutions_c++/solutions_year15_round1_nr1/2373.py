#include <iostream>
#include <fstream>

using namespace std;

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
	//cout << "Hello World" << endl ;
	fstream fs,fo;
	fs.open ("input.txt", std::fstream::in | std::fstream::out | std::fstream::app);
	fo.open ("output.txt", std::fstream::in | std::fstream::out);
	int T;
	fs >> T;
	cout << T << endl;
	for(int itr=1; itr<=T; itr++)
	{
		unsigned long long int ans,maxgap=0,gap=0;
		unsigned long long int res1=0,res2=0;
		fs >> ans;
		unsigned long long int arr[ans];
		for(int itr1 = 0; itr1<ans; itr1++)
			fs >> arr[itr1];
		for(int i=1; i<ans; i++)
		{
			if(arr[i] < arr[i-1])
			{
				gap = arr[i-1] - arr[i];
				if(gap > maxgap)
				{
					maxgap = gap;
				}
				res1 += (arr[i-1]-arr[i]);
			}
		}
		for(int i=0; i<ans-1; i++)
		{
			if(maxgap >= arr[i])
			{
				res2 += arr[i];
				//fo << res2 << endl;
			}
			else
			{
				res2 += maxgap;
				//fo << res2 << endl;
			}
		}
		fo << "Case #" << itr << ": "<< res1 << " " << res2 << endl;
	}
	return 0;
}
