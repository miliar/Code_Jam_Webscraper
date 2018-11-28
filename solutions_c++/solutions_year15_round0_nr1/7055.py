#include <iostream>
#include <cstring>

using namespace std;

char stream[1004];

int main(void)
{
	int N;
	cin>>N;

	int people;
	for (int i=0;i<N;i++)
	{
		cin>>people>>stream;
		int str_len=strlen(stream);
		int tmp_sum=0;
		int cnt=0;
		for (int j=0;j<str_len;j++)
		{
			tmp_sum+=stream[j]-'0';
			if (j>=tmp_sum)
			{
				cnt++;
				tmp_sum++;
			}
			//cout<<tmp_sum<<" ";
		}
		cout<<"Case #"<<i+1<<": "<<cnt<<endl;
	}

	return 0;
}