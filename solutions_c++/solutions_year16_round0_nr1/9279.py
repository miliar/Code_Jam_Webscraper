#include <iostream>
#include <cstdio> 
#include <cstring>
#include <cstdlib> 
#include <set>
#include <cmath>
#include <cstdlib>
#include <string>

using namespace std;


int main() {
        int cases=0;
        cin >> cases;
                
        for(int casesIter=0;casesIter<cases;casesIter++) {
                long num;
                scanf("%ld\n", &num);
		
	        bool occur[10] = {false};
		int sum=0;
		for(int i=1;i<=1000;i++)
		{
			long aNum = i*num;
			while(aNum != 0)
			{
				if( occur[aNum%10] != true){
					occur[aNum%10] = true;
					sum+= (aNum%10) + 1;
					if( sum ==55)
						cout<<"Case #"<<casesIter<<": "<<i*num<<endl;
				}
				aNum /= 10;
			}
		}
		if(sum != 55)
			cout<<"Case #"<<casesIter<<": INSOMNIA"<<endl;
		sum=0;
		for(int i=0;i<10;i++)
			occur[i] = false;
	}
	

	return 0;
}
