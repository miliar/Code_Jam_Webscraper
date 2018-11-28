#include <iostream>
#include <map>
using namespace std;

int main(int argc, char const *argv[])
{
	int N, i=1;
	cin >> N;
	while(N--){
		map<int,bool> count;
		for(int i=0 ; i<10 ; i++)
			count[i] = false;
		long long in, sum=0, out = 0, see = in;
		cin >> in;
		while(sum<10 && in){
			out++;
			long long x = out * in;
			see = x;
			while(x && sum<10){
				if(count[x%10] == false){
					count[x%10] = true;
					sum++;
				}
				x /= 10;
			}
		}
		cout << "Case #" << i++ << ": ";
		if (out)
			cout << see << endl;
		else
			cout << "INSOMNIA" << endl;
	}
	return 0;
}