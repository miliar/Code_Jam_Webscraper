//Email:kingshuk1000@gmail.com

//Just for fun :P

#include<iostream>

using namespace std;

int main()
{
	int i,j,k;

	freopen("B-small-attempt0.in", "rt", stdin);
	freopen("A-small.out","wt",stdout);
	int T;
	cin>>T;
	cout<<std::fixed;
	cout.precision(7);
	for(i=0;i<T;i++)
	{
		double c,f,x,told,t;
		cin>>c;
		cin>>f;
		cin>>x;
		told=x/2;
		j=0;
		while(1)
		{
			j++;
			t=0;
			for(k=0;k<j;k++)
			{

				t+=c/(2+k*f);
			}
			t+=x/(2+j*f);
			if(t>told)
			{
				cout<<"Case #"<<i+1<<": "<<told<<endl;
				break;
			}
			else
			{
				told=t;
			}
		}



	}

	}




