#include <bits/stdc++.h>
using namespace std;


void solve(){
	int nn;
	cin >> nn;

	if(nn == 0){
		printf("%s\n", "INSOMNIA");
		return;
	}

	bool zero = false;
	bool one = false;
	bool two = false;
	bool three = false;
	bool four = false;
	bool five = false;
	bool six = false;
	bool seven = false;
	bool eight = false;
	bool nine = false;

	int ff = 1;
	while(true){

  		

		char ss[1000000];
		sprintf(ss, "%d", ff*nn);
		if(!zero && strchr(ss, '0')){
			zero = true;	
		}
		if(!one && strchr(ss, '1')){
			one = true;
		}
		if(!two && strchr(ss, '2')){
			two = true;
		}
		if(!three && strchr(ss, '3')){
			three = true;
		}
		if(!four && strchr(ss, '4')){
			four = true;
		}
		if(!five && strchr(ss, '5')){
			five = true;
		}
		if(!six && strchr(ss, '6')){
			six = true;
		}
		if(!seven && strchr(ss, '7')){
			seven = true;
		}
		if(!eight && strchr(ss, '8')){
			eight = true;
		}
		if(!nine && strchr(ss, '9')){
			nine = true;
		}

		if(zero && one && two && three && four && five && six && seven && eight && nine){
			printf("%d\n", ff*nn);
			return;
		}

		ff++;
	}

}


int main ()
{
  	int cc;
  	cin >> cc;
	for (int dd = 1; dd <= cc; ++dd)
	{
  		printf("Case #%d: ", dd);
  		solve();
	}  
  	return 0;
}