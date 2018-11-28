#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{
    int test;
	cin >> test;
	for(int t=0; t<test; t++)
	{
		long N;
		cin >> N;
		int ch[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
		long m = N;
		if(m == 0)
		{
			cout << "Case #" << t+1 << ": " << "INSOMNIA" << endl;
			continue;
		}
		while(true)
		{
			long a = N;
			while(a != 0)
			{
				ch[a%10] = 1;
				a = a/10;
			}
			int s = 0;
			for(int i=0; i<10; i++) s+=ch[i];
			if(s == 10) break;
			N += m;
		}
		cout << "Case #" << t+1 << ": " << N << endl;
	}
	
    return 0;
}
