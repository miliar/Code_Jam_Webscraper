#include <iostream>

double work(double speed, double f, double c, double x)
{
	//std::cout<<"speed:"<<speed<<" f: "<<f<<" c: "<<c<<" x: "<<x<<std::endl;

	double noBuyTime = x / speed;

	if (x <= c)
		return noBuyTime;

	if (f * noBuyTime <= c)
		return noBuyTime;

	double buyTime = c / speed + work(speed + f, f, c, x);

	return (noBuyTime <= buyTime) ? noBuyTime : buyTime;
}

int main()
{
	int T;

	std::cin>>T;

	for (int line = 1; line <= T; line++)
	{
		double C, F, X;

		std::cin>>C>>F>>X;


		std::cout<<"Case #"<<line<<": ";
		printf("%.7f\n", work(2.0, F, C, X));
	}

	return 0;
}


