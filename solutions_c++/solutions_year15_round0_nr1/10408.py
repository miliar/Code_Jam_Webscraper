#include <iostream>     // std::cout
#include <functional>   // std::multiplies
#include <numeric>      // std::partial_sum
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;



int main(){
//    freopen("input" , "r" , stdin);
//    freopen("output" , "w" , stdout);
int tests=0;
int t=0;
int count=0;
int r;
std::vector<int> vec;
std::cin>>count;

while (tests !=count) {
        int pos=0;
	int friends =0;
	int staud=0;
	int shy;
	vec.clear();

        

	std::cin>>r >>t;
		//while(t!=-1)
	for (shy=0;shy<=r;shy++)	
		{
   			vec.push_back(t%10);
   			t/=10;
		}
        std::reverse(vec.begin(),vec.end());

			int i=0;
			 for (std::vector<int>::iterator it = vec.begin() ; it != vec.end(); ++it) {
				staud= std::accumulate(vec.begin(),it,friends);
				
				if (i-staud>0) 
					friends+=i-staud;

//					std::cout<<" i: "<<i<<" staud: "<<staud<<" friends: " <<friends<<std::endl;
		//std::cout<<"friends = "<< friends<<" Iterator: "<<*(vec.begin()+i)<<" i: "<<i<<" staud:"<<staud<<std::endl;
				i++;
//				std::cout<<" i++: "<<i<<" staud: "<<staud<<" friends: " <<friends<<std::endl;

	}




// for (std::vector<int>::iterator it = vec.begin() ; it != vec.end(); ++it)
//    std::cout << ' ' << *it;
//  std::cout << '\n';
std::cout<< "Case #" <<tests+1<<": "<<friends<<std::endl;
tests++;
}
}


//int aud=0;
//scanf("%d", &T);
//  for (int it = 1; it <= T; it++) solveCase(it);
