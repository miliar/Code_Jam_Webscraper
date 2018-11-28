#include<iostream>
#include<vector>
#include<fstream>
#include<string>
#include<sstream>
#include<cstdlib>

using namespace std;

int sum(vector<int>A)
{
    int ans = 0;
    for(int i=0;i<A.size();i++)
    {
        ans += A[i];
    }
    return ans;
}

string func(string pc)
{
    int n = pc.size();
    vector<int>A(n,0);
    int ans = 0;
    for(int i=0;i<n;i++)
    {
        if(pc[i] == '+') A[i] = 1;
    }
    int i=n-1;

    while(i>0)
    {
        if(ans %2 ==0)
        {
            if(A[i] == 1) i--;
            else if(A[i] == 0 && A[i-1] == 0) i--;
            else {i--;ans++;}
        }

        else
        {
            if(A[i] == 0) i--;
            else if(A[i] == 1 && A[i-1] == 1) i--;
            else {i--;ans++;}
        }

    }
    if(A[0] == 0 && ans%2 ==0) ans++;
    else if(A[0] == 1 && ans%2 ==1) ans++;

    stringstream ss;
    ss << ans;
    string str = ss.str();
    return str;
}

int main()
{
    int total;
    int i = 1;
    string pc;
	ifstream infile;
	ofstream ofile;
	ofile.open("output.txt");
	infile.open ("B-large.in");
    infile>>total;
        while(i <=total)
        {
            infile>>pc;
            ofile<<"Case #" << i << ": "<<func(pc)<<endl;

            i ++;
        }

	infile.close();
	ofile.close();
	return 0;
}


