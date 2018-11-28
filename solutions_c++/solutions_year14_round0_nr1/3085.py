#include <iostream>
#include <fstream>
using namespace std;



int main( int argc, char* argv[] ){

	ifstream is;
	is.open(argv[1],std::ifstream::in);

	ofstream os;
	os.open(argv[2],std::ofstream::out);


	int row1=0;
	int row2=0;
	int A[4],B[4],C[4];
	int case_num=1;
	int find_answer=0;
	int ans=0;
	int case_total=0;
	is>>case_total;
	for(int j=0;j<case_total;j++)
	{
		find_answer=0;
		is>>row1;//the row you choose
		for(int i=0;i<row1;i++)
		{
			is >> A[3] >> A[2] >> A[1] >> A[0];
			//os<<A[3]<<A[2]<<A[1]<<A[0];
		}
		for(int i=0;i<(4-row1);i++)
		{
			is >> C[3] >> C[2] >> C[1] >> C[0];
			//os<<C[3]<<C[2]<<C[1]<<C[0];
		}
		is>>row2;
		for(int i=0;i<row2;i++)
		{
			is >> B[3] >> B[2] >> B[1] >> B[0];
			//os << B[3] << B[2] << B[1] << B[0];
		}
		for(int i=0;i<(4-row2);i++)
		{
			is >> C[3] >> C[2] >> C[1] >> C[0];
			//os<<C[3]<<C[2]<<C[1]<<C[0];
		}
		for(int i=0;i<4;i++)
		{
			for(int k=0;k<4;k++)
			{
				if(A[i]==B[k])
				{
					find_answer++;
					ans=A[i];
				}
			}
		}
		if(find_answer==1)
		{
			os<<"Case #"<<case_num<<": "<<ans<<endl;
		}
		else if(find_answer>1)
		{
			os<<"Case #"<<case_num<<": "<<"Bad magician!"<<endl;
		}
		else
		{	
			os<<"Case #"<<case_num<<": "<<"Volunteer cheated!"<<endl;
		}
		
		case_num++;
	}
return 0;
}
