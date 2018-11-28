#include <iostream>
#include <set>
#include <map>
#include <vector>
#include <fstream>
#include <math.h>
#include <stack>
using namespace std;

long long getbase(int base,long long number)
{
    long long result = 0;
    int power = 0;
    while(number!=0)
    {
        int rem = number%10;
        result += rem*pow(base,power++);
        number /=10;
    }
    return result;
}

vector<long long> getallbaseupto10(long long number)
{
    int power = 0;
    vector<long long> result(11);
    int temp;
    for(int base = 2;base<=10;base++)
    {
        long long res = 0;
        temp = number;
        while(temp!=0)
        {
            long long rem = temp%2;
            res += rem*pow(base,power++);
            temp /=2;
        }
        result[base] = res;
    }
    return result;
}
bool isprime(long long n)
{
    if(n==2||n == 3)
        return true;
    for(long long i = 2;i<=sqrt(n);i++)
    {
        if(n%i==0)
            return false;
    }
    return true;
}

class IntSet
{

    public:
    set<int> divisors;
    bool operator<(IntSet x)
    {

        return false;
    }
    bool operator>(IntSet x)
    {
        if(this->divisors.size() > x.divisors.size())
            return true;
        return false;
    }

};
struct greater1{
  bool operator()(const IntSet& a,const IntSet& b) const{
      if(a.divisors.size() < b.divisors.size())
        return true;
  }
};

#include <string>
int main()
{
    ifstream infile("B-large.in");
    cin.rdbuf(infile.rdbuf());
	ofstream outfile("pb2out.txt");
    cout.rdbuf(outfile.rdbuf());
    string temp;
	int n;
	cin>>n;
	for (int i = 0; i < n; i++)
	{
		cin>>temp;
		temp += "+";
		int count = 0;
		if(i == 17)
		{
			;//cout<<"hello";
		}
		for(int j = 0;j<temp.size()-1;j++)
		{
			if(temp[j]!=temp[j+1])
				count++;
		}
		cout<<"Case #"<<i+1<<": "<<count<<endl;

	}

	return 0;
}
