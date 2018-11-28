#include <iostream>
#include <algorithm>

using namespace std;

int main(){
  int Test;
  cin >> Test;

  for(int t=1;t<=Test;++t){
	int Num, Capacity;
	cin >> Num >> Capacity;
	vector<int> files(Num, 0);
	for(int i=0;i<Num;++i)
	  cin >> files[i];
	sort(files.begin(), files.end());

	int ret = 0;
	int b=0, e = Num-1;
	while(b<=e){
	  if(b == e){
		++ret;
		break;
	  }
	  if(files[b] + files[e] > Capacity){
		++ret;
		--e;
	  }
	  else{
		++ret;
		++b, --e;
	  }
	}

	cout << "Case #" << t << ": " << ret << endl;
  }

  return 0;
}
