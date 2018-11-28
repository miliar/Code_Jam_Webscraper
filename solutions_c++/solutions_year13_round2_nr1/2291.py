#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <math.h>

using namespace std;

int main(){

	//	ifstream in ("C:/Users/weilu/Downloads/split.in");
//		ifstream in ("B-small-practice.in");
//		ofstream out ("out.txt" );
	freopen ("C:/Users/weilu/Downloads/A-small-attempt2.in","r",stdin);
	freopen("test.out", "w", stdout);
//	freopen("test.in", "r", stdin);


	int T;
	cin >> T;
	for(int ii = 0 ;ii <T ;ii++)
	{
		long long A;
		cin >> A;
		int N;
		cin >> N;
		long long  a;
		vector<long long > all;
		for (int i = 0; i < N; i++)
		{
			cin >> a;
			all.push_back(a);
		}
		sort(all.begin(), all.end() );
		long long total = A ;
		int count = 0;
		for (int i = 0; i < N; i++)
		{
			if( all[i] >= total && all[i] < 2*total - 1){
				// add point
				count++;
				total = 2*total - 1 + all[i];
	//			cout<< "1 i is "<<i << "  total is "<<total <<endl;
			}
			else if ( all[i] < total ){
				total += all[i];
	//			cout<< "2 i is "<<i << "  total is "<<total <<endl;
			}
			else if ( all[i] >= 2*total -1 ){
				long long old = total;
				long long temp = all[i];
				int cc = 0 ;
				while ( temp > total -1 && i +cc < N ){
					total += total - 1;
					cc++;
				}
				if ( i + cc >= N )
				{
//					total += temp;
					total = 2*old -1;
					count++;
				}
				else
				{
					total += temp;
					count = count +cc;
				}
 //				cout<< "3 i is "<<i << "  total is "<<total <<endl;
			}
			else
			{
				cout <<"not possible\n";
			}
		}

		cout<< "Case #"<<ii+1<<": "<<count <<endl;
	}

}