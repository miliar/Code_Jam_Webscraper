#include <iostream>
#include <vector>
#include <string>
using namespace std;

string search(vector<int>P,string ans);

int N,sum=0;
int main()
{
	int T;
	cin>>T;
	for(int i=0;i<T;i++)
	{
		int temp;
		vector<int>P;
		cin>>N;
		for(int j=0;j<N;j++)
		{
			cin>>temp;
			sum+=temp;
			P.push_back(temp);
		}

		string ans = search(P,"");
		cout<<"Case #"<<i+1<<": "<<ans<<endl;
	}
	return 0;
}

bool check(vector<int> P)
{
	double sum;
	for(int i=0;i<P.size();i++)
		sum+=P[i];
	for(int i=0;i<P.size();i++)
	{
		if(P[i]/sum >0.5)
			return false;
	}
	return true;

}

string search(vector<int>P,string ans)
{
	int i=0;
	//cout<<"dd:"<<ans<<endl;

	for(i=0;i<P.size();i++)
	{
		if(P[i]==0)
			continue;
		P[i]--;
		char ch = ('A'+i);
		if(check(P) == true)
		{
			string temp = search(P,ans+ch+' ');
			if(temp.compare("0") !=0 )
				return temp;
		}
		for(int j=0;j<P.size();j++){
			if(P[j]==0)
				continue;
			P[j]--;
			char ch2= ('A'+j);
			if(check(P) == true)
			{
				string temp = search(P,ans+ch+ch2+' ');
				if(temp.compare("0") != 0)
					return temp;
			}
			P[j]++;
		}
		P[i]++;
	}
	int check=0;
	for(i=0;i<P.size();i++)
	{
		if(P[i]!=0)
			return "0";
	}
	return ans;
}
