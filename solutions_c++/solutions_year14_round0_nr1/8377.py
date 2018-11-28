#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <set>

using namespace std;

int main()
{
    int tests;
	cin>>tests;
	for (int vb=0; vb<tests; vb++){
		int k1,k2;
		cin>>k1;
		vector<int>my;
		for (int i=1; i<=4; i++)
			for (int j=1; j<=4; j++){
				int temp;
				cin>>temp;
				if (i==k1) my.push_back(temp);
			}
        cin>>k2;
		for (int i=1; i<=4; i++)
			for (int j=1; j<=4; j++){
				int temp;
				cin>>temp;
				if (i==k2) my.push_back(temp);
			}
		 int ans1=0,ans2;
         for (int i=0; i<my.size(); i++)
			 for (int j=i+1; j<my.size(); j++)
				 if (my[i]==my[j]) {
					 ans1++;
					 ans2=my[i];
				 }
		 if (ans1>1) cout<<"Case #"<<vb+1<<": Bad magician!"<<endl;
		 else if (ans1==1) cout<<"Case #"<<vb+1<<": "<<ans2<<endl;
		 else cout<<"Case #"<<vb+1<<": Volunteer cheated!"<<endl;
	}
    return 0;
}