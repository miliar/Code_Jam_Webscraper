#include<iostream>
//#include<algorithm>
//#include<set>
using namespace std;

int main()
{
	freopen("A-small-attempt2.in","r",stdin);
	freopen("A-small-attempt2.out","w",stdout);

	int T;
	cin>>T;
	for(int i = 0; i<T; ++i)
	{
		int a,b;
		int A[16],B[16];
		cin>>a;
		for(int j = 0; j<16; ++j)
		{
			cin>>A[j];
		}
		//set<int> SA(A+(a-1)*4,A+a*4-1);
		cin>>b;
		for(int j = 0; j<16; ++j)
		{
			cin>>B[j];
		}
		int flag = 0;
		int save;
		for(int k = 0; k<4; ++k)
			for(int k2 = 0; k2<4; ++k2)
			{
				if (A[(a-1)*4+k]==B[(b-1)*4+k2])
					{flag = flag+1;
				save = A[(a-1)*4+k];
				}
				
			}
	     
		if(flag==1)
			cout<<"Case #"<<i+1<<":"<<" "<<save<<endl;
		else if(flag>1)
			cout<<"Case #"<<i+1<<":"<<" "<<"Bad magician!"<<endl;
		else cout<<"Case #"<<i+1<<":"<<" "<<"Volunteer cheated!"<<endl;
	}
}