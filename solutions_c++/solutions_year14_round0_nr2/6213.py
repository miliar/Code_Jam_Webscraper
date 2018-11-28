# include <cstdio>
# include <cstring>
# include <cmath>
# include <cstdlib>
# include <iostream>
# include <vector>
# include <algorithm>
# include <queue>
# include <set>
# include <map>

using namespace std;

int main()
{
  int T;
  scanf("%d",&T);
  for(int t=1;t<=T;t++)
  {
	double C,F,X;
	cin>>C>>F>>X;
	double pr = 2;
	double time_elap=0;
	double prev=X+1,curr = time_elap+(X/pr);
	while(prev > curr){
		time_elap += (C/pr);
		pr = pr + F;
		prev = curr;
		curr = time_elap+(X/pr);
		//cout<<" PR = "<<pr<<" Time = "<<curr<<endl;
	}
	//cout<<"Case #"<<t<<": "<<prev<<" c = "<<curr<<endl;
	//cout<<"Case #"<<t<<": "<<prev<<endl;
	cout<<"Case #"<<t<<": ";
	printf("%.7f",prev);
	cout<<endl;
  }
return 0;
}
