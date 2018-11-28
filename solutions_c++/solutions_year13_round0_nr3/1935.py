#include <fstream>
#include <vector>
using namespace std;

int chk(long long tmp)
{
	char str[16];

	int pos=0;
	while(tmp)
	{
		str[pos++] = (tmp%10)+'0';
		tmp/=10;
	}
	str[pos]=NULL;

	int flag = 0;
	for(int i=0;i<strlen(str)/2;i++)
	{
		if(str[i] != str[strlen(str)-1-i]) 
		{
			flag = 1;
			break;
		}
	}
	if(flag == 0) return 1;
	return 0;
}

int main()
{
	ifstream fin("C-large-1.in");
	ofstream fout("out.txt");
	vector<long long> v;
	char str[16];
	int T;
	long long A, B;

	for(long long i=1;i<=10000000;i++)
	{
		long long tmp;
		if(chk(i))
		{
			tmp = i*i;
			if(chk(tmp)) 
				v.push_back(tmp);
		}
	} 

	fin >> T;
	for(int i=1;i<=T;i++)
	{
		fin >> A >> B;
		int cnt=0;
		for(int j=0;j<v.size();j++)
		{
			//cout << "       " << v[j] << endl;
			if(v[j]<A) continue;
			else if(B<v[j])break;
			cnt++;
		}
		fout << "Case #" << i << ": " << cnt << endl;
	}

}