#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	int T;
	cin>>T;

	for(int i=0; i<T;i++)
	{
		int vec[16];
		vector<int> u1, u2, ans;
		int row_num;	
		int L;

		cin>>row_num;
		cin>>vec[0]>>vec[1]>>vec[2]>>vec[3]>>vec[4]>>vec[5]>>vec[6]>>vec[7]>>vec[8]>>vec[9]>>vec[10]>>vec[11]>>vec[12]>>vec[13]>>vec[14]>>vec[15];
		u1.push_back(vec[0 + (row_num-1)*4]);
		u1.push_back(vec[1 + (row_num-1)*4]);
		u1.push_back(vec[2 + (row_num-1)*4]);
		u1.push_back(vec[3 + (row_num-1)*4]);
		
		cin>>row_num;
		cin>>vec[0]>>vec[1]>>vec[2]>>vec[3]>>vec[4]>>vec[5]>>vec[6]>>vec[7]>>vec[8]>>vec[9]>>vec[10]>>vec[11]>>vec[12]>>vec[13]>>vec[14]>>vec[15];
		u2.push_back(vec[0 + (row_num-1)*4]);
		u2.push_back(vec[1 + (row_num-1)*4]);
		u2.push_back(vec[2 + (row_num-1)*4]);
		u2.push_back(vec[3 + (row_num-1)*4]);

		for(int j=0; j<4;j++)
		{
			vector<int>::iterator it = find(u1.begin(), u1.end(), u2[j]);
			if(it != u1.end())
				ans.push_back(u2[j]);
		}

		L = ans.size();
		if(L==1)
			cout<<"Case #"<<i+1<<": "<<ans[0]<<endl;
		else if(L>1)
			cout<<"Case #"<<i+1<<": Bad magician!"<<endl;
		else
			cout<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
	}
}
