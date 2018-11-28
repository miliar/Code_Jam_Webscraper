#include <iostream>
int main() {
	int ntc;
	std::cin>>ntc;
	for (int i=1; i<=ntc; i++)
	{
		long om, nm, k, count(0);
		std::cin>>om>>nm>>k;
		for (long j=0; j<om; j++)
			for (long jj=0; jj<nm; jj++)
				if ((j&jj) < k)		
					count++;
		std::cout<<"Case #"<<i<<": "<<count<<'\n';
	}
	return 0;
}