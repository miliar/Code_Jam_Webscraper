#include<cstdio>
#include<iostream>

using namespace std;

int main()
{
	int t;
	int a,b;
	int test = 1;
	int count;
	int c[10] = {1,4,9,121,484};
	scanf ("%d",&t);
	while(t--)
	{
		count = 0;
		scanf ("%d%d",&a,&b);
		for ( int i = 0; i < 5; i++ ) {
			if ( c[i] >= a && c[i] <= b ) {
				count++;
			}
		}
		cout << "Case #"<<test<<": "<<count << endl;
		test++;
	}
	return 0;
}
