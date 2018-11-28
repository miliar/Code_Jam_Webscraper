#include <iostream>
#include <fstream>
#include <string>
#include <set>
#include <vector>
using namespace std;

int main()
{
	ofstream out("A-small-attempt0.out");
	ifstream in("A-small-attempt0.in");
	cin.rdbuf(in.rdbuf());
	cout.rdbuf(out.rdbuf());
	 int n;
	cin>>n;
	for(int c=1;c<=n;c++){
		int first_row,seconde_row;
		cin>>first_row;
		set<int> flag;
		vector<int> ans;
		int num;
		for(int i=1;i<=(first_row-1)*4;i++)
			cin>>num;
		for(int i=1;i<=4;i++){
			cin>>num;
			flag.insert(num);
		}
		for(int i=first_row*4+1;i<=16;i++)
			cin>>num;
		cin>>seconde_row;//第二次改变顺序后的行
		for(int i=1;i<=(seconde_row-1)*4;i++)
			cin>>num;
		for(int i=1;i<=4;i++){
			cin>>num;
			if(flag.count(num)>0)
				ans.push_back(num);
		}
		for(int i=seconde_row*4+1;i<=16;i++)
			cin>>num;
		//得出结果
		if(ans.size()>1)
			cout<<"Case #"<<c<<": Bad magician!"<<endl;
		else if(ans.size()==0)
			cout<<"Case #"<<c<<": Volunteer cheated!"<<endl;
		else
			cout<<"Case #"<<c<<": "<<ans[0]<<endl;
	}
	return 0;
}
