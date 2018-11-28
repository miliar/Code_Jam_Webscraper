#include<iostream>
#include<vector>
using namespace std;
void main1()
{
	double c,f,x,t=0;
	double prate=2;	
	cin>>c>>f>>x;
	double timefornextfarm;
	double pt=x/prate;
	vector<double> res;
	res.push_back(pt);
	while(1)
	{
		timefornextfarm=c/prate;
		t+=timefornextfarm;
		prate+=f;
		res.push_back(t+(x/prate));
		if(res.back()-res[res.size()-2]>0.00000001)
		{
			//printf("intput: c=%f f=%f x=%f\n",c,f,x);
			//for (int i = 0; i < res.size(); i++)
			//{
			//	printf("%.8f ",res[i]);
			//}	
			//printf("\nanswer is:");
			printf("%.7f",res[res.size()-2]);
			return;
		}
	}
}
void main()
{
	freopen("input.txt","rt",stdin);
	freopen("output.txt","wt",stdout);
	int n=0;
	cin>>n;
	for(int i=0;i<n;i++)
	{	
		cout<<"Case #"<<i+1<<": ";
		main1();
		cout<<endl;
	}
}

