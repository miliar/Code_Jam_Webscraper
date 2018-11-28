#include <iostream>
#include <algorithm>
using namespace std;
int motes[100];
int main()
{
	int T;
	cin>>T;
	int num = 1;
	while(T--) {

		int N;
		
		int A;
		
		cin>>A>>N;
		for(int m=0; m<N; m++)
			cin>>motes[m];
		sort(motes, motes+N);

		int min_cnt;

		//0Èí¼ö, nÁ¦°Å
		min_cnt = N;

		//xÈí¼ö, n-xÁ¦°Å
		int opt_cnt = 0;
		for(int i=0; i<N; i++) {
			if( A == 1 )
				break;
			if( opt_cnt >= min_cnt )
				break;

			while( A <= motes[i] ) {
				opt_cnt++;
				A += A-1;
				
				if( opt_cnt >= min_cnt )
					break;
			}
			A += motes[i];

			min_cnt = min(min_cnt, opt_cnt + N-(i+1));
		}

		cout<<"Case #"<<num++<<": "<<min_cnt<<endl;
	}

	return 0;
}