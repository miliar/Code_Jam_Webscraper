#include<iostream>
#include<string>
#include<cstring>
#include<iomanip>
#include<vector>
using namespace std;

int main()
{
	double C,F,X,lambda;
	double ans1,ans2;
	int cases;
	vector<double> answer;
	
	cin>>cases;
	while(cases--)
	{
	
	cin>>C>>F>>X;
	
	ans1 = X/2.0;
	lambda = C/2.0;
	ans2 = lambda + X/(2.0+F);
	int i=1;
	while(true)
	{
		if(ans2>ans1)
		{
			//cout<<ans1<<"\n";
			answer.push_back(ans1);
			break;
		}
		ans1 = ans2;
		lambda = lambda + C/(2.0+i*F);
		ans2 = lambda + X/(2.0+(i+1.0)*F);
		i++;
	}
	
	}
	
	std::cout<<setprecision(7)<<fixed;					//to include integers also
	for(int i=0 ; i<answer.size() ; ++i)
	{
		cout<<"Case #"<<i+1<<": "<<answer[i]<<"\n";	
	}
	
	return 0;
}