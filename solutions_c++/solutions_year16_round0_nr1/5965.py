#include<iostream>
#include<vector>
#include<fstream>
#include<string>
#include<sstream>
#include<cstdlib>

using namespace std;


void update_digits(int n, vector<int>&A)
{
    int i=n;
    while(i>0)
    {
        A[i%10] = 1;
        i = i/10;
    }

}

int sum(vector<int>A)
{
    int ans = 0;
    for(int i=0;i<A.size();i++)
    {
        ans += A[i];
    }
    return ans;
}

string func(int n)
{
    vector<int>A(10,0);
    if(n==0) return "INSOMNIA";
    int counter = 0;
    int m=n;
    while(counter < 10)
    {
        update_digits(m,A);
        counter = sum(A);
        m += n;
    }
    stringstream ss;
    ss << m-n;
    string str = ss.str();
    return str;
}

int main()
{
    int total;
    int i = 1,num;
	ifstream infile;
	ofstream ofile;
	ofile.open("output.txt");
	infile.open ("A-large.in");
    infile>>total;
        while(i <=total)
        {
            infile>>num;
            ofile<<"Case #" << i << ": "<<func(num)<<endl;

            i ++;
        }

	infile.close();
	ofile.close();
	return 0;
}

