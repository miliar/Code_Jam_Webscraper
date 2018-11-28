#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;
struct Pi
{
	int P;
	char A;
};
bool compare(Pi i, Pi j) {return (i.P>j.P);}

int main()
{
	int T;
	cin>>T;
	for(int case_id=0;case_id<T;case_id++)
	{
		int N;
		cin>>N;

		vector<Pi> P;
		P.resize(N);
		for (int i=0;i<N;i++)
		{
			P[i].P=0;
			P[i].A='A'+i;
		}

		for (int i=0;i<N;i++)
			cin>>P[i].P;

		sort(P.begin(),P.end(),compare);
		cout<<"Case #"<<case_id+1<<": ";

		while (P[0].P>0)
		{
			if(P[0].P-P[1].P>1)
			{
				P[0].P-=2;
				cout<<P[0].A<<P[0].A<<" ";
			}
			else
			{
				if (P[0].P==1 && N>2 && P[2].P!=0)
				{
					P[0].P--;
					cout<<P[0].A<<" ";
				}
				else
				{
					if(P[0].P==P[1].P)
					{
						P[0].P--;
						P[1].P--;
						cout<<P[0].A<<P[1].A<<" ";
					}
					else
					{
						P[0].P--;
						cout<<P[0].A<<" ";
					}
				}
			}
			sort(P.begin(),P.end(),compare);
		}
		cout<<endl;
		P.clear();
	
	}
	return 0;	
}