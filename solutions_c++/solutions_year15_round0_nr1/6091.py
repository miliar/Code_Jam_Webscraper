#include<iostream>
using namespace std;

int countInvitions(int size , char arr[])
{
	int invite = 0;
	int count = arr[0]-48;
	for (int level = 1; level < size; ++level)
	{
		//cout<<"Count : "<<count<<"  level : "<<level << endl;
		if (count >= level)
		{
			count += (arr[level]-48);
		}
		else {
			//cout<<"kvnkgmfk\n";
			int diff = level - count;
			count += diff + (arr[level]-48);
			invite += diff;
		}
	}
	return invite;
}

int main() {
	freopen("mn.in","r",stdin);
	freopen("out.out","w",stdout);
	int test = 0;
	cin>>test;
	for (int i = 0; i < test;)
	{
		int size = 0;
		cin>>size;
		char arr[size+1];
		cin>>arr;

		cout<<"Case #"<<(++i)<<": "<<countInvitions(size+1,arr)<<endl;
	}
	return 0;
}