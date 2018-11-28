#include<string>
#include<iostream>
#include<fstream>
#include<math.h>
using namespace std;

int main(void)
{
	ifstream file;
	file.open("2A-small-attempt6.in");
	ofstream output;
	output.open("result.out");

	int caseNo;
	file >> caseNo;

	for(int t=1; t<= caseNo; t++)
	{
		long long int a, n;
		file >> a >> n;

		long long int mote[100]={0};
		long long int temp;

		for(int tt=0; tt<n; tt++){
			file >> mote[tt];
		}
		for(int tt=0; tt<n; tt++){
			for(int ttt=0; ttt<n-tt-1; ttt++){
				if(mote[ttt+1] < mote[ttt]){
					temp = mote[ttt];
					mote[ttt] = mote[ttt+1];
					mote[ttt+1] = temp;

				}
			}
		}

		long long int result = 0;
		long long int nn = n;
		for(int tt=0; tt<n; tt++){
			if(a <= mote[tt]){
				if(a+a-1 <= mote[tt]){
					if(a == 1){
						result += (n-tt);
						break;
					}else{
						int temp=0;
						while(a<=mote[tt]){
							a += a-1;
							temp += 1;
						}
						//(((mote[tt]-a)/(a-1))+1) > (n-tt) ? result += (n-tt) : result += (((mote[tt]-a)/(a-1))+1);
						if(temp >= (n-tt)){
							result += (n-tt);
							break;
						}
						else{
							result += temp;
							a += mote[tt];
						}
					}
				}else{
					result += 1;
					a += (a-1+mote[tt]);
				}
			}else{
				a += mote[tt];
				nn -= 1;
			}
		}

		//if(result > nn) result = nn;



		output << "Case #" << t << ": ";
		output <<  result << endl;

	}
}