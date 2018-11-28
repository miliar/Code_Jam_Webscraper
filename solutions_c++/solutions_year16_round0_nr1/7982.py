#include<iostream>
#include<set>
using namespace std;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	set<int> digits;
	int c,n,count,i;
	cin >>c;
	for(int z=1;z<=c;z++){
		count=0;i=0;
		digits.clear();
		cin>>n;
		if(n==0){
			cout<<"Case #"<<z<<": INSOMNIA"<<endl;
			continue;
		}
		while(digits.size()<10){
			i++;
			int x=i*n;
			while(x>0){
				if(digits.find(x%10)==digits.end())
				digits.insert(x%10);
				x=x/10;
			}
		}
		cout<<"Case #"<<z<<": "<<i*n<<endl;
	}
	return 0;
}