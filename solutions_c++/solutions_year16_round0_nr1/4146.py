#include<iostream>
//header file from  http://packages.ubuntu.com/trusty/g++-4.8
using namespace std;
int main()
{
    int T,N;
	cin>>T;
	int array1[10] = {-1,-1,-1,-1,-1,-1,-1,-1,-1,-1};
	int array2[10] = {-1,-1,-1,-1,-1,-1,-1,-1,-1,-1};
	for (int a = 1; a <= T; a++) {
		cin>>N;
		int counter = 2;
		int N1 = N;

		while (true) {
			int d = N1;
			while (d>0) {
				array1[d%10] = d%10;
				d = d/10;
			}
			//int flag = 0;
			int hello = 0;
			for (int i = 0; i < 10; i++) {
				if(array1[i] != array2[i])
				{//flag = 1;
				array2[i] = array1[i];}	
				if(array1[i] == -1)
					hello = 1;

			}

			if(hello == 0)
			{cout<<"Case #"<<a<<": "<<N1<<endl;
			break;
			}
			if(N1 == counter*N){
				cout<<"Case #"<<a<<": INSOMNIA"<<endl;
				break;
			}
			N1 = counter * N;
			
			++counter;
		}
		for (int y = 0; y < 10; y++) {
			array1[y] = -1;
			array2[y] = -1;
		}

	}

    return 0;
}
