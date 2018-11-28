#include <iostream>
#include <string>
using namespace std;

string A;
string search(string ans);
int main()
{
	int c;
	cin>>c;
	for(int i=0;i<c;i++)
	{
		string ans;
		cin>>A;
		ans=A[0];
		cout<<"Case #"<<(i+1)<<": ";
		cout<<search(ans)<<endl;
	}
}

string search(string ans)
{
	if(ans.length() == A.length())		return ans;
	string temp1 = search(A[ans.length()]+ans);
	string temp2 = search(ans+A[ans.length()]);

	if(temp1.compare(temp2)<0)
		return temp2;
	return temp1;

}
