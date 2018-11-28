#include<iostream>
#include<cstdio>

using namespace std;

int main()
{
	int t;
	cin>>t;
	string out[t];
	for(int k=0;k<t;k++){
		int p1rows[4],p1columns[4],p1diag[2];
		int p2rows[4],p2columns[4],p2diag[2];
		for (int i = 0; i < 4; ++i)
		{
			p1rows[i]=0;p1columns[i]=0;p1diag[i%2]=0;
			p2rows[i]=0;p2columns[i]=0;p2diag[i%2]=0;

		}
		bool foundT = false;
		for (int i = 0; i < 4; ++i)
		{
			string line="";
			cin>>line;
			for (int j = 0; j < 4; ++j)
			{
				if (line[j]=='O')
				{
					p1rows[i]++;
					p1columns[j]++;
					if (i==j)
					{
						p1diag[0]++;
					}
					else if (i+j==3)
					{
						p1diag[1]++;
					}
				}
				if (line[j]=='X')
				{
					p2rows[i]++;
					p2columns[j]++;
					if (i==j)
					{
						p2diag[0]++;
					}
					else if (i+j==3)
					{
						p2diag[1]++;
					}
				}
				if (line[j]=='T')
				{
					foundT=true;
					p1rows[i]++;
					p1columns[j]++;
					if (i==j)
					{
						p1diag[0]++;
					}
					else if (i+j==3)
					{
						p1diag[1]++;
					}
					p2rows[i]++;
					p2columns[j]++;
					if (i==j)
					{
						p2diag[0]++;
					}
					else if (i+j==3)
					{
						p2diag[1]++;
					}
				}
			}
		}
		int sum=0;
		bool done=false;
		for (int i = 0; i < 4; ++i)
		{
			if (p1rows[i]==4)
			{
				out[k]="O won";
				done=true;
				break;

			}
			else if (p1columns[i]==4)
			{
				out[k]="O won";
				done=true;
				break;
			}
			else if (p2rows[i]==4)
			{
				out[k]="X won";
				done=true;
				break;
			}
			else if (p2columns[i]==4)
			{
				out[k]="X won";
				done=true;
				break;
			}
			sum+= p1rows[i]+p2rows[i];

		}
		if (done==true)
		{
			continue;
		}
		for (int i = 0; i < 2; ++i)
		{
			if (p1diag[0]==4 || p1diag[1]==4)
			{
				out[k]="O won";
				done=true;
				break;
			}
			else if (p2diag[0]==4 || p2diag[1]==4)
			{
				out[k]="X won";
				done=true;
				break;
			}
		}
		if (done==true)
		{
			continue;
		}
		//cout<<sum;
		if ( (foundT==true && sum==17) || (foundT==false && sum==16) )
		{
			out[k]="Draw";
			continue;
		}
		else{
			out[k]="Game has not completed";
		}


	}
	for(int k=0;k<t;k++){
		//printf("Case #%d: %s\n",k+1,out[k]);
		cout<<"Case #"<<k+1<<": "<<out[k]<<endl;
	}

	return 0;
}