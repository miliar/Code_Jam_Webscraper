# include <iostream>
# include <cstdio>

using namespace std;

int main()
{
	float C,F,X,_time,_time1,_time2,current;
	int test_case,i;
	scanf("%d",&test_case);
	for(i=0;i<test_case;i++)
	{
		scanf("%f%f%f",&C,&F,&X);
		_time=0.0;
		current=2.0;
		while(1)
		{
			_time1=_time+(X/current);
			_time2=_time+(C/current)+(X/(current+F));
			if(_time1<_time2)
				break;
			else
			{
				_time=_time+(C/current);
				current=current+F;
			}
		}
		printf("Case #%d: %f\n",i+1,_time1);
	}
	return 0;

}