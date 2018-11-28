#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>

int main(int argc, char *argv[])
{
    int T,count=0;
    int n,m,d;
    int i,j,k;
    int counter;
    char audience[2000];
    int need,newneed,preneed;
    
    freopen("input","r",stdin);
    freopen("output","w",stdout);
    
    for(std::cin >> T;count<T;){
	std::cin >> n;
	m = 0;

	//INPUT
	while(m <= n){
	    i = 0;
	    while(i>'9'||i<'0')
		i = getchar();
	    audience[m]=(i - '0');
	    m++;
	}
	
	m--;
	need = n;

	m--;

	while(m >= 0){
	    need -= audience[m];
	    newneed = m;
	    if(newneed > need){
		need = newneed;
	    }
	    m--;
	}

	count++;

	std::cout <<"Case #" << count << ": " << need <<  std::endl;

	continue;
err:
	std::cout <<"Case #" << count <<": ERROR!" << std::endl;
    }

    return 0;
}

