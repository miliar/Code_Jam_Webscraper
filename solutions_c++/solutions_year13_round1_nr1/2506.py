#include<iostream>
#include<fstream>
#include<vector>
using namespace std;
double radius, paint;
const double PI= 3.14159265359;
int main()
{
	int testCases;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> testCases;
	for (int a=0; a<testCases; a++)
	{
		double start,temp;
		cin >> radius >> paint;
		start=pow(radius+1,2);
			temp=pow(radius,2);
		start*=2;
		start=2*(pow((radius+1),2)-pow((radius),2))-4;
		temp=-(start)+sqrt(pow(start,2)-(32*(-paint)));
		temp/=8;
	
		
		
			printf("Case #%d: %d\n", a+1, (int)floor(temp));
		}
	}
