#include <iostream>
#include <fstream>
#include <algorithm>


//#define PI 3.1415926

using namespace std;



int main()
{
	ofstream output;
	ifstream input;
	input.open("input.txt");
	output.open("output.txt");

	
	
	int T;


	input>>T;// cout<<n<<endl;
	
	//int r,t,n;
	int A, N, m[100]={0};

	for(int i=0;i<T;i++)
	{

		input>>A>>N;
//		cout<<A<<' '<<N<<endl;
		for(int j=0;j<N;j++)
		{
			input>>m[j];
//			cout<<m[j]<<' ';
		}
//		cout<<endl;
		sort(m,m+N);

		int temp=A,counter1=0,counter2=0;

		int j=0;

		while(j<N)
		{
			if(temp>m[j])
			{
				temp+=m[j++];
			}
			else
			{
				counter2=0;
				if(temp-1==0)
				{
					counter1=N-j;
					break;
				}
				else
					while(temp<=m[j])
					{
						temp+=temp-1;
						counter2++;
					}
				if(counter2<N-j)
					counter1+=counter2;
				else
				{
					counter1+=(N-j);
					break;
				}

			}
		}


		output<<"Case #"<<i+1<<": "<<counter1<<endl;
		
	}
		
	input.close();
	output.close();
//	system("pause");
	return 0;
}
