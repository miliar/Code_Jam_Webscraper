#include<cstdio>
#include <iostream>
#include <cstring>
#include <iomanip>
using namespace std;

int count = 0;
	
double *param;
double* output;
float timer;

void cookies()
{
	double cookiePerSecond = 2.0;
	double C = param[0];
	double F = param[1];
	double X = param[2];
	double totalTime = 0;
	
	while(X/cookiePerSecond >= (C/cookiePerSecond) + (X/(cookiePerSecond+F)))
	{
			totalTime += C / cookiePerSecond;
			cookiePerSecond += F;
	}
	totalTime += X / cookiePerSecond;
	output[count] = totalTime;
	
	
	
}

int main(){
	int t;
	int temp;
	int i, j,k=0;
	param = new double[3];
	cin >> t;
	temp = t;
	output = new double[temp];
	timer = 0;
	while(t--)
	{
		for(i=0;i<3;i++)
		{
			cin >> fixed >> setprecision(5) >> param[i];
		}
		
		cookies();
		count++;
	}
	
	k = 0;
	while(temp--)
	{
			//cout << fixed << setprecision(2) << param[i];
		cout << "Case #" << k+1 << ": " << fixed << setprecision(7) << output[k] << endl;
		k++;
	}

	
	return 0;
}
