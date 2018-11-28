#include <iostream>
#include <algorithm>

int main() {
	int n, r, m[4], m2[4], m3[8], idx(0), t;
	std::cin>>n;
	for (int i=0; i<n; i++)
	{
		std::cin>>r;
		for (int j=0; j<4; j++) {
			if (j==r-1)
				std::cin>>m[0]>>m[1]>>m[2]>>m[3];
			else
				std::cin>>t>>t>>t>>t;
		}
		std::cin>>r;
		for (int j=0; j<4; j++) {
			if (j==r-1)
				std::cin>>m2[0]>>m2[1]>>m2[2]>>m2[3];
			else
				std::cin>>t>>t>>t>>t;
		}
		std::fill(m3, m3+8, 0);
		std::sort(m, m+4);
		std::sort(m2, m2+4);
		std::set_intersection(m, m+4, m2, m2+4, m3);
		if (m3[0]==0)
			std::cout<<"Case #"<<i+1<<": Volunteer cheated!\n";
		else if (m3[1]==0)
			std::cout<<"Case #"<<i+1<<": "<<m3[0]<<'\n';
		else if (m3[1]!=0)
			std::cout<<"Case #"<<i+1<<": Bad magician!\n";
	}
	std::cout<<std::endl;
	return 0;
}