#include"../std_lib_facilities.h"

int main()
{
	ifstream ist("A-small-attempt0.in");
	ofstream ost("output.out");
	int solve,count=0;
	ist>>solve;
	while (solve>count)
	{
		++count;
		int x,t;
		int a[4],f;
		ist>>x;
		for (int i=1; i<=4; ++i)
			if (i==x)
				ist>>a[0]>>a[1]>>a[2]>>a[3];
			else ist>>f>>f>>f>>f;
		ist>>x;
		int mode=0,s=0;
		for (int i=1; i<=4; ++i)
			if (i!=x)
				ist>>f>>f>>f>>f;
			else
			{
				ist>>t;
				for (int j=0; j<4; ++j)
					if (t==a[j])
					{
						++mode;
						s=t;
					}
				ist>>t;
				for (int j=0; j<4; ++j)
					if (t==a[j])
					{
						++mode;
						s=t;
					}
				ist>>t;
				for (int j=0; j<4; ++j)
					if (t==a[j])
					{
						++mode;
						s=t;
					}
				ist>>t;
				for (int j=0; j<4; ++j)
					if (t==a[j])
					{
						++mode;
						s=t;
					}
			}
		switch (mode)
		{
		case 0:
			ost<<"Case #"<<count<<": Volunteer cheated!"<<endl;
			break;
		case 1:
			ost<<"Case #"<<count<<": "<<s<<endl;
			break;
		default:
			ost<<"Case #"<<count<<": Bad magician!"<<endl;
			break;
		}
	}
	return 0;
}