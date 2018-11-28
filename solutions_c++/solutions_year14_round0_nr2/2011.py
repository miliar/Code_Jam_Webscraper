#include <iostream>
#include <cstdlib>
#include <string>
#include <cmath>
#include <algorithm>
using namespace std;
typedef long long ll;
typedef unsigned long long ul;
//Var
long T;
double C,F,X;
long i, j;
long BinarySearch();
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B.o","w",stdout);
	cin >> T;
	for (i = 1; i <= T; i++)
	{
        double sum = 0;
		cin >> C >> F >> X;
		//Goi A + 1 la so lan mua may moi. Tim A
		long A = BinarySearch();
		if (A == 0) if (X/2 < C/2 + X/(F + 2)) A = -1;
		cout << "Case #"<<i<<": ";
		for(j = 0; j <= A; j++)
		{
              sum += C/(j*F+2);              
        }
        sum += X/ ((A + 1)*F +2);
        printf("%0.7lf\n",sum);
              
	}
	//system("pause");
	return 0;
}
long BinarySearch()
{
	long start, end, mid;
	start = 0;
	end = 100000;
	while (start <= end)
	{
		mid = (start + end) / 2;
		if (double(C) / (mid*F + 2) + double(X) / ((mid + 1)*F + 2) < double(X / (mid*F + 2))) start = mid + 1;
		else end = mid - 1;
	}
	while (double(C) / (mid*F + 2) + double(X) / ((mid + 1)*F + 2) < double(X / (mid*F + 2))) mid++;
	while ( (mid>0) && (double(C) / (mid*F + 2) + double(X) / ((mid + 1)*F + 2) > double(X / (mid*F + 2)))) mid--;
	return mid;
}
